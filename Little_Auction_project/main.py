import art
from replit import clear

print(art.logo)

end_game = False
dict_info= {}
bid_price = 0
winner = ""

def dict_create(target_person, target_bid):
  dict_info[target_person] = target_bid

while not end_game:

  print("Welcome to the secret auction program!")
  person = input("What is your name?!: ")
  bid = int(input("What is your bid price!? $"))

  dict_create(person, bid)
  reply = input("Are there any other bidders!?, type yes or no \n").lower()
  if reply == 'yes':
    clear()
  else:
    end_game = True

for key in dict_info:
  if dict_info[key] > bid_price:
    bid_price = dict_info[key]
    winner = key

print(f"The winner is {winner} and the bid price is {bid_price}.")

