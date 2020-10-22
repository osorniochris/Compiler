class AFD:
    def __init__(self, id, initial_state, alphabet, accept_states, states, table):
        self.id = id
        self.initial_state = initial_state
        self.alphabet = alphabet
        self.accept_states = accept_states
        self.states = states
        self.table = table