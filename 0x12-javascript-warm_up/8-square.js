#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (size.toString() === 'NaN') {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let str = '';
    for (let i = 0; i < size; i++) {
      str = str.concat('X');
    }
    console.log(str);
  }
}
