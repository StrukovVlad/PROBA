import requests

url = 'https://www.youtube.com/results'

query ={'search_query': 'audi'}

response = requests.get(url, params=query, timeout =2y

print(response.url)
print(response.content)
print(response.status_code)

# data = response.json()
# print(json.dumps(data, indent=2))
