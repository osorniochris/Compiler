from State import State
from Transition import Transition
from queue import LifoQueue

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
        S = LifoQueue()
        R = set()
        S.put(state)

        while not S.empty() :
            p = S.get()
            print(p)
            R.add(p)

            for t in p.transitions:
                if ord(t.symbol) == 400:
                    if not t.destination_states.issubset(R):
                        S.put(t.destination_states.pop())
        
        return R

    def move_one(self, c, state):
        pass

    def epsilon_closure(self, states):
        R = set()

        for s in states:
            R.union(self.single_epsilon_closure(s))
        
        return R
        
    def move(self, c, states):
        pass

    def go_to(self, c, states):
        pass

    def to_afd(self):
        pass

    def check_string(self, string):
        pass



s_26 = State(26, [], False, False, 0)
s_27 = State(27, [], False, False, 0)
s_28 = State(28, [], False, False, 0)
s_30 = State(30, [], False, False, 0)
t_26_27 = Transition(chr(400), {s_27})
t_27_28 = Transition(chr(400), {s_28})
t_27_30 = Transition(chr(400), {s_30})

s_26.add_transition(t_26_27)
s_27.add_transition(t_27_28)
s_27.add_transition(t_27_30)

s = single_epsilon_closure(s_26)

