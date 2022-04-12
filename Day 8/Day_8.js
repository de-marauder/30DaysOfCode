// Function to check if a string is a palindrom.
// Returns true or false
const checkPalindrome = (text) => {
  let palCheck = 0
  for (let i=0; i<=text.length-1; i++){
    if (text.split('')[i] === text.split('').reverse()[i]) {
      palCheck += 1
    }
  }

  return palCheck === text.length
}

// Function to loop through list and find palindromes
const checkListForPalindrome = (arr) => {
  let boolArr = []
  
  for (let i=0; i<=arr.length-1; i++) {
      boolArr[i] = checkPalindrome(arr[i])
  }
  
  return boolArr
}

console.log(checkListForPalindrome(['racecar','abcd','babk','ala','madam', 'carac']))

