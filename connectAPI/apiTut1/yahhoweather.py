import json,requests

key="k9NjGpE2jXi50MG0km7BoDgI25m2Bq2L "
locationKey=input('please enter a the city where you would lie to see the current weather')

url=f"http://dataservice.accuweather.com/currentconditions/v1/{locationKey}"

headers = {'Accept': 'application/json',
          }
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(json.loads(response.content.decode('utf-8')))
else:
    print('not a valid city ')


