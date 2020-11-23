from State import State
from Transition import Transition
from graphviz import Digraph
import tempfile
import json

class AFD:
    def __init__(self, id_, initial_state, alphabet, accept_states, states):
        self.id_ = id_
        self.initial_state = initial_state
        self.alphabet = alphabet
        self.accept_states = accept_states
        self.states = states
        self.table = {}

    
    def add(self, t):
        subset, i, c, token_1, token_2 = t
        origin_exists = False

        if token_2 != -1:
            destination = State(i, [], False, True, token_2) 
            self.states.add(destination)
            self.accept_states.add(destination)
        else:
            destination = State(i, [], False, False, -1) 
            self.states.add(destination)

        for s in self.states:
            if s.id_ == subset:
                origin_exists = True
                if token_1 != -1:
                    s.is_accept_state = True
                    s.token = token_1
                    self.accept_states.add(s)
                s.add_transition(Transition(c, c, {destination}))
                
        if not origin_exists:
            if subset == 0:
                if token_1 == -1:
                    state = State(subset, [], True, False, -1)
                    self.initial_state = state
                else:
                    state = State(subset, [], True, True, token_1)
                    self.initial_state = state
                    self.accept_states.add(state)
            else:
                if token_1 == -1:
                    state = State(subset, [], False, False, -1)
                else:
                    state = State(subset, [], False, True, token_1)
                    self.accept_states.add(state)
            
            state.add_transition(Transition(c, c, {destination}))
            self.states.add(state)

    def add_to_table(self, t):
        subset, i, c, token_1, token_2 = t
        row = self.table.get(subset)
        row_2 = self.table.get(i)

        if row == None:
            self.table[int(subset)] = {}
            for a in self.alphabet:
                if a == c:
                    self.table[int(subset)][a] = int(i)
                else:
                    self.table[int(subset)][a] = -1
            self.table[int(subset)]['token'] = int(token_1)
        else:
            self.table[int(subset)][c] = int(i)
            self.table[int(subset)]['token'] = int(token_1)
        
        if row_2 == None:
            self.table[int(i)] = {}
            for a in self.alphabet:
                self.table[int(i)][a] = -1
            self.table[int(i)]['token'] = int(token_2)
        else:
            self.table[int(i)][c] = int(i)
            self.table[int(i)]['token'] = int(token_2)
        

    def show(self):
        f = Digraph('afn_' + str(self.id_), filename='afn_' + str(self.id_), format='png')
        f.attr(rankdir='LR', size='8,5')
        
        f.attr('node', shape='doublecircle')
        for s in self.accept_states:
            f.node(str(s.id_))

        f.attr('node', shape='circle')
        f.node(str(self.initial_state.id_))

        for s in self.states:
            for t in s.transitions:
                for d in t.destination_states:
                    if t.symbol_1 == t.symbol_2:
                        f.edge(str(s.id_), str(d.id_), label= str(t.symbol_1))
                    else:
                        f.edge(str(s.id_), str(d.id_), label= str(t.symbol_1)+"-"+str(t.symbol_2))

        f.view(tempfile.mktemp())
    
    def table_to_file(self):
        with open('afd'+self.id_+'_table.json', 'w') as table_json:
            json.dump(self.table, table_json, indent=2)



        

