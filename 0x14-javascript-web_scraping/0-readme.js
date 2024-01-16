#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
fs.readFile(filepath, 'utf8', function (err, line) {
  if (err) {
    console.log(err);
  } else {
    console.log(line);
  }
});
