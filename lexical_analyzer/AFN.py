from State import State
from Transition import Transition
from Subset import Subset
from AFD import AFD
from queue import LifoQueue
from graphviz import Digraph
import tempfile
import copy

class AFN:
    def __init__(self, id_, initial_state, alphabet, accept_states, states):
        self.id_ = id_
        self.initial_state = initial_state
        self.alphabet = alphabet
        self.accept_states = accept_states
        self.states = states
    
    @staticmethod
    def create_basic(current_state_id, current_afn_id, token, symbol):
        initial_state = State(current_state_id+1, [], True, False, 0)
        accept_state = State(current_state_id+2, [], False, True, token)

        initial_state.add_transition(Transition(symbol, {accept_state}))

        a = AFN(current_afn_id, initial_state, {symbol}, {accept_state}, {initial_state, accept_state})
        return a

    def join_afn(self, afn, current_state_id, afn_id, token):
        new_states = set()

        initial_state = State(current_state_id+1, [], True, False, 0)
        final_state = State(current_state_id+2, [], False, True, token)

        for a_s in self.states:
            if a_s.is_accept_state:
                a_s.add_transition(Transition(chr(400), {final_state}))
                a_s.is_accept_state = False
            if a_s.is_initial_state:
                initial_state.add_transition(Transition(chr(400), {a_s}))
                a_s.is_initial_state = False
        
        for a_s in afn.states:
            if a_s.is_accept_state:
                a_s.add_transition(Transition(chr(400), {final_state}))
                a_s.is_accept_state = False
            if a_s.is_initial_state:
                initial_state.add_transition(Transition(chr(400), {a_s}))
                a_s.is_initial_state = False
        
        new_alphabet = list(set(self.alphabet) | set(afn.alphabet))
        new_states.update(self.states) 
        new_states.update(afn.states)
        new_states.add(initial_state)
        new_states.add(final_state)

        a = AFN(afn_id, initial_state, new_alphabet, {final_state}, new_states)

        return a
        
    def concatenate_afn(self, afn, afn_id, token):

        for s in self.states:
            if s.is_accept_state:
                for t in afn.initial_state.transitions:
                    s.add_transition(t)

                for x in afn.states:
                    for tx in x.transitions:
                        if {afn.initial_state}.issubset(tx.destination_states):
                            x.add_transition(Transition(tx.symbol, {s}))

                s.is_accept_state = False
                s.token = 0

        afn.states.remove(afn.initial_state)
        
        for a_s in afn.accept_states:
            a_s.token = token
        
        for a_s in afn.states:
            if a_s.is_accept_state:
                a_s.token = token

        new_alphabet = list(set(self.alphabet) | set(afn.alphabet))
        new_states = set()
        new_states.update(self.states) 
        new_states.update(afn.states)
        
        a = AFN(afn_id, self.initial_state, new_alphabet, afn.accept_states, new_states)

        return a

    def kleene_star(self, afn_id, current_state_id, token):
    	#Se define el set donde iran los nuevos estados
        new_states = set()

    	#Se crea el nuevo estado inicial
        new_initial_state = State(current_state_id+1, [], True, False, 0)
        #Se crea el nuevo estado de aceptacion
        new_accept_state = State(current_state_id+2, [], False, True, token)
        
        for t in self.states:
        	#Si el estado actual es el estado de aceptacion del AFN
        	if t.is_accept_state:
        		#Se añade una transicion del mismo al estado inicial
        		t.add_transition(Transition(chr(400), {self.initial_state}))

        for t in self.states:
        	#Si el estado actual es el estado de aceptacion del AFN
        	if t.is_accept_state:
        		#Se añade una transicion del mismo al nuevo estado de aceptacion
        		t.add_transition(Transition(chr(400), {new_accept_state}))
        		#El estado actual ya no será de aceptación
        		t.is_accept_state = False
        	#Si el estado actual es el estado inicial del AFN
        	if t.is_initial_state:
        		#El nuevo estado inicial hara una transicion hacia el estado actual
        		new_initial_state.add_transition(Transition(chr(400), {t}))
        		#El estado actual ya no sera de aceptacion
        		t.is_initial_state = False
        		

        new_initial_state.add_transition(Transition(chr(400), {new_accept_state}))

        new_states.update(self.states)
        new_states.add(new_initial_state)
        new_states.add(new_accept_state)

        a = AFN(afn_id, new_initial_state, self.alphabet, {new_accept_state}, new_states)
        return a				

    def kleene_plus(self, afn_id, current_state_id, token):
    	#Se define el set donde iran los nuevos estados
        new_states = set()

    	#Se crea el nuevo estado inicial
        new_initial_state = State(current_state_id+1, [], True, False, 0)
        #Se crea el nuevo estado de aceptacion
        new_accept_state = State(current_state_id+2, [], False, True, token)
        
        for t in self.states:
        	#Si el estado actual es el estado de aceptacion del AFN
        	if t.is_accept_state:
        		#Se añade una transicion del mismo al estado inicial
        		t.add_transition(Transition(chr(400), {self.initial_state}))

        for t in self.states:
        	#Si el estado actual es el estado de aceptacion del AFN
        	if t.is_accept_state:
        		#Se añade una transicion del mismo al nuevo estado de aceptacion
        		t.add_transition(Transition(chr(400), {new_accept_state}))
        		#El estado actual ya no será de aceptación
        		t.is_accept_state = False
        		
        	#Si el estado actual es el estado inicial del AFN
        	if t.is_initial_state:
        		#El nuevo estado inicial hara una transicion hacia el estado actual
        		new_initial_state.add_transition(Transition(chr(400), {t}))
        		#El estado actual ya no sera de aceptacion
        		t.is_initial_state = False
        		
        new_states.update(self.states)
        new_states.add(new_initial_state)
        new_states.add(new_accept_state)

        a = AFN(afn_id, new_initial_state, self.alphabet, {new_accept_state}, new_states)
        return a
    
    def optional_operator(self, afn_id, current_state_id, token):
        new_initial_state = State(current_state_id+1, [], True, False, 0)
        new_final_state = State(current_state_id+2,[], False, True, token)
        
        new_states = set()
        
        for t in self.states:
            if t.is_accept_state:
                new_initial_state.add_transition(Transition(chr(400), {self.initial_state}))
                new_initial_state.add_transition(Transition(chr(400), {new_final_state}))
                t.add_transition(Transition(chr(400), {new_final_state}))
                t.is_accept_state = False
                self.initial_state.is_initial_state = False
            
        new_states.update(self.states)
        new_states.add(new_initial_state)
        new_states.add(new_final_state)
        
        a = AFN(afn_id, new_initial_state, self.alphabet, {new_final_state}, new_states)
        
        return a

    @staticmethod
    def single_epsilon_closure(state):
        S = LifoQueue()
        R = set()
        S.put(state)

        while not S.empty() :
            p = S.get()
            R.add(p)

            for t in p.transitions:
                if ord(t.symbol) == 400:
                    if not t.destination_states.issubset(R):
                        S.put(t.destination_states.pop())
        
        return R

    #Operacion Move: Recibe un Estado "E", un simbolo "c"
    #                Regresa un Conjunto de Estados "R"
    @staticmethod
    def move_one(c, state):
        R = set()
        for t in state.transitions:
            if t.symbol == c:
                R.update(t.destination_states)
        return R

    @staticmethod
    def epsilon_closure(states):
        R = set()

        for s in states:
            R.update(AFN.single_epsilon_closure(s))
        
        return R
    
    #Operacion MoveTo: Recibe un Conjunto de Estados "E", un simbolo "c"
    #                  Regresa un Conjunto de Estados "R"
    @staticmethod
    def move(c, states):
        R = set()
        for e in states:
            R.update(AFN.move_one(c, e))
        return R
    
    @staticmethod
    #Operacion GoTo: Recibe un Conjunto de Estados "E", un simbolo "c"
    #                Regresa un Conjunto de Estados "R"
    def go_to(c, states):
        R = set()
        R = AFN.epsilon_closure(AFN.move(c, states))
        return R

    def to_afd(self, id_afd, current_state_id):
        R = set()
        checked = []
        self = copy.copy(self)

        s_0 = Subset(0, AFN.epsilon_closure({self.initial_state}))
        R.add(s_0)
        i = 1

        afd = AFD(id_afd, None, self.alphabet, set(), set())

        while len(R) > 0:
            r = R.pop()
            if not r in checked:
                for c in self.alphabet:
                    states = AFN.go_to(c, r.states)

                    if len(states) != 0:
                        id_aux = i 
                        exists = False
                        for r_ in checked:
                            if r_.states.issubset(states) and r_.states.issuperset(states):
                                id_aux == r_.id_ 
                                exists = True
                        
                        if not exists:
                            sn = Subset(i, states)
                            token_1 = 0
                            token_2 = 0
                        
                            e = r.states.intersection(self.accept_states)
                            if len(e) != 0:
                                token_1 = e.pop().token
                            
                            d = sn.states.intersection(self.accept_states)
                            if len(d) != 0:
                                token_2 = d.pop().token
                        
                            t = (r.id_, i, c, token_1, token_2)
                            afd.add(t)
                            afd.add_to_table(t)
                            i += 1
                            R.add(sn)
                        else:
                            t = (r.id_, id_aux, c, token_1, token_2)
                            afd.add(t)
                            afd.add_to_table(t)
                            
                checked.append(r)

        return afd

    def check_string(self, string):
        E = set()

        E = self.single_epsilon_closure(self.initial_state)

        for s in string:
            E = AFN.go_to(s, E)
            if len(E) == 0:
                return False
        
        if E.isdisjoint(self.accept_states):
            return False

        return True 

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
                    f.edge(str(s.id_), str(d.id_), label= str(t.symbol))

        f.view(tempfile.mktemp())
    
    @staticmethod
    def union_to_afd(afns, current_state_id, afn_id):
        
        new_alphabet = []
        new_accept_states = set()
        new_states = set()

        i_s = State(current_state_id+1, [], True, False, 0)

        for afn in afns:
            i_s.add_transition(Transition(chr(400), {afn.initial_state}))
            afn.initial_state.is_initial_state = False

            new_alphabet.extend([element for element in afn.alphabet if element not in new_alphabet])
            new_accept_states.update(afn.accept_states)
            new_states.update(afn.states)

        new_states.update({i_s})
        a = AFN(afn_id, i_s, new_alphabet, new_accept_states, new_states)

        return a
