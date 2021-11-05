from CamLang_libraries import BuiltIn as cll
class Funcs:
    def __init__(self) -> None:
        self.functions = {
            "output": [["/builtins"], [cll().output], ["stop"]],
            "op": [["output"], ["stop"]],
            "variable": [["/builtins"], [cll().create_variable], ["stop"]]
        }
       

    def add_function(self, function: str, commands: list) -> None:
        self.functions[f'{function}'] = commands

    def check_function_exists(self, function: str) -> bool:
        try:
            x = self.functions[f"{function}"]
            return True
        except KeyError:
            return False
        except Exception as e:
            print(f"INTERNAL ERROR - {e}")
            return False


