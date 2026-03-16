import requests


def search_web(query):
    url = 'https://api.example.com/search'
    response = requests.get(url, params={'q': query})
    if response.status_code == 200:
        return response.json()
    else:
        return None


def format_search_results(results):
    if not results:
        return 'No results found.'
    formatted_results = []
    for item in results['items']:
        formatted_results.append(f"Title: {item['title']}, URL: {item['link']}")
    return '\n'.join(formatted_results)