// a function to transform a '/' separated string into an object of sorts

const strEditor = (strList) => {
  //split string into array
  let result = []
  for (let str of strList) {
    const strArr = str.split('/')
    
    const strObject = {}
    //populate strObject
    strObject.name = strArr[0] || "not known"
    strObject['age'] = strArr[1] || "not known"
    strObject.level = strArr[2] || "not known"
    
    result.push(strObject)
  }
  
  return result
}

console.log(strEditor(['marader/100/100', 'T\'challa/50', 'maestro/1000/infinity']))
