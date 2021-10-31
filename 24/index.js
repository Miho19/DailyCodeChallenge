class Node {
  constructor(item) {
    this.data = item;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  insert(item) {
    let newNode = new Node(item);
    if (this.root == null) {
      this.root = newNode;
      return;
    }

    return this._insert(this.root, newNode);
  }

  _insert(currNode, node) {
    if (currNode.data > node.data) {
      if (currNode.left === null) {
        currNode.left = node;
        return;
      }
      return this._insert(currNode.left, node);
    } else {
      if (currNode.right === null) {
        currNode.right = node;
        return;
      }
      return this._insert(currNode.right, node);
    }
  }

  sumtoK(pair, elements, currNode, k) {
    if (currNode === null) {
      return false;
    }

    if (this.sumtoK(pair, elements, currNode.left, k)) {
      return true;
    }

    if (elements.has(k - currNode.data)) {
      pair.push(currNode.data, k - currNode.data);
      return true;
    }

    !elements.has(currNode.data) && elements.add(currNode.data);

    if (this.sumtoK(pair, elements, currNode.right, k)) {
      return true;
    }
  }
}

function setUp(arr, k) {
  tree = new BST();
  let pair = [];
  let elements = new Set();

  for (let e of arr) {
    tree.insert(e);
  }

  return tree.sumtoK(pair, elements, tree.root, k) ? pair : [false, false];
}

const [a, b] = setUp([10, 5, 15, 11, 15], 20);

console.log(`pair: ${a} ${b}`);
