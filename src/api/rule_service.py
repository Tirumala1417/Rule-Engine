# src/api/rule_service.py

from ast.ast_builder import create_rule, combine_rules, build_ast

class RuleService:
    def create_rule(self, rule_string):
        return create_rule(rule_string)

    def combine_rules(self, rules):
        rule_asts = [build_ast(rule) for rule in rules]
        return combine_rules(rule_asts)

    def evaluate_rule(self, rule_ast, data):
        return self._evaluate_ast(rule_ast, data)

    def _evaluate_ast(self, node, data):
        if node.node_type == "operand":
            # Evaluate operand using eval (or a safer custom method)
            return eval(node.value, {}, data)
        elif node.node_type == "operator":
            if node.value == "AND":
                return self._evaluate_ast(node.left, data) and self._evaluate_ast(node.right, data)
            elif node.value == "OR":
                return self._evaluate_ast(node.left, data) or self._evaluate_ast(node.right, data)
        return False
