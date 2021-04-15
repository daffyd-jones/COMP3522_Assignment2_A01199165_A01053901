class Request:
    def __init__(self):
        self.mode = None
        self.input = None
        self.expanded = None
        self.output = None
        self.endpoint = None

    def get_mode(self):
        return self.mode
