#!/usr/bin/node
exports.nbOccurences = function (list = [], searchElement = int) {
  let counter = 0;
  for (i of list) {
    if (i === searchElement) {
      counter++;
    }
  }
  return counter;
};
