#!/usr/bin/node

const list = require('./100-data').list;

const map1 = new Map();

for (let i = 0; i < list.length; i++) {
  map1.set(i, i * list[i]);
}

const newList = [];
for (const value of map1.values()) {
  newList.push(value);
}
console.log(list);
console.log(newList);
