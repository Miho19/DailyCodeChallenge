//https://stackoverflow.com/questions/1436438/how-do-you-set-clear-and-toggle-a-single-bit-in-javascript

class bitArray {
  constructor(size) {
    this._arr = new Uint8Array(Math.round(size / 8));
    this._size = size;
  }

  set(i, val) {
    if (i >= this._size) {
      return null;
    }

    let block_index = Math.floor(i / this._size);

    let mask = 1 << i % 8;

    val ? (this._arr[block_index] |= mask) : (this._arr[block_index] &= mask);
  }

  get(i) {
    if (i >= this._size) {
      return null;
    }

    let block_index = Math.floor(i / this._size);
    let block = this._arr[block_index];

    let mask = 1 << i % 8;

    if ((block & mask) != 0) {
      return 1;
    }

    return 0;
  }
}

function test1() {
  let size = 8;

  let arr = new bitArray(size);
  let test_arr = [0, 1, 0, 1, 1, 0, 1, 0]; // decimal 90
  arr._arr[0] = 90;

  let test_arr_2 = [];

  for (let i = 0; i < size; i++) {
    test_arr_2.push(arr.get(i));
  }

  let a = JSON.stringify(test_arr);
  let b = JSON.stringify(test_arr_2);

  console.log("Get test: expected true got: ", a === b);

  console.log("a: ", a);
  console.log("b: ", b);
}

function test2() {
  let size = 8;

  let arr = new bitArray(size);
  let test_arr = [0, 1, 0, 1, 1, 0, 1, 0]; // decimal 90
  arr._arr[0] = 90;

  let test_arr_2 = [];

  arr.set(7, 1);

  for (let i = 0; i < size; i++) {
    test_arr_2.push(arr.get(i));
  }

  let a = JSON.stringify(test_arr);
  let b = JSON.stringify(test_arr_2);

  console.log("Set 8th bit: expected false got: ", a === b);
  console.log("a: ", a);
  console.log("b: ", b);
}
test1();
test2();
