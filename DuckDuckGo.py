import requests
import json
import unittest


class DuckDuckGo(unittest.TestCase):
    def test_presidents(self):
        president = open('presidents.txt', 'r')
        count = 0
        list_presidents = []

        for line in president:
            count += 1
            list_presidents.append(line.strip())

        print(list_presidents)

        request = requests.get("https://api.duckduckgo.com/?q=presidents of the united states&format=json")
        data = request.json()
        # print(json.dumps(data["RelatedTopics"], indent = 5))

        for line in data["RelatedTopics"]:
            print(line["Text"])

        for president in list_presidents:
            self.assertTrue(any(president in line["Text"] for line in data["RelatedTopics"]))


president = open('presidents.txt', 'r')
count = 0
list_presidents = []

for line in president:
    count += 1
    list_presidents.append(line.strip())

print(list_presidents)

request = requests.get("https://api.duckduckgo.com/?q=presidents of the united states&format=json")
data = request.json()
# print(json.dumps(data["RelatedTopics"], indent = 5))

for line in data["RelatedTopics"]:
    print(line["Text"])
