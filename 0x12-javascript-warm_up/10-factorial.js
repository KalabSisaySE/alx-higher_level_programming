#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (num) {
  if (num.toString() === 'NaN') {
    return 1;
  } else {
    if (num === 1) {
      return 1;
    } else {
      while (num > 1) {
        return num * factorial(num - 1);
      }
    }
  }
}

console.log(factorial(num));
