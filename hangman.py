import random

animals = ["dog", "cat", "aardvark", "baboon", "camel"]
lives = 6
word = random.randint(0, len(animals)-1)

display = []
old_display = []
correct = []
for n in animals[word]:
    display.append("_")
    old_display.append("_")
    correct.append(n)

print(display)

while lives != 0:
    letter = input("please guess a letter: ").lower()
    x=0
    y=0
    for n in animals[word]:
        if letter == n:
            display[x]=letter

        x+=1

    print(display)    
    
    if display == correct:
        lives = 0
    
    if old_display == display:
        lives -= 1
        print(f"you lost a life: {lives} lives left")
    else:
        for n in animals[word]:
            if letter == n:
                old_display[y]=letter
            y+=1

        print(f"you have {lives} left")
    
    if lives == 6:
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif lives ==5:
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif lives == 4:
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif lives ==3:
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif lives == 2:
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif lives == 1 : 
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')

if display == correct:
    print("you won!!")
else:
    print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
    print(f"loser the real word was {animals[word]}")

  