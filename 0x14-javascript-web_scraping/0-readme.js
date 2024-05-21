#!/usr/bin/node
// Import the 'fs' module to work with the file system
const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];
fs.writeFile(file, content, 'utf-8', function (err) {
  if (err) {
  // If an error occurred while reading the file, log the error message
    console.log(err);
  }
});
