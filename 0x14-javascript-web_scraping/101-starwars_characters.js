#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    let charactersProcessed = 0;
    characterUrls.forEach(function (characterUrl, index) {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);

          charactersProcessed++;
          if (charactersProcessed === characterUrls.length) {
            // All characters have been processed
            process.exit(0);
          }
        } else {
          console.error('Error requesting character:', error);
        }
      });
    });
  } else {
    console.error('Error requesting the Star Wars API:', error);
  }
});
