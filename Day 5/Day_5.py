# Fibonnacci sequence generator with recursion
def fib2(n):
  
  a = 0
  b = 1
  c = a + b

  # if block to handle n = 0 to 2
  if n == 0:
    return []
  if n == 1:
    return [a]
  if n == 2:
    return [a, b]
    
  result = [a, b, c]
  counter = 2

  # defining recursive function
  def fib(b, c, counter):
    a = b
    b = c
    c = a+b
    
    counter += 1

    # recursion halting condition
    if counter == n:
      return result

    # result update
    result.append(c)
    fib(b, c, counter)
    
  fib(b, c, counter)

  return result

print(fib2(15), len(fib2(15)))


#################    OR     ##################

# Fibonnacci generator without recursion
def fib(n):
  result = [0, 1]
  while (len(result) < n):
    result.append(result[len(result) - 1] + result[len(result) - 2])

  if (n == 1):
    result = [0]
  if (n == 0):
    result = []
  return result

print(fib(15))
