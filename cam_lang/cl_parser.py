class Parser:
    def __init__(self, content) -> None:
        self.content = content
        self.tokens = []

    def make_tokens(self):
        line_by_line = self.content.split("\n")
        line_num = 0
        for line in line_by_line:
            line_num += 1
            line_content = line.split(" ")  # Removes Spaces
            line_content = [x for x in line_content if x != ""]
            line_content = [x.replace(",", "") for x in line_content]

            if line_content == []:
                continue  # Skips empty lines
            keyword_identifier = line_content[0]
            self.tokens.append(
                [keyword_identifier, line_content[1:], line_num])
