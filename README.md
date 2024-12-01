# Binary Search Tree Implementation

This project implements a Binary Search Tree (BST) data structure in Python with testing and performance evaluation.

## Features

- Complete BST implementation with the following operations:
  - Add: Insert new nodes
  - Remove: Delete nodes (handling all cases)
  - Maximum: Find maximum value
  - InorderTraverse: Print tree contents in-order
  - Find: Search for specific values

- Testing suite
- Performance evaluation for different tree sizes

## Setup and Running

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/bst-implementation.git
cd bst-implementation
```

2. (Optional) Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Run the program:
```bash
python bst.py
```

## Tests

The program includes tests for:
- Empty tree operations
- Duplicate insertions
- Node removal (leaf, one child, two children)
- BST property verification

## Performance Testing

Evaluates BST performance with:
- 100 nodes
- 1,000 nodes
- 10,000 nodes
- 100,000 nodes
