const arrEditor = (dictArr) => {
  let editedArr = []
  for (let dict of dictArr) {
    editedArr.push(dict.name + '/' + dict.age + '/' + dict.level)
  }
  return editedArr
}

console.log(arrEditor([{name: 'marauder', age: "unknown", level: "infinity"}, {name: 'zeldor', age: 1000, level: "ascending"}]))
