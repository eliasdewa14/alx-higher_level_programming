#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const sorted = process.argv.sort();
  const reverse = sorted.reverse();
  console.log(reverse[1]);
}
