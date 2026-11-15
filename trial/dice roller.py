#in order to make dices, we need to learn to make lines, circle to draw the actual dice
import random
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518" )
#the above output is ● ┌ ─ ┐ │ └ ┘  using this we can literally make a dice
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
dice_art = {1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
             2:("┌─────────┐",
                "│  ●      │",
                "│         │",
                "│       ● │",
                "└─────────┘"),
             3:("┌─────────┐",
                "│ ●       │",
                "│    ●    │",
                "│       ● │",
                "└─────────┘"),
             4:("┌─────────┐",
                "│ ●     ● │",
                "│         │",
                "│ ●     ● │",
                "└─────────┘"),
             5:("┌─────────┐",
                "│ ●     ● │",
                "│    ●    │",
                "│ ●     ● │",
                "└─────────┘"),
             6:("┌─────────┐",
                "│ ●     ● │",
                "│ ●     ● │",
                "│ ●     ● │",
                "└─────────┘")}
dice = []
total = 0

num_of_dice = int(input("How many dice ? :"))
for die in range(num_of_dice):
   dice.append(random.randint(1,6))
for die in range(num_of_dice):
   for x in dice_art.get(dice[die]):
      print(x)
for die in range(num_of_dice):
   total += dice[die]
print(total)

    
