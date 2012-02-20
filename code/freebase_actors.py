import urllib
import json

# Query parameters
query = [{"type": "/tv/tv_actor", "id": []}]
query_envelope = {'query': query}  
         
# Service url
service_url = 'http://api.freebase.com/api/service/mqlread'
url = service_url + '?query=' + json.dumps(query_envelope)

# Perform request
response = json.loads(urllib.urlopen(url).read())

# Read results
for actor in response['result']:
    print actor['id']