import csv
import PySimpleGUI as sg
import numpy as np
from random import shuffle

i = 2
mark = ["♤","♧","♡","♢"]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_deck = []
player =[]
dealer = []
player_hand = []


class User:
    
    userName = ""
    password = ""
    money = 10000
    
    def __init__(self):
        print("ユーザ登録なら「c」、ログインなら「l」を入力してください")
        ans = input("c/l => ")
        if ans == "c":
            self.characreate()
        elif ans == "l":
            self.login()

    def characreate(self):
        self.userName = input("名前を入力してください(10文字以内) => ")
        self.Character_limit_name(self.userName)
        print(f"ようこそ{self.userName}")
        self.password = input("パスワードを入力してください(半角英数字,10文字以内) => ")
        self.Character_limit_pass(self.password)
        print("パスワードが設定されました")
        self.showstatus()
        with open('information.csv','a') as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')
            writer.writerow([self.userName,self.password])
            csvfile.close()
    
    def showstatus(self):
        print(f"UserName[{self.userName}],Money[{self.money}],pass[{self.password}]")

    def Character_limit_name(self,username):
        if len(username) == 0 or len(username) > 10:
            username = input("名前を入力してください(10文字以内) => ")
            self.userName = username
            if len(username) == 0 or len(username) > 10:
                self.Character_limit_name(username)
        return self.userName
    
    def Character_limit_pass(self,password):
        if len(password) == 0 or len(password) > 10 or password.isascii() == False or password.isalnum() == False:
            password = input("パスワードを入力してください(半角英数字,10文字以内) => ")
            self.password = password
            if len(password) == 0 or len(password) > 10 or password.isascii() == False or password.isalnum() == False:
                self.Character_limit_pass(password)
        return self.password 
    
    def login(self):
        self.login_name()
        print("YES")

    def login_name(self):
        with open("information.csv","r") as df:
            name = input("ユーザネームを入力してください => ")
            csv.reader(df)
            for row in csv.reader(df):
                if row[0] == name:
                    self.login_pass()
        return name

        
    def login_pass(self):
        with open("information.csv","r") as df:
            pw = input("パスワードを入力してください => ")
            csv.reader(df)
            for row in csv.reader(df):
                if row[1] == pw:
                    print("ようこそ")
    
    def GameStart(self):
        print("ゲームスタート!!!")
        

        

class Bet:
    bet = 0
    money = 10000
    def __init__(self):
        self.set(self.money)
        print(f"{self.bet},{self.money}")
        
    def set(self,money):
        if money == 0:
            print("掛け金が不足しています")
        else:
            try:
                self.bet = int(input("掛け金を入力してください(半角数字) => "))
                if self.bet > money:
                    print(f"所持金が足りません(所持金{money})")
                    self.set(money)
            except ValueError:
                print("半角数字で入力してください")
                self.set(money)
            print(f"掛け金を{self.bet}円に設定しますか？(所持金{self.money}円)")
            self.ans_bet(self.bet,money)
        return self.bet,self.money
    
    def ans_bet(self,bet,money):
        ans = input("(Y/N) => ")
        if ans == "Y" or ans == "y":
            money = money - bet
            self.money = money
            print(f"掛け金を{bet}円に設定しました(所持金{self.money}円)")
            return self.money
        elif ans == "N" or ans == "n":
            print("掛け金を再設定します")
            self.set(money)
        else:
            self.ans_bet(bet,money)



class Deck:
    def __init__(self):
        self.deck = []
    def createDeck(self):
        for i in mark:
            for j in number:
                self.deck.append([i,j])
        shuffle(self.deck)
    def pop(self):
        return self.deck.pop()