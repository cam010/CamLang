class Error:
    def __init__(self, error, level) -> None:
        self.error = error
        level = level.upper()
        match level:
            case "WARNING":
                self.warning()
            case "ERROR":
                self.error()
            case _:
                print(f"Error - {self.error}")    
    def warning(self):
        print(f"WARNING - {self.error}")
    
    def critical(self):
        print(f"CRITICAL - {self.error}")