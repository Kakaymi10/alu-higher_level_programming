#!/usr/bin/node
const n = process.argv;
function secondBiggest () {
  if (n.length > 3) {
    const c = (n.slice(2)).sort();
    const b = c.slice(-2);
    console.log(parseInt(b));
  } else {
    console.log(0);
  }
}
secondBiggest.call();
