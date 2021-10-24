from art import logo, vs
from game_data import data
import random
from replit import clear

print(logo)
score = 0
game_flag = True
#generate a random account from the game data, beginning setup of two positions
account_a = random.choice(data)
account_b = random.choice(data)

#the game is repeatable
while game_flag:

  # making account at position B become the next account at position A
  account_a = account_b
  account_b = random.choice(data)
  
  if account_a == account_b:
    account_b = random.choice(data)


  def format_data(account):
    """Format the account data into printable format. takes the acc data and returns the printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_description} from {account_country}")

  def check_answer(guess, a_followers, b_followers):
    """take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers and guess == "a":
      return guess == "a"
    else:
      return guess == "b"




  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Compare B: {format_data(account_b)}.")


  #Ask user for a guess
  guess = input("Who has more followers? 'a' or 'b' ").lower()

  #get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  #clear the screen
  clear()
  print(logo)
  
  #Give feedback on their guess
  if is_correct:
    score += 1
    print(f"You are right! Current score: {score}.")
  else:
    game_flag = False
    print("Wrong!")





# import random
# from art import logo, vs
# from game_data import data
# from replit import clear

# # random data from game data and return follower's number
# def get_random_data():
#   return random.choice(data)


# #compare choose with examples,  #jesli tak, wybrany trafny wybor, zostaw example z wyzsza wartoscia
# #punktacja += 1
# def compare(a, b, choice, points):
#   if choice == "a" and a["follower_count"] > b["follower_count"]:
#     print("You are right!")
#     return points + 1
    
#   elif choice == "b" and b["follower_count"] > a["follower_count"]:
#     print("You are right!")
#     return points + 1
#   else:
#     print("You lose.")
#     print(f"You have {points} points.")
#     return 0
      



# clear()

# #two entries
# first_entry = get_random_data()
# second_entry = get_random_data()

# game_flag = True
# points = 0
# while game_flag:
#   #show logo, beginning
#   print(logo)
#   print(f"You have {points} points.\n\n")
#   print(f"A: {first_entry['name']}, {first_entry['description']} from {first_entry['country']}. ")
#   print(vs)
#   print(f"B: {second_entry['name']}, {second_entry['description']} from {second_entry['country']}. ")



#   #user's choice
#   choice = input("\n\nChoice between two options: 'a' or 'b': ")
#   points = compare(first_entry, second_entry, choice, points)

#   if points != 0:
#     print("Next round.")
#     first_entry = second_entry
#     second_entry = get_random_data()
#   else:
#     print("Game over.")
#     game_flag = False




  
