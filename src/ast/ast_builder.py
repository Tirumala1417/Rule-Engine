# src/ast/ast_builder.py

from ast_node import Node
from utils.parser import parse_rule_string

def create_rule(rule_string: str) -> Node:
    # Parse rule_string into components and build an AST
    tokens = parse_rule_string(rule_string)
    return build_ast(tokens)

def combine_rules(rules: list[Node]) -> Node:
    # Combine multiple ASTs with OR operator for simplicity
    root = Node("operator", "OR")
    root.left = rules[0]
    for rule in rules[1:]:
        new_root = Node("operator", "OR", left=root, right=rule)
        root = new_root
    return root

def build_ast(tokens: list[str]) -> Node:
    # Construct AST from tokens, assuming simplified rule structure
    pass  # Parse tokens and create Nodes accordingly
