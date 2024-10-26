# src/api/api_endpoints.py

from flask import Flask, request, jsonify
from rule_service import RuleService

app = Flask(__name__)
service = RuleService()

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json.get('rule_string')
    rule_ast = service.create_rule(rule_string)
    return jsonify({"rule": rule_ast}), 201

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rules = request.json.get('rules')
    combined_ast = service.combine_rules(rules)
    return jsonify({"combined_rule": combined_ast}), 200

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    rule_ast = request.json.get('rule_ast')
    data = request.json.get('data')
    result = service.evaluate_rule(rule_ast, data)
    return jsonify({"eligible": result}), 200

