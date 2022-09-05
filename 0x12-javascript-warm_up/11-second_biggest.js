#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const arr = [];
  // append all the args to a list
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(Number(process.argv[i]));
  }
  arr.sort(function (a, b) {
    return b - a;
  });
  // print the second largest
  console.log(arr[1]);
}
