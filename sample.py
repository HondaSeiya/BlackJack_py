import csv

def login_name():
    with open("information.csv","r") as df:
        csv.reader(df)
        name = str(input("=> "))
        for row in csv.reader(df):
            if row[0] == name:
                login_pass()

def login_pass():
    with open("information.csv","r") as df:
        csv.reader(df)
        password = input("==> ")
        for row in csv.reader(df):
            if row[1] == password:
                print("GOOD")

login_name()      