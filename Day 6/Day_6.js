const indexSum = (arr, target) => {
  for (const [index, value] of arr?.entries()){
    for (const [i, v] of arr.entries()){
        
        //skips loop to prevent adding an element to itself
        if (index === i){
          continue
        }
        //checks sum and compares with target. Returns indices if true.
        if (value + v === target) {
          return [index, i]
        }
    }
  }
  return [-1, -1]
}

console.log(indexSum([5,3,2,5], 10))
