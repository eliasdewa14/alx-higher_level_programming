#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const completedTask = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!completedTask[todo.userId]) {
        completedTask[todo.userId] = 1;
      } else {
        completedTask[todo.userId] += 1;
      }
    }
  });
  console.log(completedTask);
});