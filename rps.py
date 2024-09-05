#really simple rps by svrbrndmg [at] proton.me

import random as rm

rps = ["rock", "paper", "scissors"]
points = 0
aipoints = 0

print("Let's play RPS! There are 5 rounds! You get 1 point for a win! Whoever has the most at the end, is the winner!! :3", end='\n')

while True:
    # main gameloop
    points = 0
    aipoints = 0
    # resetting points here so you can't win with previously earned points.
    for i in range(5):
       choice = input("Rock, paper, scissors! ")
       ai = rm.choice(rps)
       print("I chose: " + ai + "!")
       if choice == "rock" and ai == "paper" or choice == "paper" and ai == "scissors" or choice == "scissors" and ai == "rock":
          print("I've won! 1 point to me! :D")
          aipoints += 1
       elif choice == "rock" and ai == "scissors" or choice == "paper" and ai == "rock" or choice == "scissors" and ai == "paper":
          print("I've lost! 1 point to you! :(")
          points += 1
       elif choice == "rock" and ai == "rock" or choice == "paper" and ai == "paper" or choice == "scissors" and ai == "scissors":
          print("It's a draw! No-one gets any points! :p")
        # should be self-explanatory. you choose an option, then the ai "chooses"
        # (randomized) and you see how it plays out, then get your points.
    if points > aipoints:
        print("You've won! Bravo!! ")
    elif aipoints > points:
        print("I've won! Yay!! ")
    else:
        print("Shucks, it's a draw in points! ")
        # this is here in case someone wants to change the game rotation to
        # more than 5, to make it easier to do so. rn, with 5 games, it is
        # impossible to draw
    restart = input("Wanna play again? ")
    if restart.strip().lower() == "yes":
        pass
    elif restart.strip().lower() == "no":
        quit()
    else:
        print("Not a valid response, I'm afraid! Now restarting...")
    # restart question. strip lower removes capitalization so all
    # strings get accepted, even "  YES ". how does it restart?
    # well, by passing (not doing anything), the while loop has
    # reached the end of it's rope and has to start again. by
    # quitting, it is, well just quitting.
quit()
