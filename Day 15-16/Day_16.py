# Function to return the roman numeral of an integer less than 5000

# Set of conditions for assigning numerals
def condition(roman, val, value):
  if (int(val) >= 1000 and int(val) < 5000):
      roman += ('M' * int(value))
  elif (int(val) >= 900 and int(val) < 1000):
    roman += 'CM'
  elif (int(val) >= 500 and int(val) < 900):
    roman += 'D' + ('C' * (int(value)-5))
  elif (int(val) >= 400 and int(val) < 500):
    roman += 'CD'
  elif (int(val) >= 100 and int(val) < 400):
    roman += ('C' *int(value))
  elif (int(val) >= 90 and int(val) < 100):
    roman += ('XC')
  elif (int(val) >= 50 and int(val) < 90):
    roman += 'L' + ('X' * (int(value)-5))
  elif (int(val) >= 40 and int(val) < 50):
    roman += 'XL'
  elif (int(val) >= 10 and int(val) < 40):
    roman += ('X' *int(value))
  elif (int(val) >= 9 and int(val) < 10):
    roman += ('IX')
  elif (int(val) >= 5 and int(val) < 9):
    roman += 'V' + ('I' * (int(value)-5))
  elif (int(val) >= 4 and int(val) < 5):
    roman += 'IV'
  elif (int(val) >= 1 and int(val) < 4):
    roman += ('I' *int(value))

  return roman
def roman(no):
  if type(no) != int:
    print("Incorrect input. \nFunction only takes integers")
    return
  if no >= 5000:
    print("Incorrect input. \nFunction only takes integers less than 5000")
    return

  num = str(no)
  numList = list(num)
  enum = [[len(numList)-int(i+1), numList[int(i)]] for i in range(len(numList))]
  # print(enum)

  roman = ''
  for index, value in enum:
    val = value+(index*'0')
    print(index, val)
    print(roman)

    roman = condition(roman, val, value)
  
  return roman

print(roman(456))

