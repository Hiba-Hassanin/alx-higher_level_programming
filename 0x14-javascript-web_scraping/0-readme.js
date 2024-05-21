#!/usr/bin/node

// Import the 'fs' module to work with the file system
const fs = require('fs');

// Read the file specified in the command line arguments
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    // If an error occurred while reading the file, log the error message
    console.log(err);
  } else {
    // If the file was read successfully, log its contents
    console.log(data.toString());
  }
});
