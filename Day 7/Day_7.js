// A function that sorts a list of numbers in ascending order
const sortAsc = (arr) => {
  let sortedArr = [];
  let prevArr = [...arr];
  let currArr = [];
  let active = true;
  
  let counter = 0
  // let for_counter = 0
  while (active !== false) {
    let storedArrBool = 0;

    for (let i=0; i<=prevArr.length-2; i++) {

      // for_counter += 1      
      // console.log('for_counter: ', for_counter)
      if (prevArr[i] === currArr[i-1]) {
        currArr[i] = currArr[i]
      }
      else if ((prevArr[i] < prevArr[i+1])){
        currArr[i] = prevArr[i]
        // console.log('if currArr: ', currArr)
      }
      else {
        currArr[i] = prevArr[i+1]
        currArr[i+1] = prevArr[i]
        // console.log('else currArr: ', currArr)
      }


      // console.log('while counter: ', counter)
      // console.log('arr: ', arr)
      // console.log('prevArr: ', prevArr)
      // console.log('currArr: ', currArr)
      // console.log('sortedArr: ', sortedArr, '\n')

      if (currArr[i] === prevArr[i]) {
        storedArrBool += 1
      }
    }
    prevArr = currArr.slice()
    // console.log('while counter: ', counter)

    if (storedArrBool === arr.length-1) {
      // console.log('prev and curr are equal')
      sortedArr = currArr
      active=false
    }
    counter += 1; 
    if(counter >= 10){
      active=false
    }
  }
  return sortedArr;
}

console.log(sortAsc([1,3,4,5,-3, 1, -7]))
