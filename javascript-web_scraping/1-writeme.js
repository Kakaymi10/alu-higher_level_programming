#!/usr/bin/node
const fs = require('fs');

let file = process.argv[2];
let content = process.argv[3];

fs.writeFile(file, content, err => {
  if (err) {
    console.error(err);;
    return;
  }
});
