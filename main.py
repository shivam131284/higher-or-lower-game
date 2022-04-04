from art import logo,vs
print(logo)
from game_data import data
import random 
import clear
score = 0
def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country= account["country"]
  return f"{account_name},a {account_descr} , from {account_country}"
def check_answer(guess,a_followers,b_followers):
  if a_followers > b_followers:
    return guess =="a"
  else:
    return guess == "b"
game_should_continue = True
while  game_should_continue:
  account_a = random.choice(data)
  account_b = random.choice(data)
  if account_a == account_b:
    account_a = random.choice(data)
  
  print(f"compare A:{format_data(account_a)}")
  print(vs)
  print(f"compare B:{format_data(account_b)}")
  
  guess=input("who has more followers a or b ?").lower()
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count , b_follower_count)
  clear()
  if is_correct:
    score += 1
    print(f"you're right! current score:{score}")
  else:
    game_should_continue= False
    print(f"unfortunately you're wrong! your final score:{score}")