import json
with open("./topviews-2024_03.json") as f:
    x = json.load(f)
    for i in x:
        print(i['article'])
