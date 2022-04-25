 # A function to generate a 2D array that maps pascal's triangle
def PascalsTriangle(num):
  result = []

  for i in range(num):
    row = []
    row.insert(0, 1) # insert first digit
    for n in range(i-1):
      # insert middle digits
      row.insert(i-1, result[i-1][n] + result[i-1][n+1])  
    if (i>0):
      row.insert(len(row), 1) # insert last digit
    
    result.append(row)
    print(f"row {i+1} => {row}")
  return result


PascalsTriangle(10)
