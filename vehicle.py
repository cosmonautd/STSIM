class Vehicle:
    def __init__(self, G, initial, terminal):
        self.map = G
        self.initial  = initial
        self.terminal = terminal
        self.current  = initial
        self.path = None
        self.next = None

    def set_path(self, path):
        self.path = path
        self.next = 1

    def get_initial(self):
        return self.initial

    def get_terminal(self):
        return self.terminal

    def get_current(self):
        return self.current

    def get_path(self):
        return self.path

    def update_state(self):
        if self.next < len(self.path):
            self.current = self.map.node[self.path[self.next]]
            self.next += 1
