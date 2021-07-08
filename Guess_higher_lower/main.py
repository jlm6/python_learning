from art import logo, vs
from game_data import data
from random import randint
from replit import clear

print(logo)

num1 = 0
num2 = 0
score = 0
is_over = False
user_pick = 0
against = 0

print(data[1])


def extract(data_list, number):
    full_name = data[number]['name']
    descriptions = data[number]['description']
    # follower_counts = str(data[number]['follower_count'])
    countrys = data[number]['country']
    # detail = full_name + ', ' + descriptions + ', ' + follower_counts + 'from ' + countrys
    detail = full_name + ', ' + descriptions + ', ' + 'from ' + countrys
    return detail


def compare_score(data, user_pick, against):
    global is_over
    if data[user_pick]['follower_count'] > data[against]['follower_count']:
        global score
        score += 1
        clear()
    else:
        print(f"Game over!, your score is {score}.")
        is_over = True


def number_select_2_ppl():
    global num1
    num1 = randint(0, 51)
    global num2
    num2 = randint(0, 51)
    if num2 == num1:
        num2 = randint(0, 51)

    person1 = extract(data, num1)
    person2 = extract(data, num2)

    print(f"Compare A: {person1} ")
    print(vs)
    print(f"Against B: {person2}")


def chooseside():
    selection = input('Who has more followers? Type A/B: ')
    global user_pick
    global against
    if selection == 'A':
        user_pick = num1
        against = num2

    else:
        user_pick = num2
        against = num1


while not is_over:
    number_select_2_ppl()
    chooseside()
    compare_score(data, user_pick, against)
