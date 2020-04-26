# cmpe273-assignment2
Scantron evaluation using Flask API<br>
- An SQLite database has been created and pre-initialised with necessary table schemas.<br>
  The flask application will store and retrieve all data from this database.<br>
- Upload a file to add a new test using the /tests endpoint (POST)<br>
  The file must contain a json in the foloowing format:<br>
  {<br>
    "subject": "",<br>
    "answer_keys": {<br>
      "1": "A",<br>
      "2": "B",<br>
      "3": "C",<br>
        .<br>
        .<br>
        .<br>
      "49":"D",<br>
      "50": "E"<br>
    }<br>
  }<br>
- Upload a file to evaluate your test using the tests/{test_id}/scantrons endpoint (POST)<br>
  The file must be in the following format:<br>
  {<br>
    "name": "Foo Bar",<br>
    "subject": "Math",<br>
    "answers": {<br>
      "1": "A",<br>
      "2": "B",<br>
      "3": "C",<br>
        .<br>
        .<br>
        .<br>
      "49": "D",<br>
      "50": "E"<br>
  }<br>
- To check all submissions for a test, execute a GET request against the /tests/{test_id} endpoint<br>
