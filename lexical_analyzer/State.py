class State:
    def __init__(self, id, transitions, is_initial_state, is_accept_state, token):
        self.id = id
        self.transitions = transitions
        self.is_initial_state = is_initial_state
        self.is_accept_state = is_accept_state
        self.token = token

