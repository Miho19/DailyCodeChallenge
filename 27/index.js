class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

class LinkedList {
  constructor() {
    this.root = null;
  }

  add(value) {
    let newNode = new Node(value);
    if (this.root === null) {
      this.root = newNode;
      return;
    }

    let current = this.root;

    while (current.next != null) {
      current = current.next;
    }

    current.next = newNode;
    newNode.prev = current;
  }

  printNodes() {
    let current = this.root;

    while (current != null) {
      console.log(`${current.value} `);
      current = current.next;
    }
  }

  swapEvery2nd() {
    let head = new LinkedList();
    let current = this.root;
    while (current != null) {
      head.add(current.value);
      current = current.next;
    }
    let one = head.root;
    let two = head.root.next;
    let temp = 0;

    while (one !== null && two !== null) {
      temp = one.value;
      one.value = two.value;
      two.value = temp;

      if (two.next) {
        one = two.next;
        two = one.next;
      } else {
        break;
      }
    }

    return head;
  }
}

function test1() {
  let list = new LinkedList();

  let test = list === null;
  test
    ? console.log(`fail: new LinkedList should return an object`)
    : console.log(`pass: new LinkedList returned an object`);
}

function test2() {
  let list = new LinkedList();
  for (let i = 1; i < 5; i++) {
    list.add(i);
  }
  list.printNodes();

  let newList = list.swapEvery2nd();
  console.log("new list");
  newList.printNodes();
}

test1();
test2();
