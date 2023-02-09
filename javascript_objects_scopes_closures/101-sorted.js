#!/usr/bin/node
// Import a dictionary of occurrences by user id
// Compute a dictionary of user ids by occurrence

const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  const value = dict[key];
  if (newDict[value] === undefined) {
    newDict[value] = [];
    newDict[value].push(key);
  } else {
    newDict[value].push(key);
  }
}
console.log(newDict);

