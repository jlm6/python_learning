from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
bidder_dict={}
def findoutwinner(bidder_dict):
  winner = ""
  highest = 0
  for bidder in bidder_dict:
    if bidder_dict[bidder] > highest:
      highest = bidder_dict[bidder]
      winner = bidder
  print(f"The winner is {winner} and the bid price is ${bid_price}.")
print(logo)
end_game = False

while not end_game:

  bid_name = input("What is your name?: ")
  bid_price = float(input("What is your bid price? $"))
  play_again = input("Is there any other bidder? Type yes or no\n").lower()

  bidder_dict[bid_name] = bid_price

  if play_again == 'yes':
    clear()
  else:
    end_game = True


findoutwinner(bidder_dict)
