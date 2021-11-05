from functions import Funcs as functions


class Executor:
    def __init__(self, tokens, funcs) -> None:
        self.tokens = tokens
        self.funcs = funcs

    def execute(self):
        for token in self.tokens:
            keyword_identifier = token[0]
            params = " ".join([x for x in token[1:-1][0]])
            self.get_keyword_function(keyword_identifier, params)

    def get_keyword_function(self, keyword_identifier, params):
        for key, value in functions().functions.items():
            if keyword_identifier == key:
                for ls in value:
                    to_perform = ls[0]
                    if to_perform == "/builtins":
                        to_perform = value[1][0]
                        to_perform(params)
                    elif to_perform == "stop":
                        break

                    elif to_perform != "/builtins":
                        keyword_identifier = to_perform
                        self.get_keyword_function(keyword_identifier, params)
