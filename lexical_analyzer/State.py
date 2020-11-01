class State:
    def __init__(self, id, transitions, is_initial_state, is_accept_state, token):
        self.id = id
        self.transitions = transitions
        self.is_initial_state = is_initial_state
        self.is_accept_state = is_accept_state
        self.token = token
    
    def __hash__(self):
        return hash((self.id, tuple(self.transitions), self.is_initial_state, self.is_accept_state, self.token))

    def __eq__(self, other):
        if not isinstance(other, type(self)): 
            return NotImplemented
        else:
            return self.id == other.id and self.transitions == other.transitions and self.is_initial_state == other.is_initial_state and self.is_accept_state == other.is_accept_state and self.token == other.token

    def add_transition(self, transition):
        self.transitions.append(transition)

