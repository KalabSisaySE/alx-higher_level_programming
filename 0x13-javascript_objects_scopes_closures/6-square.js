#!/usr/bin/node

const FirstSquare = require('./5-square');

module.exports = class Square extends FirstSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let str = '';
        for (let j = 0; j < this.width; j++) {
          str = str.concat(c);
        }
        console.log(str);
      }
    } else {
      super.print();
    }
  }
};
