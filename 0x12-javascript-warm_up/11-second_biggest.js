#!/usr/bin/node

if (process.argv.length > 3) {
  const sortList = process.argv.sort();
  const reverseList = sortList.reverse();
  console.log(reverseList[1]);
} else {
  console.log(0);
}
