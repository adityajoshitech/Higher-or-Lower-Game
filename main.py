import art
import random
from game_data import data


def game_data_extractor(data_list,index_number):
    name=data_list[index_number]['name']
    follower_count=data_list[index_number]['follower_count']
    description=data_list[index_number]['description']
    country=data_list[index_number]['country']
    return name,follower_count,description,country

def correct_answer(follower_count_a,follower_count_b):
    if follower_count_a>follower_count_b:
        return "a"
    else:
        return "b"

def game():
    print(art.logo)
    current_score=0
    should_continue=True
    index1=random.randint(0,49)
    while should_continue:
        name,follower_count1,description,country=game_data_extractor(data,index1)
        print(f"Compare A: {name}, {description}, from {country}")
        print(art.vs)
        index2=random.randint(0,49)
        while index1==index2:
            index2=random.randint(0,49)
        name,follower_count2,description,country=game_data_extractor(data,index2)
        print(f"Against B: {name}, {description}, from {country}")
        guess=input("Who has more followers? Type 'A' or 'B': ").lower()
        print(art.logo)
        if guess==correct_answer(follower_count1,follower_count2):
            current_score+=1
            print(f"You're right! Current score: {current_score}.")
            index1=index2
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            should_continue=False

game()
