#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      count++;
    }
  }
  return count;
};