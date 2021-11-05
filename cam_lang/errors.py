class Error:
    """Outputs Errors in correct format\n
    Error Types (in accending order of importance):\n
    \tWARNING\n
    \tCRITICAL\n
    \tINTERNAL\n
    NOTIMPLEMENTED (not included in order)
    """
    def __init__(self, error, level) -> None:
        self.error = error
        level = level.upper()
        match level:
            case "WARNING":
                self.warning()
            case "CRITICAL":
                self.critical()
            case "INTERNAL":
                self.internal()
            case "NOTIMPLEMENTED" | _:
                print(f"Error - {self.error}")    
    def warning(self):
        print(f"WARNING - {self.error}")
    
    def critical(self):
        print(f"CRITICAL - {self.error}")
    
    def internal(self):
        print(f"INTERNAL - {self.error}")