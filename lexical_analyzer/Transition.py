class Transition:
    def __init__(self, symbol_1, symbol_2, destination_states):
        self.symbol_1 = symbol_1
        self.symbol_2 = symbol_2
        self.destination_states = destination_states

    def __hash__(self):
        return hash((self.symbol_1, self.symbol_2, tuple(self.destination_states)))

    def __eq__(self, other):
        if not isinstance(other, type(self)): 
            return NotImplemented
        else:
            return self.symbol_1 == other.symbol_1 and self.symbol_2 == other.symbol_2 and tuple(self.destination_states) == tuple(other.destination_states)