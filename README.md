# cmpe273-assignment2
Scantron evaluation using Flask API
- An SQLite database has been created and pre-initialised with necessary table schemas.<br>
  The flask application will store and retrieve all data from this database.<br?>
- Upload a file to add a new test using the /tests endpoint (POST)<br>
  The file must contain a json in the foloowing format:<br>
  {
    "subject": "",
    "answer_keys": {
      "1": "A",
      "2": "B",
      "3": "C",
        .
        .
        .
      "49":"D",
      "50": "E"
    }
  }<br>
- Upload a file to evaluate your test using the tests/{test_id}/scantrons endpoint (POST)<br>
  The file must be in the following format:<br>
  {
    "name": "Foo Bar",
    "subject": "Math",
    "answers": {
      "1": "A",
      "2": "B",
      "3": "C",
        .
        .
        .
      "49": "D",
      "50": "E"
  }<br>
- To check all submissions for a test, execute a GET request against the /tests/{test_id} endpoint<br>
