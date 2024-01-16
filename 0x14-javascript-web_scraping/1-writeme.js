#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const file_content = process.argv[3];

fs.writeFile(filepath, file_content, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
