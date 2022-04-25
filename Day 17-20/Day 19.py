def day_from_date():
  days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', ]
  date_str = input("Enter date with the format dd/mm/yyyy: ")
  if('/' not in date_str):
    print("Error, date format is incorrect")
    return

  try:
    day, month, year = date_str.split("/")
  except:
    print("ValueError: not enough values. Error, date format is incorrect")
    return
  try:
    d = int(day)
    m = int(month)
    y = int(year)
  except:
    print("TypeError: date format only accepts integers")
    return
  
  if len(day)!=2 or len(month)!=2:
    print("Error, date format is incorrect")
    return
  if len(year)!=4:
    print("Error, date format is incorrect")
    return


  # Check leap year if month = jan or feb
  leap = False
  if (month =='01' or month == '02'):
    print('calculating...')
    leap = y%4 == 0 and ((y%100 != 0 and y%400 != 0) or (y%100 == 0 and y%400 == 0))

  # Year code
  yr_code = (int(year[2:]) + int(int(year[2:])/4))%7
  
  # month code
  month_codes = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
  month_code = month_codes[int(month)-1]

  # Century code
  century = f"{year[:-2]}00"
  if (int(century)-1700)%400 == 0:
    century_code = 4
  if (int(century)-1800)%400 == 0:
    century_code = 2
  if (int(century)-1900)%400 == 0:
    century_code = 0
  if (int(century)-2000)%400 == 0:
    century_code = 6

  # Date code = day

  # Make calculation to get day
  leap_modifier = 1 if leap else 0
  calc_result = (yr_code + month_code + century_code + int(day) - leap_modifier) % 7
  
  result = days[calc_result]
  print(result)
  return result

day_from_date()
# "24/04/2022"
