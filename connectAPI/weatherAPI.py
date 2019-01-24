import json,requests

city=input('enter city')
key="k9NjGpE2jXi50MG0km7BoDgI25m2Bq2L "
# url=f"https://api.ipdata.co/1.1.1.1/{city}?api-key=47e03c175baca35edd3ad7ceead397fbf25cb401bb003fba75c6078d"

print(requests.get(url))


headers = {
    'Accept': 'application/json'
}
req = requests.get('https://api.ipdata.co/?api-key=47e03c175baca35edd3ad7ceead397fbf25cb401bb003fba75c6078d', headers=headers)




print(json.loads(req.content.decode('utf-8')))

