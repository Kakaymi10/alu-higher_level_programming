#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
let map1 = list.map(x => x * list.indexOf(x));
console.log(map1);
