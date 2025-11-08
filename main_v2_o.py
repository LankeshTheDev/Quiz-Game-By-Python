
# ===============================================================
# 🧠  PROJECT: KAUN BANEGA CROREPATI - Quiz Game
# 👨‍💻  DEVELOPER: LANKESH TAYADE
# 🏫  CREATED BY: Lankesh Tayade 
# 💾  FILE: main.py
# 📅  VERSION: 1.0
# ⚙️  LANGUAGE: Python 3
# ===============================================================
#  DESCRIPTION:
#  This program simulates a text-based version of the popular
#  quiz game show "Kaun Banega Crorepati".
#  Players answer random questions to earn points, 
#  and their scores are saved to a leaderboard file.
# ===============================================================
#  NOTE:
#  © 2025 Lankesh Tayade. All Rights Reserved.
#  This file is part of a personal learning & portfolio project.
# ===============================================================


import random
from question import question_dict
from question import option_list


                    
leaderBoard = {}
question_no = 1
score = 0
def intro():
    global player_name
    print("---------------------------------------")
    print("Good afternoon, ladies and gentlemen!")
    print("---------------------------------------")
    print("WELCOME THE TO WORLD'S BIGGEST QUIZ SHOW")
    print("---------------------------------------")
    print("KAUN BANEGA ROADPATI")
    print("---------------------------------------")
    print("Presented By Lankesh Tayade")
    print("---------------------------------------")
    player_name = input("Enter your name: ")
    print("---------------------------------------")
    print(f"Welcome {player_name} To The Show")
    print("---------------------------------------")
    
def load_question():
    global computer_choice
    computer_choice = random.choice(list(question_dict.keys()))
    global answer_comp_choice
    answer_comp_choice = question_dict[computer_choice]


def ask_question():
    print(f"Q no.{question_no} {computer_choice}")
    global option
    option = random.sample(option_list,3)
    option.append(answer_comp_choice)
    random.shuffle(option)
    
def check_answer():
    global question_no
    global score
    no = 1
    for i in option:
        print(f"Option {no}:{i}")
        no+=1
    user_choice = input("Enter your choice: ").lower()
    if user_choice.lower() == answer_comp_choice.lower():
        print("Correct Answer,You Got 10+ Points")
        question_no+=1
        score+=10
 
    else:
        print(f"Wrong Anwser...correct answer {answer_comp_choice}")
        question_no+=1
        

def update_Score():
    global score
    global player_name        
    print("===========================")
    print(f"{player_name} your Score {score}", end="\n")
    print("----------------------------")

def show_Result():
    global score 
    if score >= 90:
        print("You are the Pro ")
        print("===========================")
    elif score >= 60 and score < 90:
        print("You are Good ")
        print("===========================")
    elif score >= 50 and score < 60:
        print("You are Average ")
        print("===========================")
    else :
        print("You are Noobb")
        print("===========================")

    
def save_Leaderboard():
    global score
    global player_name 
    global leaderBoard
    leaderBoard[player_name] = score
    with open("data.txt", "a+") as file:
        for key,value in leaderBoard.items():
            file.write(f"{key} = {value}\n")


intro()      
while True:
    score = 0
    question_no = 1

    while question_no <= 10:         
        load_question()
        ask_question()
        check_answer()
    update_Score() 
    show_Result()
    save_Leaderboard()

    ask_player =  input("Play again? (yes/no)")
    if ask_player != "yes":
        print("GAME OVER")
        break

                    
    









    