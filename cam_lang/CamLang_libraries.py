from typing import Type
from errors import Error
import variables

class BuiltIn(variables.Variables):
    def __init__(self) -> None:
        super().__init__()
        self.DIGITS = '0123456789'
        self.CHARS = 'abcdefghijklmnopqrstuvwxyz'
        self.VAR_ALLOWED_SPECIAL_CHARS = '_-'
        self.keywords = "output op variable add"

    def output(self, to_output):
        "Checks whether 'output' keyword outputs string, int, var ect"
        # Printing all assigned variables
        if to_output == "variables":
            to_print = "Stored Variables:"
            for k, v in self.variables.items():
                to_print += f"\n  {k} : {v}"
            self.output_val(to_print)
            return

        # If escape character
        if to_output == "\".n\"":
            self.output_val("")
            return

        # Printing strings
        if to_output.startswith('"'):
            first_quotes = to_output.find('"', 0)
            second_quotes = to_output.find('"', (first_quotes + 1))
            new_content = to_output[first_quotes:second_quotes + 1]
            self.output_val(new_content)
            return

        # Printing numbers
        all_digits = True
        for x in to_output:
            if x not in self.DIGITS:
                all_digits = False
        if all_digits:
            self.output_val(to_output)
            return

        # Find Value in self.variables
        value = self.check_if_var(to_output)
        if value:
            i = 0
            for char in value:
                i += 1
                if char == "s":
                    if value[i - 1] == ".":
                        value = value[0: i] + value[i + 1:]
                        value = value[0: (i-1)] + value[i:]

            self.output_val(value)
            return
        else:
            Error(
                f"Could not find variable \"{to_output}\" to output", "CRITICAL")

    def output_val(self, to_output):
        "Outputs value to screen"
        print(to_output)

    def create_variable(self, args):
        args = [x for x in args.split()]
        key = args[0]
        val = ""
        for arg in args[2:]:
            val += arg

        # Key Checks
        if key in self.keywords:
            Error(
                f"Variable name {key} is a pre-existing keyword; Value not assigned", "CRITICAL")
            return

        if key[0] in self.DIGITS:
            Error(
                f"Variable name must not start with a number; Value not assigned", "CRITICAL")
            return

        for x in list(key):
            if x not in self.DIGITS:
                if x not in self.CHARS:
                    if x not in self.VAR_ALLOWED_SPECIAL_CHARS:
                        Error(
                            f"Variable name must not contain special characters; Value not assigned", "CRITICAL")
                        return

        # Value Checks
        if val[0] in self.CHARS:
            try:
                # if value starts with char, must be a var. Checks if its a var
                val = self.variables[val]
            except KeyError:
                Error(f"Bad value given; Value not assigned", "CRITICAL")
                return

        if val[0] == '"' and val[-1] != '"':
            Error(
                f"String value must start and end with \'\"\'; Value not assigned", "critical")
            return

        self.add_variable(key, val)

    def get_values(self, val1, val2):
        try:
            val1 = self.variables[val1]
        except KeyError:
            Error(f"Variable {val1} not found.", "Warning")
        try:
            val2 = self.variables[val2]
        except KeyError:
            Error(f"Variable {val2} not found.", "Warning")

        return val1, val2

    def subtract(self, val1, val2, ):
        val1, val2 = self.get_values(val1, val2)
        return int(val2) - int(val1)

    def add(self, values, output=True):
        """outputs total of values
           \nif output = False, returns total instead"""
        values = [x for x in values.split(" ")]
        values = [x if not self.check_if_var(x) else self.check_if_var(x) for x in values]
        total = 0
        try:
            for x in values:
                if type(x) != int and type(x) != float:
                    try:
                        _type = "int"
                        for char in x:
                            if char == ".":
                                _type = "float"
                        if _type == "int":
                            x = int(x)
                        elif _type == "float":
                            x = float(x)
                    except ValueError as e:
                        Error("Can only add numbers, not other types", "Critical")
                total += x
        except TypeError as e:
            print(e)
            Error("Can only add numbers, not other types", "Critical")
            return
        if output:
            self.output_val(total)
        else: return total

    def divide(self, val1, val2, ):
        val1, val2 = self.get_values(val1, val2, )
        if val1 and val2:
            return int(val1) / int(val2)
