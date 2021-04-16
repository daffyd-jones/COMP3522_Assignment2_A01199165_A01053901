class Request:

    def __init__(self, m, t, e, o):
        self.mode = m
        self.inputType = t
        self.expanded = e
        self.output = o

    def get_mode(self):
        return self.mode

    def get_iput_type(self):
        return self.inputType

    def is_expanded(self):
        return self.expanded

    def get_output(self):
        return self.output
