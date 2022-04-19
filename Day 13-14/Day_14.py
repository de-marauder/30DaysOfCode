def guess():
  import random
  
  answer = random.randrange(1, 50, 1)
  
  # print(answer)
  for i in range(5):
    number = input("Guess a number between 1 and 50: ")
    if int(number) < int(answer):
      print(f"wrong. the answer is greater than {number}")
    elif int(number) > int(answer):
      print(f"wrong. the answer is less than {number}")
    else:
      print(f"Correct! You got the right answer in {i+1} tries")
      break
      
  return

guess()
