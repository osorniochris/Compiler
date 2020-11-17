class State:
    def __init__(self, id_, transitions, is_initial_state, is_accept_state, token):
        self.id_ = id_
        self.transitions = transitions
        self.is_initial_state = is_initial_state
        self.is_accept_state = is_accept_state
        self.token = token
    
    def __hash__(self):
        return hash((self.id_, self.is_initial_state, self.is_accept_state, self.token))

    def __eq__(self, other):
        if not isinstance(other, type(self)): 
            return NotImplemented
        else:
            return self.id_ == other.id_ and  self.is_initial_state == other.is_initial_state and self.is_accept_state == other.is_accept_state and self.token == other.token
    
    def add_transition(self, transition):
        self.transitions.append(transition)

