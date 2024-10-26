# tests/test_rule_evaluation.py

import unittest
from src.rule_service import RuleService

class TestRuleEvaluation(unittest.TestCase):
    def setUp(self):
        self.service = RuleService()

    def test_rule_evaluation(self):
        rule_string = "(age > 30 AND department == 'Marketing')"
        data = {"age": 35, "department": "Marketing"}
        rule_ast = self.service.create_rule(rule_string)
        result = self.service.evaluate_rule(rule_ast, data)
        self.assertTrue(result)
