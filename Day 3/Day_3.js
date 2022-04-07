const fizzBuzz = (num) => {
  let res = [];
  for (let i = 1; i <= num; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      res.push("fizzbuzz");
    } else if (i % 5 === 0) {
      res.push("buzz");
    } else if (i % 3 === 0) {
      res.push("fizz");
    } else {
      res.push(i);
    }
  }

  return res;
};

const fizzBuzzProMax = (array) => {
  let result = [];
  for (let el of array) {
    result = [...result, fizzBuzz(el)];
  }
  return result;
};

fizzBuzzProMax([4, 10, 6]);
