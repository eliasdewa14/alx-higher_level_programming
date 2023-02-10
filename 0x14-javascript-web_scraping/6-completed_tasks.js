#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (!error) {
    const completedTask = {};
    body.forEach((todo) => {
      if (todo.completed && completedTask[todo.userId] === undefined) {
        completedTask[todo.userId] = 1;
      } else if (todo.completed) {
        completedTask[todo.userId] += 1;
      }
    });
    console.log(completedTask);
  }
});