import os
print("Welcome to the secret auction program.")
nominies={}
nominies_num=True

while nominies_num:
    name=str(input("What's your name? "))
    bid=int(input("What's your bid? $"))    
    nominies[name]=bid
    others=str(input("Are there any other bidders? Type 'yes' or 'no'. ")).lower()
    os.system('cls')
    if others=='yes':
        continue
        
    else:
        nominies_num=False
    
highest_bid=0
winner_name=""
for key in nominies:
    if nominies[key]>highest_bid:
        highest_bid=nominies[key]
        winner_name=key
print(f"The winner is {winner_name} with a bid of ${highest_bid}.")