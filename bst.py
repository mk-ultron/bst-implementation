import random
import time
from typing import Optional, Any

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def add(self, data: int) -> bool:
        """Insert a new node with the given data into the BST.
        Returns True if successful, False if duplicate found."""
        if self.root is None:
            self.root = Node(data)
            return True
            
        return self._add_recursive(self.root, data)
    
    def _add_recursive(self, node: Node, data: int) -> bool:
        if data == node.data:
            return False  # Duplicate found
        
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                return True
            return self._add_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
                return True
            return self._add_recursive(node.right, data)
    
    def remove(self, data: int) -> bool:
        """Remove the node with the given data from the BST.
        Returns True if successful, False if not found."""
        if self.root is None:
            return False
            
        # Handle root removal specially
        if self.root.data == data:
            if self.root.left is None:
                self.root = self.root.right
            elif self.root.right is None:
                self.root = self.root.left
            else:
                # Find smallest value in right subtree
                parent = self.root
                successor = self.root.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                if parent != self.root:
                    parent.left = successor.right
                    successor.right = self.root.right
                successor.left = self.root.left
                self.root = successor
            return True
            
        return self._remove_recursive(self.root, data)
    
    def _remove_recursive(self, node: Node, data: int) -> bool:
        if node is None:
            return False
            
        # Find the node to remove and its parent
        parent = None
        current = node
        while current and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
                
        if current is None:  # Node not found
            return False
            
        # Case 1: Node to remove has no children
        if current.left is None and current.right is None:
            if data < parent.data:
                parent.left = None
            else:
                parent.right = None
                
        # Case 2: Node to remove has one child
        elif current.left is None:
            if data < parent.data:
                parent.left = current.right
            else:
                parent.right = current.right
        elif current.right is None:
            if data < parent.data:
                parent.left = current.left
            else:
                parent.right = current.left
                
        # Case 3: Node to remove has two children
        else:
            # Find smallest value in right subtree
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
                
            if successor_parent != current:
                successor_parent.left = successor.right
                successor.right = current.right
                
            successor.left = current.left
            if data < parent.data:
                parent.left = successor
            else:
                parent.right = successor
                
        return True
    
    def maximum(self) -> Optional[int]:
        """Returns the maximum value in the BST."""
        if self.root is None:
            return None
            
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    def inorder_traverse(self) -> None:
        """Print the BST contents in-order."""
        self._inorder_recursive(self.root)
        print()  # Add newline at end
    
    def _inorder_recursive(self, node: Node) -> None:
        if node:
            self._inorder_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_recursive(node.right)
    
    def find(self, data: int) -> bool:
        """Returns True if data is found in the BST, False otherwise."""
        current = self.root
        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

def test_bst():
    """Run comprehensive tests on the BST implementation."""
    bst = BinarySearchTree()
    
    # Test 1: Remove from empty tree
    print("Test 1: Remove from empty tree")
    assert not bst.remove(5), "Should return False when removing from empty tree"
    
    # Test 2: Insert and find
    print("\nTest 2: Insert and find")
    assert bst.add(10), "Should successfully add 10"
    assert bst.find(10), "Should find 10"
    assert not bst.find(20), "Should not find 20"
    
    # Test 3: Duplicate insertion
    print("\nTest 3: Duplicate insertion")
    assert not bst.add(10), "Should not add duplicate"
    
    # Test 4: Remove leaf node
    print("\nTest 4: Remove leaf node")
    bst.add(5)
    bst.add(15)
    assert bst.remove(5), "Should remove leaf node 5"
    bst.inorder_traverse()
    
    # Test 5: Remove node with one child
    print("\nTest 5: Remove node with one child")
    bst.add(20)
    assert bst.remove(15), "Should remove node with one child"
    bst.inorder_traverse()
    
    # Test 6: Remove node with two children
    print("\nTest 6: Remove node with two children")
    bst.add(5)
    bst.add(15)
    assert bst.remove(10), "Should remove root node with two children"
    bst.inorder_traverse()
    
    print("\nAll tests passed!")

def performance_test():
    """Test BST performance with different numbers of nodes."""
    sizes = [100, 1000, 10000, 100000]
    
    for size in sizes:
        bst = BinarySearchTree()
        numbers = random.sample(range(1, size * 2), size)  # Ensure unique numbers
        
        start_time = time.time()
        for num in numbers:
            bst.add(num)
        end_time = time.time()
        
        print(f"\nTime to add {size} nodes: {end_time - start_time:.4f} seconds")
        print(f"Maximum value: {bst.maximum()}")

if __name__ == "__main__":
    # Run tests
    print("Running BST tests...")
    test_bst()
    
    # Run performance evaluation
    print("\nRunning performance tests...")
    performance_test()