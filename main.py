import random
HANGMANPICS = ['''
 +---+
 |   |
     |
     |
     |
     |
========''','''
 +---+
 |   |
 O   |
     |
     |
     |
========''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
========''','''
 +---+
 |   |
 O   |
 |\  |
     |
     |
========''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
========''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
========''','''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========''']

words = {'animals':'ant baboon badger bat bee beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
'Fruits':'apple apricot avocado banana boysenberries blueberries cherry cantaloupe clementine cucumber dates dewberry elderberry eggfruit entawak fig farkleberry grapefruit grapes gooseberry guava hackberry imbe jackfruit jambolan kiwi kumquat lime lemon longan lychee loquat mango mulberry melon nectarine olive oranges papaya persimmon peach pomegranate pineapple quince rambutan raspberry strawberry tomato tangerine tamarind ugni watermelon wolfberry xigua yangmei zuchinni'.split()}


def getRandomWord(wordDict):
  wordKey = random.choice(list(wordDict.keys()))
  wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
  return wordDict[wordKey][wordIndex], wordKey

def displayBoard(HANGMANPICS, missedletters, correctletters, secretword):
  print(HANGMANPICS[len(missedletters)])
  print()
  
  print('Missed letters:', end=' ')
  for letter in missedletters:
    print(letter, end=' ')
  print()

  blanks = '_' * len(secretword)

  for i in range (len(secretword)):
    if secretword[i] in correctletters:
      blanks = blanks[:i] + secretword[i] + blanks[i+1:]

  for letter in blanks:
    print(letter, end=' ')
  print()

def getguess(alreadyguessed):
  while True:
      print('guess a lettter.')
      guess = input()
      guess = guess.lower()
      if len(guess) != 1:
        print('please enter a SINGLE letter.')
      elif guess in alreadyguessed:
        print('You have already guessed that letter. Choose again')
      elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('Please enter a LETTER.')
      else:
        return guess

def playagain():
  print('Do you want to play again? (yes or no)')
  return input().lower().startswith('y')

print('H A N G M A N')
missedletters = ''
correctletters = ''
secretword, secretKey = getRandomWord(words)
gameisdone = False

while True:
  print('The secret word is in the set: ' + secretKey)
  displayBoard(HANGMANPICS, missedletters, correctletters, secretword)

  guess = getguess(missedletters + correctletters)

  if guess in secretword:
    correctletters = correctletters + guess

    foundallletters = True
    for i in range(len(secretword)):
      if secretword[i] not in correctletters:
        foundallletters = False
        break
    if foundallletters:
      print('Yes! The secret word is "' + secretword + '"! You have won!')
      gameisdone = True

  else:
    missedletters = missedletters + guess

    if len(missedletters) == len(HANGMANPICS) - 1:
      displayBoard(HANGMANPICS, missedletters, correctletters, secretword)
      print('You have run out of guesses!\nAfter ' + str(len(missedletters)) + ' missed guesses and ' + str(len(correctletters)) + ' correct guesses, the word was "' + secretword + '"')
      gameisdone = True


  if gameisdone:
    if playagain():
      missedletters = ''
      correctletters = ''
      gameisdone = False
      secretword, secretKey = getRandomWord(words)
    else:
      break
