import requests

class WikipediaSearch:
    def __init__(self):
        self.base_url = 'https://en.wikipedia.org/w/api.php'

    def search(self, query):
        params = {
            'action': 'query',
            'list': 'search',
            'srsearch': query,
            'format': 'json'
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

# Example usage
if __name__ == '__main__':
    wiki_search = WikipediaSearch()
    result = wiki_search.search('Python programming')
    print(result)