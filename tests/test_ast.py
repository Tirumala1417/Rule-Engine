# tests/test_ast.py

import unittest
from src.ast.ast_builder import create_rule, combine_rules
from src.ast.ast_node import Node

class TestASTCreation(unittest.TestCase):

    def test_create_simple_rule(self):
        rule_string = "age > 30"
        ast = create_rule(rule_string)
        self.assertEqual(ast.node_type, "operand")
        self.assertEqual(ast.value, "age > 30")

    def test_create_complex_rule(self):
        rule_string = "(age > 30 AND department == 'Marketing') OR (salary < 50000)"
        ast = create_rule(rule_string)
        
        # Check root node is an OR operator
        self.assertEqual(ast.node_type, "operator")
        self.assertEqual(ast.value, "OR")
        
        # Check left and right nodes
        self.assertEqual(ast.left.node_type, "operator")
        self.assertEqual(ast.left.value, "AND")
        self.assertEqual(ast.right.node_type, "operand")
        self.assertEqual(ast.right.value, "salary < 50000")
    
    def test_combine_rules(self):
        rule1 = create_rule("age > 30")
        rule2 = create_rule("department == 'Marketing'")
        
        combined_ast = combine_rules([rule1, rule2])
        self.assertEqual(combined_ast.node_type, "operator")
        self.assertEqual(combined_ast.value, "OR")
        self.assertEqual(combined_ast.left, rule1)
        self.assertEqual(combined_ast.right, rule2)

if __name__ == "__main__":
    unittest.main()
