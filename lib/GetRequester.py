import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        the_list = []
        items = json.loads(self.get_response_body())
        for item in items:
            the_list.append(item)
        
        print (the_list)
        return the_list
    

api_1 = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
api_1.load_json()