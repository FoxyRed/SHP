import os
from sys import exit as sexit
from math import isqrt, gcd, factorial,floor
from sympy import mod_inverse, randprime
from time import sleep
from random import randint,choice
import threading
from inputimeout import inputimeout, TimeoutOccurred




# Main function to choose between games
def main():
    clear_screen()
    initialize_database()
    print("Welcome to the printer of Healian")
    sleep(2)
    randomwords, shapes,randomaspects= get_data() 
    goal_num = display_menu(["I want to print an object", "I want to design an object"])
    if goal_num == 1:
        goal = "print"
    elif goal_num == 2:
        goal = "design"
    else:
        main()
    objects_made_by_printer = [
        f"I want to {goal} basic equipment or tools",
        f"I want to {goal} electronics, computers, sensors or deflectors",
        f"I want to {goal} autonomous robots or cybernetic implants",
        f"I want to {goal} mechanical machinery, weapons, or armor"
    ]
    goal_lvl = display_menu(objects_made_by_printer)
    skill = [
        "I lack any skill for this",
        "Trust me for this, I'm an Ingenieur (N1)",
        "Trust me for this, I'm an Electronic Ingenieur (N2)",
        "Trust me for this, I'm an Robo/Cybernetics Ingenieur (N3)",
        "Trust me for this, I'm an Mechanical Ingenieur (N2)"
    ]
    skill_lvl = display_menu(skill)
    ## set skill level relative to the task if user did not understand
    
        
    hack = display_menu(
        ["I am not able/willing to HAX0R",  "I try some hacking without the skill (notify SL)","1 W1ll d0 S0m3 SX1ll3D H4X0R1N' (notify SL)"]
    )
    skill_lvl,goal_lvl,hack,goal,diff=find_diff(skill_lvl,goal_lvl,hack,goal)
    hacked_done = False
    if not(hack==1):
        print("W1th0ut 4 d0ubt!")
        count_down()
        
        repeat=True
        while repeat:
            if hack >= 2:
                layers=randint(1,6-hack)
                if not(hacking(layers,14-4*hack)):
                    print("Sorry you failed :( Try again?")
                    if display_menu(["I will try again my H4KZ0R1N9","No, will skip it (No SL needed anymore)"])==2:
                        print("oké")
                        repeat=False
                        hacked_done = False
                    else:
                        print("L4tz pwn")
                        repeat=True
                        hacked_done = False
                else:
                    repeat=False
                    hacked_done = True
            else:
                repeat=False
                hacked_done = False
        print(f"Hakzor done\n ")
    clear_screen()
    print("What do you want to print?")
    easy = display_menu(
        ["It will be very difficult task, highly complex","Though, but doable","Something easy (because it is based on something in the database)","Just loading it from a disk"]
    )
    easy = easy - 0.5
    object_name = input("Under what name to put it in the logs?")
    print("Did you asked Henk for a prediction?")
    henk = display_menu(
        ["Yes","No"]
    )
    if henk == 1: 
        printtijd=get_int(f"How many minutes did Henk say for the {object_name} to print?")
        henked=True
    else:
        printtijd=get_int(f"How many minutes you guess for the {object_name} to print?")
        henked=False  
    repeat=0
    print(f"Starting with the print of {object_name}!\nExpected time: Unkown\nNumber of manual corrections to expect:{max(0,(4-easy)*(1+goal_num)+randint(-2,2))}")
    while repeat < (4-easy)*(1+goal_num):
        problem=1
        for i in range(randint(4,40)):
            sleep(0.5)
            if i % 8 ==0 :
                print(f"...working on sketching the next {choice(randomwords)}...")
                problem*=-1
        problem+=randint(0,6)
        
        print("Want to keep working on the next section(s)?")
        stop = display_menu(
        ["Yes, go go go!","No, stop."]
        )
        if stop == 1: 
            done=True
            falserepeat=True
        else:
            done = False
            goal_num=-1
            falserepeat=False
        while falserepeat:
            if goal == "design":
                if problem < 2:
                    print("A problem has arisen. A parameter is incorrect. Can you find the mistake?")
                    sleep(2)
                    count_down(10)
                    print("A problem has arisen. A parameter is incorrect. Can you find the mistake?")
                    if sequence_prediction_game(goal=max(1,int(diff/2)),replay=int((2+abs(goal_lvl))/easy)):  # You can adjust the goal value as needed
                        falserepeat=False
                    else:
                        print("A different approach is needed.")
                elif problem <4:
                    print("A problem has arisen. Please correct the following vector as we need a rotation to fit the object in the printer. Ready your self.")
                    sleep(2)
                    count_down(10)
                    print("A problem has arisen. Please correct the following vector as we need a rotation to fit the object in the printer. Ready your self.")
                    if vector_game(dimensions=int((6+3*abs(goal_lvl))/easy),difficulty=1+diff,tolerance=((1+abs(goal_lvl))*abs(skill_lvl)*2*(1+hack))):
                        falserepeat=False
                    else:
                        print("A different approach is needed.")
                else:
                    print(f"Added {choice(randomaspects).lower()} [{problem}]")
                    falserepeat=False
        repeat+=1
    add_data_point(name=object_name, kind_int=goal_lvl, printtime=printtijd, sl_approved=henked, sl_checked=None, advanced=4.5-easy, hacked=hacked_done, successful_drawn=repeat)


if __name__ == "__main__":
    main()
