from game_data import data
from art import logo, vs
from random import randint
import os

def generate_data():
    return data[randint(0,49)]
def game():
    dict_1={}
    dict_2={}
    check_num=0
    count=0
    dict_1=generate_data().copy()
    dict_2=generate_data().copy()
    while dict_1['name'] == dict_2['name']:
        dict_2=generate_data().copy()
    game=True
    while game:
        print(logo)
        max_num=max(dict_1['follower_count'],dict_2['follower_count'])
        print(f"Compare A: {dict_1['name']}, a {dict_1['description']}, from {dict_1['country']}.\n")
        print(vs,'\n')
        print(f"Compare B: {dict_2['name']}, a {dict_2['description']}, from {dict_2['country']}.\n")
        
        user_choice=input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_choice=='A':
            check_num=dict_1['follower_count']
        elif user_choice == 'B':
            check_num=dict_2['follower_count']
        if check_num==max_num:
            count+=1
            dict_1.update(dict_2)
            dict_2=generate_data().copy()
            while dict_1['name'] == dict_2['name']:
                dict_2=generate_data().copy()
            os.system('cls')
            continue
        else:
            os.system('cls')
            print(f"Sorry, that's wrong. Final score: {count}")
            game=False


game()