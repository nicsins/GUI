from tkinter import *
import xlrd
import datetime
import re
import csv
import pandas as pd

# file=open(r"Book1.csv")


# PennBro={"Date":['1/1/2019','1/2/2019','1/3/2019','1/4/2019','1/5/2019','1/7/2019','1/8/2019'],"Location":["Warehouse","Warehouse","lowry","lowry","Warehouse","lowry","FourPlex"],"Apartment":["boiler","boiler","roof","roof","roof","sonya","building"],"Description":["check on leaky boiler","replace 3 water heaters","patch roof","patch roof","patch roof","patch ceiling/break up toilet","check on rear entry lock"],"Hours":[1,9,4,4,3,2,1]}
#
#
#
# df=pd.DataFrame(PennBro)
# df.to_csv("work.csv",header="Penn Bro log", encoding='utf-8', index=False)
#
# print(df)





def get_Date():
    da= re.compile(r'\d\d/\d\d/\d\d\d\d')

    while True:
        try:
            day=input('please enter the date work was performed')
        except ValueError:
            print('Please enter the proper date')
            continue
        if not day!=da :
            print('please try again only', end='')
            continue
        else:
           break
    return day


def get_location():
    locatio=["Warehouse","FourPlex","Chicken","Oliver","Lisa's","Purple","PennBro","Gear","MissCandi","Keith","Other","lowry"]
    while True:
        spot=input("please enter location choose")
        if  spot.lower() not in [i.lower() for i in locatio]:
            print("must be one of these...",*locatio,sep=',')
            continue
        else:
            break
    return spot.lower()

def get_Apt():
     return input("please enter apt number or descrition of location")

def get_description():
    return input("Please enter a brief descrition of the work needed to be completed")

def get_Hours():
    while True:
        try:
            hours=float(input('please enter the number of hours needed to be completed'))
        except ValueError:
            print("must be a valud number can be a decimal if needed no fractions")
            continue
        if hours<0:
            print("must be more than 0")
            continue
        else:
            break
    return hours



def get_log_entry():
    import csv
    with open("work.csv","a") as file:
        writer=csv.writer(file)
        writer.writerow([get_Date(),get_location(),get_Apt(),get_description(),get_Hours()])

    print('your entry has been recorded')

def readFile():
   file=pd.read_csv("work.csv",sep=',',encoding='utf-8',index_col=False)
   df=pd.DataFrame(file)
   print(df)


if __name__ == '__main__':
    print("Here is the log to date")
    readFile()
    get_log_entry()
    readFile()