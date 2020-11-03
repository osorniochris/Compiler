class Transition:
    def __init__(self, symbol, destination_states):
        self.symbol = symbol
        self.destination_states = destination_states

    def __hash__(self):
        return hash((self.symbol, tuple(self.destination_states)))

    def __eq__(self, other):
        if not isinstance(other, type(self)): 
            return NotImplemented
        else:
            return self.symbol == other.symbol and tuple(self.destination_states) == tuple(other.destination_states)