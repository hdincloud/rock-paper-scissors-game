import random

def play_rock_paper_scissors():
  # List of possible choices
  choices = ['rock', 'paper', 'scissors']
  
  # Get the user's choice
  user_choice = input('Enter your choice (rock, paper, or scissors): ')
  
  # Make sure the user entered a valid choice
  if user_choice not in choices:
    print('Invalid choice')
    return
  
  # Get the computer's choice
  computer_choice = random.choice(choices)
  
  # Determine the winner
  if user_choice == computer_choice:
    print('It\'s a tie!')
  elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
    print('You win!')
  else:
    print('You lose!')

# Start the game
play_rock_paper_scissors()
