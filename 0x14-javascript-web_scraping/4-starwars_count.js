#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

function getFilmsCount(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const filmsData = JSON.parse(body);
        const moviesWithWedgeAntilles = filmsData.results.filter(film =>
          film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
        );
        resolve(moviesWithWedgeAntilles.length);
      }
    });
  });
}

function getAllFilmsCount(apiUrl) {
  return new Promise((resolve, reject) => {
    let count = 0;

    function getPageCount(url) {
      request.get(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const filmsData = JSON.parse(body);
          count += filmsData.results.length;
          if (filmsData.next) {
            getPageCount(filmsData.next);
          } else {
            resolve(count);
          }
        }
      });
    }

    getPageCount(apiUrl);
  });
}

getAllFilmsCount(apiUrl)
  .then(count => console.log(count))
  .catch(error => console.error(error));
