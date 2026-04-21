import requests


parameters = {
    "amount" : 10,
    "type" : "boolean"
}
response = requests.get("https://opentdb.com/api.php",params= parameters)
response.raise_for_status()
questions = response.json()


question_data = [question for question in questions["results"]]

