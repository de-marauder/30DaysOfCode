# Function to calculate the Greatest common divisor using Euclid's method.
def HCF(num1, num2):

  # input check
  if (type(num1) != int or type(num2) != int):
    return "Both function inputs must be integers"

  # assign highest and lowest numbers
  higher_num = num1 if (num1 > num2) else num2
  lower_num = num2 if (num1 > num2) else num1

  # Guard to end function if one number is a factor of the other
  if (higher_num % lower_num == 0):
    rem = lower_num

  # Euclid's method
  while (higher_num % lower_num != 0):
    rem = higher_num % lower_num
    higher_num = lower_num
    lower_num = rem
  
  return rem

print(HCF(40, 16))
