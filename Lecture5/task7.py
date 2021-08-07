import codecs
import json


profits = []
firms_dictionary = {}
with codecs.open('firms.txt', 'r', 'utf-8-sig') as f:
    lines = f.readlines()
    for line in lines:
        words = line.split(' ')
        revenue = int(words[2]) - int(words[3])
        if revenue >= 0:
            profits.append(revenue)
        firms_dictionary[words[0]] = revenue

average_profit = {}
average_profit['average_profit'] = sum(profits)/len(profits)
json_list = [firms_dictionary, average_profit]
print(json_list)
with open('json.txt', 'w') as jsonInput:
    json.dump(json_list, jsonInput)