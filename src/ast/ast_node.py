# src/ast/ast_node.py

class Node:
    def __init__(self, node_type: str, value=None, left=None, right=None):
        """
        Initialize an AST Node.
        :param node_type: Type of node ("operator" or "operand")
        :param value: Value for operand nodes (e.g., number for comparison)
        :param left: Left child for operators
        :param right: Right child for operators
        """
        self.node_type = node_type
        self.value = value
        self.left = left
        self.right = right
