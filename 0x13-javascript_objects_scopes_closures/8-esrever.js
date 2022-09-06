#!/usr/bin/node

exports.esrever = function (list) {
  let j = (list.length - 1);

  for (let i = 0; i <= j; i++) {
    if (i !== j) {
      const temp = list[i];
      list[i] = list[j];
      list[j] = temp;
    }
    j--;
  }

  return list;
};
