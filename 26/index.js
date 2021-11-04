function findOne(arr) {
  let map = new Map();
  let ans = [];

  for (let value of arr) {
    if (map.has(value)) {
      map.set(value, map.get(value) + 1);
    } else {
      map.set(value, 1);
    }
  }

  map.forEach((value, key) => {
    if (value === 1) {
      ans.push(key);
    }
  });

  return ans;
}

/**
 *  for a O(N) space (1) using XOR of each element in the array since our input has 2 values and 1 value
 *  7 ^ (3 ^ 3)
 *  7 ^ (0)          since a number XOR itself is zero
 *
 *  since we have two elements we do the pass once and XOR
 *  take this XOR finds a bit that is 1, then we sum each element that has this bit 1
 *  this sum is the first xor then we take the original and xor it against the new sum to get the other answer
 *
 * in short
 *
 * r = a ^ b  -------> we first calculate (r)
 * (a)        -------> then a or b is calculated
 *  b = a ^ r -------> then we can get the other answer
 */

function XORfindOne(arr) {
  const ans = [];
  let mask = -1;

  let xorSum = arr[0];
  let maskxor = 0;

  for (let e of arr) {
    xorSum = xorSum ^ e;
  }

  for (let b = 0; b < 32; b++) {
    mask = 1 << b % 32;

    if ((xorSum & mask) != 0) {
      break;
    }
  }

  if (mask == -1) {
    return ans;
  }

  for (let e of arr) {
    if ((e & mask) != 0) {
      maskxor = maskxor ^ e;
    }
  }

  ans.push(maskxor);
  ans.push(maskxor ^ xorSum);
  return ans;
}

function test1() {
  const arr = [2, 4, 6, 8, 10, 2, 6, 10];
  const ans = [4, 8];

  const response = findOne(arr);

  const testANS = JSON.stringify(ans) === JSON.stringify(response);

  console.log(
    `\ntesting\narr: [${arr}]\nans:[${ans}]\nresponse: [${response}]\npassed: ${testANS}`
  );
}

function test2() {
  const arr = [2, 2, 4, 8, 8, 10, 2, 6, 10, 6];
  const ans = [4];

  const response = findOne(arr);

  const testANS = JSON.stringify(ans) === JSON.stringify(response);

  console.log(
    `\ntesting\narr: [${arr}]\nans:[${ans}]\nresponse: [${response}]\npassed: ${testANS}`
  );
}

function test3() {
  const arr = [2, 2, 4, 8, 10, 2, 6, 10, 6];
  const ans = [4, 8];

  const response = XORfindOne(arr);

  const testANS = JSON.stringify(ans) === JSON.stringify(response);

  console.log(
    `\ntesting\narr: [${arr}]\nans:[${ans}]\nresponse: [${response}]\npassed: ${testANS}`
  );
}

test3();
