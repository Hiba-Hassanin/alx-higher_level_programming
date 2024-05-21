#!/usr/bin/node

// Import required modules
const fs = require('fs');
const request = require('request');

// Get the source URL and destination file path from command line arguments
const sourceURL = process.argv[2];
const destinationFilePath = process.argv[3];

// Make a request to the source URL and pipe the response to a writable stream
request(sourceURL)
  .pipe(fs.createWriteStream(destinationFilePath));
