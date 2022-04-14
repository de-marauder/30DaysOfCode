# A function that calculates whether an integer is prime. 
# For numbers below a billion. 
# returns false for numbers greater than a million.

def isPrime(num):
  if num < 2:
    return False
  for i in range(1000000000):

    if (num != i+1) and (i+1 != 1) and (num % (i+1) == 0):
      print(i+1)
      return False
    elif ((num == i+1) and (num % (i+1) == 0)): 
      return True
   
  return "Oops! \nLoop count has exceeded number. \nTry a number less than 1000000000"

print(isPrime(15485863))
