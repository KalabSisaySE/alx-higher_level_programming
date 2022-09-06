#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const x in dict) {
  const value = dict[x];
  if (!Object.keys(newDict).includes(value)) {
    const arr = [];
    for (const x in dict) {
      if (dict[x] === value) {
        arr.push(x);
      }
      newDict[value] = arr;
    }
  }
}

console.log(newDict);
