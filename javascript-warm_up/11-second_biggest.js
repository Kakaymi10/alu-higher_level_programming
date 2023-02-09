#!/usr/bin/node
function findSecondLargestElem () {
  const arr = process.argv;
  if (arr.length > 3) {
    arr.slice(2);
    let first = -1; let second = -1;

    for (let i = 0; i <= arr.length - 1; i++) {
      if (arr[i] > first) {
        second = first;
        first = arr[i];
      } else if (arr[i] > second && arr[i] !== first) {
        second = arr[i];
      }
    }
    console.log(second);
  } else {
    console.log(0);
  }
}
findSecondLargestElem();
