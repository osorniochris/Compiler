class AFN:
    def __init__(self, id, initial_state, alphabet, accept_states, states):
        self.id = id
        self.initial_state = initial_state
        self.alphabet = alphabet
        self.accept_states = accept_states
        self.states = states
    
    def create_basic(self, symbol):
        pass

    def join_afn(self, afn):
        pass

    def concatenate_afn(self, afn):
        pass

    def kleene_star(self):
        pass

    def kleene_plus(self):
        pass

    def optional_operator(self):
        pass

    def single_epsilon_closure(self, state):
        pass

    def move_one(self, c, state):
        pass

    def epsilon_closure(self, states):
        pass

    def move(self, c, states):
        pass

    def go_to(self, c, states):
        pass

    def to_afd(self):
        pass

    def check_string(self, string):
        pass
