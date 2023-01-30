#!/usr/bin/node
function multiC() {
  if (parseInt(process.argv[2])) {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
     console.log('C is fun');
    }
  } else if (parseInt(process.argv[2]) <= 0) {
    pass;
  } else {
    console.log('Missing number of occurrences');
  }
}
multiC()
