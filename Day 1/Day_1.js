const addArray = (array) => {
  let sum = 0;
  
  // Loop through array and increment sum
  for (let i in array) {
    sum = array[i] + sum;
  }
 
  return sum
};

console.log("sum = ", addArray([1, 2, 3])); // Logs sum = 6
