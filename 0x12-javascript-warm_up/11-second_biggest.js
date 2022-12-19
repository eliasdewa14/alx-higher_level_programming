#!/usr/bin/node

if (process.argv.length > 3) {
  const sorted = process.argv.sort();
  const reverse = sorted.reverse();
  console.log(reverse[1]);
} else {
  console.log(0);
}
