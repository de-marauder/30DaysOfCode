import numpy as np

def isMagicSquare(magicSquare):
  if (type(magicSquare) != list and type(magicSquare[0]) != list):
    print("Array should be 2D")
    return 
    
  magicSquare = np.array(magicSquare)
  magicSquareFlat = magicSquare.flatten()

  for i in range(9):
    if not ((i+1) in magicSquareFlat):
      print(f"number {i+1} is not in the square")
      return

  rowSum = np.sum(magicSquare, axis=1)
  rowsum = int(np.sum(rowSum)/3)
  
  columnSum = np.sum(magicSquare, axis=0)
  columnsum = int(np.sum(columnSum)/3)
  
  diagonalSum = np.trace(magicSquare)
  diagonalSum1 = np.trace(np.rot90(magicSquare))
  # print(rowsum, columnsum, diagonalSum, diagonalSum1)
  if (rowsum == columnsum and 
     rowsum == diagonalSum and
     rowsum == diagonalSum1):
       print("Your array is a magic array")
       return True
  else: 
    print("Your array is not a magic array")
    return False

isMagicSquare([[4,9,2], [3,5,7], [8,1,6]])
