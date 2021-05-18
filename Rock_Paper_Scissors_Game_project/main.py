import random
import image

select = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
bot_chose = random.randint(0, 2)
if select >= 3:
  print(
    "You type the wrong number, you lose!")
else:

  entry = [image.rock, image.paper, image.scissors]

  print(entry[select])

  bot_chose = random.randint(0, 2)
  bot = entry[bot_chose]
  print(f"Computer chose: {bot}")

#0 -> rock
#1 -> paper
#2 -> scissors

  if (select == 2 and bot_chose == 1) or (select ==1 and bot_chose ==0) or (select ==0 and bot_chose ==2):
    print(" You win the game.")
  elif select == bot_chose:
    print("We tie the game!")
  else:
    print(" You lose the game.") 
