import json
import requests

api_token= "26e370b153ab65c59460078cebdbbb5b"



headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

def get_city():
    return input('enter city name')
def get_account_info():

    api_url = '{0}account'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

if __name__ == '__main__':




    import requests, json

    # enter your api key here
    api_key = "26e370b153ab65c59460078cebdbbb5b"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # take a city name from city_field entry box
    city_name = get_city()

    # complete_url variable to store complete url address
    complete_url = (f'{base_url}appid ={api_key}&q ={city_name}')

    account_info = get_account_info()

    if account_info is not None:
        print("Here's your info: ")
        for k, v in account_info['account'].items():
            print('{0}:{1}'.format(k, v))

    else:
        print('[!] Request Failed')
