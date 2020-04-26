# cmpe273-assignment2
Scantron evaluation using Flask API
- Upload a file to add a new test using the /tests endpoint (POST)
  The file must contain a json in the foloowing format:
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
  }
- Upload a file to evaluate your test using the tests/{test_id}/scantrons endpoint (POST)
  The file must be in the following format:
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
  }
- To check all submissions for a test, execute a GET request against the /tests/{test_id} endpoint
