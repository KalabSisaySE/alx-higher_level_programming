#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (typeof num === 'number' && num.toString() !== 'NaN') {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
