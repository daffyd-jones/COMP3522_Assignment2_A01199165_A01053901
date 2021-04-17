class Request:
    """
    request class
    """

    def __init__(self, m, t, e, o):
        """
        request init
        :param m: mode - string
        :param t: input - string
        :param e: expanded - bool
        :param o: output - string
        """
        self.mode = m
        self.input = t
        self.expanded = e
        self.output = o
        self.input_data = None

    def get_mode(self):
        """
        returns mode
        :return: string
        """
        return self.mode

    def get_input(self):
        """
        returns input
        :return: string
        """
        return self.input

    def is_expanded(self):
        """
        returns whether expanded
        :return: bool
        """
        return self.expanded

    def get_output(self):
        """
        returns output
        :return: string
        """
        return self.output

    def set_input(self, data):
        """
        sets input_data
        :param data: data to be queried - string
        :return: void
        """
        self.input_data = data
