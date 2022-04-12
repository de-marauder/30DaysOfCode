WORD_LIST = [
'women',
'nikau',
'swack',
'feens',
'fyles',
'poled',
'clags',
'starn',
'bindi',
'woops',
'fanos',
'cabin',
'souct',
'trass',
'shoat',
'lefty',
'durra',
'hypes',
'junta'
]

import random

word = random.choice(WORD_LIST)

print(f'word = {word}')

#Wordle game
# 1 => letter and position are correct
# + => letter is correct but position isn't
# - => letter is not correct
def wordle ():
  active = True
  
  prompt = "Enter a five letter word: "
  counter= 0

  while active:
    guess = input(prompt).lower()

    # Guard against non 5 letter words
    if len(guess) != 5:
      print("You must enter a five letter word!")
      continue
      
    guessBool = ['', '', '', '', '']
    
    if (guess in WORD_LIST):
      active = False
      print("CONGRATULATIONS!!!\n You have guessed correctly!!")
      guessBool = '11111'
      return guessBool

    copy_word = word[:]
    copy_word_list = [e for e in copy_word]
    for i in range(5):
      
      # if not(guess[i] in copy_word):
      #   guessBool[i] = '0'
        
      try:
        id = copy_word_list.index(guess[i])
        
        if (guess[i] in copy_word):
          print('i = ', i, ' id = ', id)
          if (guess[i] == copy_word_list[i]):
            guessBool[i] = '1'
          elif (copy_word_list[id] == guess[id]):
            guessBool[i] = '0'
          else:
            guessBool[i] = '+'

            print('copy_word_list = ', copy_word_list)
            copy_word_list[id] = ''
            print('copy_word_list = ', copy_word_list)

        else:
          guessBool[i] = '0'
      
      except ValueError:
        print(f'{guess[i]} not in {copy_word_list}')
        guessBool[i] = '0'
        
      
      print('guessBool = ', guessBool)
      print('copy_word_list = ', copy_word_list)
      print('new_word = ', copy_word, '\n')

    print ('Answer = ', ''.join(guessBool), '\n')
    counter += 1
    
    if counter >= 6: active = False
      
  return guessBool

print(wordle())
