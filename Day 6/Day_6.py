# Man in the well function.
# returns the number of days required for a man to xit a well of a certain depth
def well(n):
  dist = 0
  days = 0
  while (dist < n):
    dist = dist + 8
    days += 1
    if dist > n:
      break
    dist = dist - 3

    
  return days, dist

print(well(17))
