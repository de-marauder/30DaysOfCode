#A function to calculate the hex value of a decimal number (integer)

def dec_to_hex(num):
  #exit function if argument is not an integer
  if type(num) != int:
    print(type(num))
    print('please pass a number (integer) to this function')
    return

  hex_value = []
  
  #Calculation loop
  while (num != 0):
    #hex rules
    if (num%16 == 10):
      hex_digit = 'a'
    elif (num%16 == 11):
      hex_digit = 'b'
    elif (num%16 == 12):
      hex_digit = 'c'
    elif (num%16 == 13):
      hex_digit = 'd'
    elif (num%16 == 14):
      hex_digit = 'e'
    elif (num%16 == 15):
      hex_digit = 'f'
    else: hex_digit = num%16
    
    # add the result of hex_digit to hex_value list
    hex_value.append(hex_digit)
    #update the num variable
    num = int(num/16)

  #return edited hex_value by converting the list to a string, reversing it and concatenating the 0x prefix.
  return "0x" + ''.join(str(e) for e in hex_value[::-1])

print(dec_to_hex(9725547256389251))
