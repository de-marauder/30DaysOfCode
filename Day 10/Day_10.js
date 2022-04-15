// A function that sorts a list of numbers in ascending order
const sort = (prevArr) => {
  let currArr = [];
  let active = true;
  
  let counter = 0
  while (active !== false) {
    let storedArrBool = 0;
    for (let i=0; i<=prevArr.length-2; i++) {
      if ((prevArr[i] < prevArr[i+1])){
        prevArr[i] = prevArr[i]
      }
      else if ((prevArr[i] > prevArr[i+1])) {
        const el = prevArr[i]
        prevArr[i] = prevArr[i+1]
        prevArr[i+1] = el
      }
      if (currArr[i] === prevArr[i]) {
        storedArrBool += 1
      }
    }
    currArr = [...prevArr]

    if (storedArrBool === prevArr.length-1) {
      active=false
    }
    counter += 1; 
  }
  return prevArr;
}

const mergeArray = (arr1, arr2) => {
  let result = []
  const maxLength = Math.max(arr1.length, arr2.length)
  
  for (let i=0; i<=maxLength; i++) {
    if (typeof arr1[i] !== "number" && typeof arr1[i] !== undefined) {
      return `List has a non number type ${arr1[i]}`
    }
    if (typeof arr2[i] !== "number" && typeof arr2[i] !== undefined) {
      return `List has a non number type ${arr2[i]}`
    }
    arr1[i] !== undefined ? result.push(arr1[i]) : null
    arr2[i] !== undefined ? result.push(arr2[i]) : null
  }
  return sort(result)
}

console.log(mergeArray([0, 9, ,4,2],[2,2,1,2,1,0]))
