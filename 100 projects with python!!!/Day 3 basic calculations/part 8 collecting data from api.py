import requests
import json
raw_data = requests.get('https://opentdb.com/api.php?amount=5&category=9&difficulty=easy&type=boolean')
data = json.loads(raw_data.text)
print(data)
print(data.keys())
lst  = data['results']
# run a for loop adn one by one collect question
for each in lst:
    print('question:')
    print(each['question'])
    print('the answer is:')
    print(each['correct_answer'])

