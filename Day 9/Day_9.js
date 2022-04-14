// A function to generate a 2D array that maps pascal's triangle
const PascalsTriangle = (num) => {
  let result = []
  for (let i=1; i<=num; i++) {
    let row = []
    for (let j=1; j<=i; j++) {
      row[0] = 1 // First term of each array
      if ((i > 2) && (result.length > 0) && row.length < i) {
        // console.log(i, j, result[i-2])
        for (let n=1; n<=(i-2); n++) {
          // fill in the middle parts of each array
          row.push(result[i-2][n-1] + result[i-2][n])
        }
      }
      if (i>1) {row[i-1] = 1} //last term of each array
    }
    result.push(row)
  }

  return result
}

console.log(PascalsTriangle(10))
