# Acronym finder
def acronyms(string_input):
  if type(string_input) != str:
    print("Function only accepts strings")
    return
    
  strList = string_input.split(' ')
  acronymsList = []
  
  for string in strList:
    letterList = [letter for letter in string]
    letter_count = 0

    for letter in letterList:
      # Check for uppercase, periods and/or exclamations
      if (letter.isupper() and (letter != '.' or letter != '!')):
        letter_count += 1
    # If period or exclamation present at the end of string ignore it and append acronyms.
    if (letter == '.' or letter == '!'):
      if letter_count == (len(string)-1):
        acronymsList.append(string[:len(string)-1])
    elif len(string) > 1:
      if letter_count == (len(string)):
        acronymsList.append(string)
      
      
  return acronymsList

print(acronyms("I need to get this done ASAP."))
print('\n\n')
print(acronyms("LOOOL. I thought you were at KFC"))
print('\n\n')
print(acronyms("SMH. The NPF is really a joke!"))
# acronyms(12)
