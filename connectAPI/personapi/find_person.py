




class Person:
    def __init__(self,name,street1,street2,city,postal,state,country,historical,metro,match,alt):
        self.__name=name
        self.__street1=street1
        self.__street2=street2
        self.__city=city
        self.__postal=postal
        self.__state=state
        self.__country=country
        self.__historical=historical
        self.__metro=metro
        self.__match=match
        self.__alt=alt
    #setters
    def __set_name(self, owner, name):
        self.__name=name
    def __set_street1(self,street1):
        self.__street1=street1
    def __set_street2(self,street2):
        self.__street2=street2
    def __set_city(self,city):
        self.__city=city
    def __set_postal(self,postal):
        self.__postal=postal
    def __set_state__(self, state):
        self.__state=state

    #getters
    def __get_name(self,name):
        return self.__name
    def __get_street1(self,street1):
        return self.__street1
    def __get_street2(self,street2):
        return self.__street2
    def __get_city(self,city):
        return self.__city
    def __get_postal(self,postal):
        return self.__postal
    def __get_state(self,state):
        return self.__state
    def __get_country(self,country):
       return self.__country
    def __get_historical(self):
        return True
    def __get_metro(self):
        return True
    def __get_match(self):
        return " phonetic"
    def __get_alt(self):
        return True


import json, requests

'''
https://proapi.whitepages.com/3.0/person?name=Giaan+Qiuntero&address.city=Lynden&address.state_code=WA&api_key=KEYVAL

'''
api_key = '1a4dede691984f9282a1162ca5ca9b6c'

call_list = ['name',
             'address.street_line_1',
             'address.street_line_2',
             'address.city',
             'address.postal_code',
             'address.state_code',
             'address.country_code',
             'search.historical',
             'search.metro',
             'search.name_match',
             'search.alternate_name']



def make_call():
    name =input('enter name')
    # street1 = input('enter line1 address')
    # street2 = input('enter line 2 address')
    city =input('enter city')
    postal=input('enter zip code')
    state=input('enter 2 letter state code')
    # country=input('enter 2 letter country code')
    # info=[name,street1,street2,city,postal,state,country,"true","true","phonetic","true"]

    complete_url = f"https://proapi.whitepages.com/3.0/person?name={name}&address.city={city}&address.postal_code={postal}&address.state_code={state}&search.historical=true$search.metro=true&search.alternate_name=true&api_key={api_key}"

    response = requests.get(complete_url)
    content=response.content



    print(content)


if __name__ == '__main__':
    make_call()