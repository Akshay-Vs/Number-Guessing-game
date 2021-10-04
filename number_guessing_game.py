#Number Guessing game
import random

	
pointwrite=open('point.txt','w')
root=open('point.txt','r')
point=root.read()

try:
	max_value =int(input('Enter your level : '))
	bots=str(input('Enter game mode \neg: single, multiplayer\n\t\t: '))
except Exception:
		print('\n\tInvalid input\n\tGame over\n\n')
if max_value==0:
		print("\n\tLevel zero is not available\n\t\tGame over\n\nError : ")
		

remaining_attempts=float(1)
remaining_attempts=75%max_value

player_state=bool(False)
bot_state=bool(False)

if max_value<=10:
	level="Easy"
elif max_value>10 and max_value<=40:
	level="Hard"
else:
	level="Impossible"
	remaining_attempts=remaining_attempts -15% remaining_attempts

print('Level applied : ',level,"\nYou got ", remaining_attempts," attempts")

number= random.randint(1, max_value)
bot_input=random.randint(1,max_value)

for I in range(remaining_attempts):
	remaining_attempts=remaining_attempts-1
	try:
			
		guess = int(input('\nEnter your guess '))
		if bot_input==number:
			bot_state=True
		if guess > number:
			print('Too high')
		if guess < number:
			print('Too low')
		if guess==number:
			player_state=True
			bonus=float(remaining_attempts+10)
			remaining_attempts=remaining_attempts+bonus			
			print("\n Congratulations,You got ",bonus," bonus points")			
			break
			
	except ValueError:
		print("\nInvalid Input\n")

	
		remaining_attempts=remaining_attempts+1
print("\nGame over")
if remaining_attempts==0:
	print("You loose the game\n")
