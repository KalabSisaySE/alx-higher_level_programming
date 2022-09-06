#!/usr/bin/node

const list = require('./100-data').list;

const map1 = new Map();

const newList = list.map(double);

function double(value) {
  return value * 2;
}

console.log(list);
console.log(newList);
