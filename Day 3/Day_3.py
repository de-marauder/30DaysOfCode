#A function to identify palindromic numbers below a certain input value.
def palindrome_finder(num):
  result = []
  counter = 0
  while counter < num:
    #convert number to string and split in into an array
    numArr = list(str(counter))
    #compare num array with a reversed copy and add the counter to the result array if they are equal
    if numArr == numArr[::-1]:
      result.append(counter)
    counter +=1 
    
  return result, len(result), num


result, amount, max_num = palindrome_finder(500)

print(f"The palindromic numbers below {max_num} are {amount} in number. \nThey include:\n {result}")
