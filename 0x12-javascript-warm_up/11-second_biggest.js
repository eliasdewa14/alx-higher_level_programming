#!/usr/bin/node

if (process.argv.length > 2) {
  const sort_list = process.argv.sort();
  const reverse_list = sort_list.reverse();
  console.log(reverse_list[1]);
} else {
  console.log(0);
}