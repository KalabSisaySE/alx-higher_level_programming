#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;

  for (const elem of list) {
    if (elem === searchElement) {
      occurence++;
    }
  }

  return occurence;
};
