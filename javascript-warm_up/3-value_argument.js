#!/usr/bin/node
function firstArgument() {
  if ((process.argv).length === 2) {
    console.log('No argument');
  } else {
    console.log(process.argv[2]);
  }
}
firstArgument();
