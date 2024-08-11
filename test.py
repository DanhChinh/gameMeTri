import requests

response = requests.get('https://quotable.io/random')
quote = response.json()

print(f"{quote['content']} - {quote['author']}")
