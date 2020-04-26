from flask import Flask, escape, request
import json
import sqlite3
app = Flask(__name__)
tests = []
test_id = 0
DATABASE = "cmpe273.db"

#scantron_id = db_execute_query("select count('test_id') from cmpe273_tests")

def db_execute_query(query, args):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    db.commit()
    return result

def db_insert_query(query, args):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    db.commit()
    return cursor.lastrowid

scantron_id = db_execute_query("select count('test_id') from cmpe273_submissions",[])[0][0]

def grade_scantron(inputJson, sampleAnswer):
    score = 0
    report = {}
    for k in sampleAnswer:
        if k in inputJson["answers"] and sampleAnswer[k] == inputJson["answers"][k]:
            score += 1
        report[k] = { "actual":inputJson["answers"][k] , "expected":sampleAnswer[k] }
    return score,report

@app.route('/tests', methods=['POST'])  #Add a new test
def addNewTest():
    print("Add a new test . . .")
    if 'file' in request.files:
        request.files['file'].save("file.json")
        inputJsonFile = json.loads(open("file.json").read())
    new_test = {'subject': inputJsonFile["subject"], 'answer_keys': inputJsonFile["answer_keys"], 'submissions': []}
    q = 'insert into cmpe273_tests(subject,answer_keys) values(?,?)' 
    args = [new_test["subject"],json.dumps(new_test["answer_keys"])]
    new_test["test_id"] = db_insert_query(q, args)
    return {"result": new_test}

@app.route('/tests/<int:id>', methods=['GET'])  #Get details for a particular test
def getTestDetails(id):
    print("Getting test details . . . ")
    q = 'select test_id, submission from cmpe273_submissions where test_id='+str(id) #join cmpe273_submissions on cmpe273_tests.test_id=cmpe273_submissions.test_id'
    args = []
    result1 = db_execute_query(q, args)
    q = 'select test_id, subject, answer_keys from cmpe273_tests where test_id='+str(id)
    result2 = db_execute_query(q,args)
    if len(result2) > 0:
        final_result = {"test_id": result2[0][0],"subject": result2[0][1], "answer_keys": json.loads(result2[0][2]), "submissions": []}
        for r in result1:
            final_result["submissions"].append(json.loads(r[1]))
    else:
        final_result = {"result": "Invelid tests ID"}
    return final_result

@app.route('/tests/<int:id>/scantrons', methods=['POST']) #Upload a submission for a test
def addSubmission(id):
    global scantron_id
    if 'file' in request.files:
        request.files['file'].save("file.json")
        inputJsonFile = json.loads(open("file.json").read())
    name = inputJsonFile["name"]
    q = 'select answer_keys from cmpe273_tests where test_id='+str(id)
    result1 = db_execute_query(q,[])
    if len(result1) > 0:
        sampleAnswer = json.loads(db_execute_query(q,[])[0][0])
        score, report = grade_scantron(inputJsonFile, sampleAnswer)
        scantron_id = scantron_id + 1
        result = {"scantron_id": scantron_id, "scantron_url":"http://localhost:5000/files/scantron-"+str(scantron_id)+".json", "name": name, "subject": "Math", "score": score, "result":report}
        # Add result to submission
        q = 'insert into cmpe273_submissions(test_id,submission) values(?,?)'
        args = [id,json.dumps(result)]
        db_insert_query(q,args)
    else:
        result = {"result": "Invalid Test ID"}
    return result

