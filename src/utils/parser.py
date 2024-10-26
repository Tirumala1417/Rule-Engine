# src/utils/parser.py

import re

def parse_rule_string(rule_string: str):
    # Simplistic rule parser (would need expansion for complex rules)
    tokens = re.findall(r"[()<>!=]+|AND|OR|[\w\d]+", rule_string)
    return tokens
