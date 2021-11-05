import json
import os


class Variables:
    def __init__(self) -> None:
        self.variable_path = "variables.json"
        with open(self.variable_path) as f:
            self.variables = json.load(f)

    def add_variable(self, key, val):
        self.variables[key] = val
        with open(self.variable_path, 'w') as f:
            json.dump(self.variables, f, indent=2)

    def check_if_var(self, key_to_search: str) -> bool:
        is_in_vars = False
        for key, val in self.variables.items():
            if key_to_search == key:
                is_in_vars = True
                value = val
        return value if is_in_vars else False

    def reset_vars(self):
        variables = {}
        with open(self.variable_path, 'w') as f:
            json.dump(variables, f, indent=2)
