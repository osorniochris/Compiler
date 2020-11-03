from State import State
from Transition import Transition

class AFD:
    def __init__(self, id, initial_state, alphabet, accept_states, states):
        self.id = id
        self.initial_state = initial_state
        self.alphabet = alphabet
        self.accept_states = accept_states
        self.states = states
        self.table = {}

    
    def add(self, t):
        subset, i, c, token = t
        origin_exists = False

        destination = State(i, [], False, False, 0) 
        self.states.add(destination)

        for s in self.states:
            if s.id == subset:
                origin_exists = True
                if token != 0:
                    s.is_accept_state = True
                    s.token = token
                    self.accept_states.add(s)
                s.add_transition(Transition(c, {destination}))
                
        if not origin_exists:
            if subset == 0:
                if token == 0:
                    state = State(subset, [], True, False, 0)
                    self.initial_state = state
                else:
                    state = State(subset, [], True, True, token)
                    self.initial_state = state
                    self.accept_states.add(state)
            else:
                if token == 0:
                    state = State(subset, [], False, False, 0)
                else:
                    state = State(subset, [], False, True, token)
                    self.accept_states.add(state)
            
            state.add_transition(Transition(c, {destination}))
            self.states.add(state)
            self.alphabet.append(c)

    def add_to_table(self, t):
        subset, i, c, token = t
        row = self.table.get(subset)

        if row == None:
            self.table[subset] = {}
            for a in self.alphabet:
                if a == c:
                    self.table[subset][a] = i
                else:
                    self.table[subset][a] = -1
            self.table[subset]['token'] = token
        else:
            self.table[subset][c] = i
            self.table[subset]['token'] = token




        

