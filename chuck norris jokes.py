import requests

categories = ["animal", "career", "celebrity", "dev", "explicit", "fashion", "food", "history", "money", "movie",
              "music", "political", "religion", "science", "sport", "travel"]
jokes_list = []
for category in categories:
    response = requests.get(F"https://api.chucknorris.io/jokes/random?category={category}")
    jokes = response.json()
    jokes_list.append(jokes)
jokes_sort = sorted(jokes_list, key=lambda jokes_sort: jokes_sort['created_at'])
for i in range(len(jokes_sort)):
    print(
        F"Date: {jokes_sort[i]['created_at']}\nCategory: {jokes_sort[i]['categories']}\nText: {jokes_sort[i]['value']}",
        end='\n \n')
