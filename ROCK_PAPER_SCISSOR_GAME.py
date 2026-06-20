import random
def get_choices():

    person_choice= input("Choose rock, paper, or scissors: ")
    option = ["rock", "paper", "scissors"]
    computer_choice=random.choice(option)
    choices = {"person": person_choice, "computer": computer_choice}
    return choices

def check_win(person,computer):
    print(f"You chose {person}, computer chose {computer}")
    if person == computer:
        
        return "It's a tie!"
    elif person == "rock":  
      if computer == "scissors":
          return "rock smashes the scissors, you win!" 
      else:
          return "paper covers the rock , you lose!"
    elif person == "paper":  
      if computer == "scissor":
          return "scissors cuts the paper, you lose!" 
      else:
          return "paper covers the rock , you win!"
    elif person == "scissor":  
      if computer == "paper":
          return "scissors cuts the paper, you win!" 
      else:
          return "rock smashes the scissor , you lose!"   
choices = get_choices()
result = check_win(choices["person"], choices["computer"])
print(result)


