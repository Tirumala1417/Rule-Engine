# tests/test_api_endpoints.py

import unittest
import json
from src.api.api_endpoints import app

class TestAPIEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_rule_endpoint(self):
        rule_data = {"rule_string": "(age > 30 AND department == 'Marketing')"}
        response = self.app.post('/create_rule', data=json.dumps(rule_data), content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn("rule", data)

    def test_combine_rules_endpoint(self):
        rules_data = {"rules": ["age > 30", "department == 'Marketing'"]}
        response = self.app.post('/combine_rules', data=json.dumps(rules_data), content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("combined_rule", data)

    def test_evaluate_rule_endpoint(self):
        rule_ast = {
            "node_type": "operator",
            "value": "AND",
            "left": {"node_type": "operand", "value": "age > 30"},
            "right": {"node_type": "operand", "value": "department == 'Marketing'"}
        }
        eval_data = {
            "rule_ast": rule_ast,
            "data": {"age": 35, "department": "Marketing"}
        }
        response = self.app.post('/evaluate_rule', data=json.dumps(eval_data), content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data["eligible"])

if __name__ == "__main__":
    unittest.main()
