from State import State
from Transition import Transition
from queue import LifoQueue
from graphviz import Digraph

class AFN:
    def __init__(self, id, initial_state, alphabet, accept_states, states):
        self.id = id
        self.initial_state = initial_state
        self.alphabet = alphabet
        self.accept_states = accept_states
        self.states = states
    
    def create_basic(self, symbol):
        pass

    def join_afn(self, afn, current_state_id, afn_id, token):
        new_states = set()

        initial_state = State(current_state_id+1, [], True, False, 0)
        final_state = State(current_state_id+2, [], False, True, token)

        for a_s in self.states:
            if a_s.is_accept_state:
                a_s.add_transition(Transition(chr(400), final_state))
                a_s.is_accept_state = False
            if a_s.is_initial_state:
                initial_state.add_transition(Transition(chr(400), a_s))
                a_s.is_initial_state = False
        for a_s in afn.states:
            if a_s.is_accept_state:
                a_s.add_transition(Transition(chr(400), final_state))
                a_s.is_accept_state = False
            if a_s.is_initial_state:
                initial_state.add_transition(Transition(chr(400), a_s))
                a_s.is_initial_state = False
        
        new_alphabet = list(set(self.alphabet) | set(afn.alphabet))
        new_states.union(self.states) 
        new_states.union(afn.states)
        new_states.add(initial_state)
        new_states.add(final_state)

        a = AFN(afn_id, initial_state, new_alphabet, {final_state}, new_states)

        return a
        
    def concatenate_afn(self, afn, afn_id, token):
        
        for s in self.states:
            if s.is_accept_state:
                for t in afn.initial_state.transitions:
                    s.add_transition(t)
                s.is_accept_state = False
                s.token = 0
        
        for s in afn.states:
            if s.is_initial_state:
                afn.states.remove(s)
        
        for a_s in afn.accept_states:
            a_s.token = token
        
        new_alphabet = list(set(self.alphabet) | set(afn.alphabet))
        new_states = set()
        new_states.union(self.states) 
        new_states.union(afn.states)
        
        a = AFN(afn_id, self.initial_state, new_alphabet, afn.accept_states, new_states)

        return a

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
        E = set()

        E = self.single_epsilon_closure(self.initial_state)

        for s in string:
            E = self.go_to(E, s)
            if len(E) == 0:
                return False
        
        if E.isdisjoint(self.accept_states):
            return False

        return True 

    def show(self):
        f = Digraph('afn_' + str(self.id), filename='afn_' + str(self.id)+'.png')
        f.attr(rankdir='LR', size='8,5')
        
        f.attr('node', shape='doublecircle')
        for s in self.accept_states:
            f.node(str(s.id))

        f.attr('node', shape='circle')
        f.node(str(self.initial_state.id))

        for s in self.states:
            if not s.is_initial_state and not s.is_accept_state:
                for t in s.transitions:
                    for d in t.destination_states:
                        f.edge(str(s.id), str(d.id), label= str(t.symbol))

        f.view()
    
    @staticmethod
    def union_to_afd(afns, current_state_id, afn_id):
        
        destination = set()
        new_alphabet = []
        new_accept_states = set()
        new_states = set()

        initial_state = State(current_state_id+1, [], True, False, 0)

        for afn in afns:
            afn.initial_state.is_initial_state = False
            destination.add(afn.initial_state)

            new_alphabet = list(set(new_alphabet) | set(afn.alphabet)) 
            new_accept_states.union(afn.accept_states)
            new_states.union(afn.states)

        t = Transition(chr(400), destination)
        initial_state.add_transition(t)

        a = AFN(afn_id, initial_state, new_alphabet, new_accept_states, new_states)

        return a
