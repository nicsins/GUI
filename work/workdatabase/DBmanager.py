import sqlite3
import re


def get_Date():
    da = re.compile(r'\d\d/\d\d/\d\d\d\d')

    while True:
        try:
            day = input('please enter the date work was performed')
        except ValueError:
            print('Please enter the proper date')
            continue
        if not day != da:
            print('please try again only', end='')
            continue
        else:
            break
    return day

def get_location():
    locatio = ["Warehouse", "FourPlex", "Chicken", "Oliver", "Lisa's",
               "Purple", "PennBro", "Gear", "MissCandi", "Keith", "Other",
               "lowry"]
    while True:
        spot = input("please enter location choose")
        if spot.lower() not in [i.lower() for i in locatio]:
            print("must be one of these...", *locatio, sep=',')
            continue
        else:
            break
    return spot.lower()

def get_Apt():
    return input("please enter apt number or description of location")

def get_description():
    return input(
        "Please enter a brief description of the work needed to be completed")

def get_Hours():
    while True:
        try:
            hours = float(input(
                'please enter the number of hours needed to be completed'))
        except ValueError:
            print("must be a valud number can be a decimal if needed no fractions")
            continue
        if hours < 0:
            print("must be more than 0")
            continue
        else:
            break
    return hours

def get_log_entry():

    return get_Date(), get_location(), get_Apt(), get_description(),get_Hours()






if __name__ == '__main__':
    # connecting to the database
    connection = sqlite3.connect("PennBroDB.db")

    # cursor
    crsr = connection.cursor()

    date, loc, apt, desc, hr =get_log_entry()
    crsr.execute(
        "INSERT INTO WorkLog (Date,Location,Apartment,Description,Hours)VALUES (?,?,?,?,?)",
        (date, loc, apt, desc, hr))
    connection.commit()
    print('your entry has been recorded')