import requests


get_snippets_url = 'http://127.0.0.1:8000/snippets/'
get_snippet_url = 'http://127.0.0.1:8000/snippets/1/'


response_get_snippets = requests.get(get_snippets_url)
response_get_snippet = requests.get(get_snippet_url)

print(response_get_snippets)
print(response_get_snippets.text)

print(response_get_snippet.text)