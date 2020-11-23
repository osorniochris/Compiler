from State import State
from Transition import Transition
from Subset import Subset
from AFD import AFD
from queue import LifoQueue
from graphviz import Digraph
import tempfile

class AFN:
    def __init__(self, id_, initial_state, alphabet, accept_states, states):
        self.id_ = id_
        self.initial_state = initial_state
        self.alphabet = alphabet
        self.accept_states = accept_states
        self.states = states
    
    @staticmethod
    def create_basic(current_state_id, current_afn_id, token, char1, char2):
        initial_state = State(current_state_id+1, [], True, False, -1)
        accept_state = State(current_state_id+2, [], False, True, token)

        initial_state.add_transition(Transition(char1, char2, {accept_state}))
        
        new_alphabet = set()
        ini = ord(char1)
        fin = ord(char2)
        
        for x in range(ini, fin+1):
            new_alphabet.add(chr(x))

        a = AFN(current_afn_id, initial_state, new_alphabet , {accept_state}, {initial_state, accept_state})
        return a

    def join_afn(self, afn, current_state_id, afn_id, token):
        new_states = set()

        initial_state = State(current_state_id+1, [], True, False, -1)
        final_state = State(current_state_id+2, [], False, True, token)

        for a_s in self.states:
            if a_s.is_accept_state:
                a_s.add_transition(Transition(chr(400), chr(400), {final_state}))
                a_s.is_accept_state = False
            if a_s.is_initial_state:
                initial_state.add_transition(Transition(chr(400), chr(400), {a_s}))
                a_s.is_initial_state = False
        
        for a_s in afn.states:
            if a_s.is_accept_state:
                a_s.add_transition(Transition(chr(400), chr(400), {final_state}))
                a_s.is_accept_state = False
            if a_s.is_initial_state:
                initial_state.add_transition(Transition(chr(400), chr(400), {a_s}))
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
                            x.add_transition(Transition(tx.symbol_1, tx.symbol_2, {s}))

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
        new_initial_state = State(current_state_id+1, [], True, False, -1)
        #Se crea el nuevo estado de aceptacion
        new_accept_state = State(current_state_id+2, [], False, True, token)
        
        for t in self.states:
        	#Si el estado actual es el estado de aceptacion del AFN
        	if t.is_accept_state:
        		#Se añade una transicion del mismo al estado inicial
        		t.add_transition(Transition(chr(400), chr(400), {self.initial_state}))

        for t in self.states:
        	#Si el estado actual es el estado de aceptacion del AFN
        	if t.is_accept_state:
        		#Se añade una transicion del mismo al nuevo estado de aceptacion
        		t.add_transition(Transition(chr(400), chr(400), {new_accept_state}))
        		#El estado actual ya no será de aceptación
        		t.is_accept_state = False
        	#Si el estado actual es el estado inicial del AFN
        	if t.is_initial_state:
        		#El nuevo estado inicial hara una transicion hacia el estado actual
        		new_initial_state.add_transition(Transition(chr(400), chr(400), {t}))
        		#El estado actual ya no sera de aceptacion
        		t.is_initial_state = False
        		

        new_initial_state.add_transition(Transition(chr(400), chr(400), {new_accept_state}))

        new_states.update(self.states)
        new_states.add(new_initial_state)
        new_states.add(new_accept_state)

        a = AFN(afn_id, new_initial_state, self.alphabet, {new_accept_state}, new_states)
        return a				

    def kleene_plus(self, afn_id, current_state_id, token):
    	#Se define el set donde iran los nuevos estados
        new_states = set()

    	#Se crea el nuevo estado inicial
        new_initial_state = State(current_state_id+1, [], True, False, -1)
        #Se crea el nuevo estado de aceptacion
        new_accept_state = State(current_state_id+2, [], False, True, token)
        
        for t in self.states:
        	#Si el estado actual es el estado de aceptacion del AFN
        	if t.is_accept_state:
        		#Se añade una transicion del mismo al estado inicial
        		t.add_transition(Transition(chr(400), chr(400), {self.initial_state}))

        for t in self.states:
        	#Si el estado actual es el estado de aceptacion del AFN
        	if t.is_accept_state:
        		#Se añade una transicion del mismo al nuevo estado de aceptacion
        		t.add_transition(Transition(chr(400), chr(400), {new_accept_state}))
        		#El estado actual ya no será de aceptación
        		t.is_accept_state = False
        		
        	#Si el estado actual es el estado inicial del AFN
        	if t.is_initial_state:
        		#El nuevo estado inicial hara una transicion hacia el estado actual
        		new_initial_state.add_transition(Transition(chr(400), chr(400), {t}))
        		#El estado actual ya no sera de aceptacion
        		t.is_initial_state = False
        		
        new_states.update(self.states)
        new_states.add(new_initial_state)
        new_states.add(new_accept_state)

        a = AFN(afn_id, new_initial_state, self.alphabet, {new_accept_state}, new_states)
        return a
    
    def optional_operator(self, afn_id, current_state_id, token):
        new_initial_state = State(current_state_id+1, [], True, False, -1)
        new_final_state = State(current_state_id+2,[], False, True, token)
        
        new_states = set()
        
        for t in self.states:
            if t.is_accept_state:
                new_initial_state.add_transition(Transition(chr(400), chr(400), {self.initial_state}))
                new_initial_state.add_transition(Transition(chr(400), chr(400), {new_final_state}))
                t.add_transition(Transition(chr(400), chr(400), {new_final_state}))
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
                if ord(t.symbol_1) == 400 and ord(t.symbol_2) == 400:
                    if not t.destination_states.issubset(R):
                        s_aux = t.destination_states.pop()
                        S.put(s_aux)
                        t.destination_states.add(s_aux)

        
        return R

    #Operacion Move: Recibe un Estado "E", un simbolo "c"
    #                Regresa un Conjunto de Estados "R"
    @staticmethod
    def move_one(c, state):
        R = set()
        for t in state.transitions:
            if c >= t.symbol_1 and c <= t.symbol_2:
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
                        exists = False
                        for r_ in R:
                            if r_.states == states:
                                exists = True
                                sn = Subset(r_.id_, r_.states)
                        for r_ in checked:
                            if r_.states == states:
                                exists = True
                                sn = Subset(r_.id_, r_.states)
                        if r.states == states:
                            exists = True
                            sn = Subset(r.id_, r_.states)
                        
                        if not exists:
                            sn = Subset(i, states)
                            token_1 = -1
                            token_2 = -1

                            for y in r.states:
                                for w in self.accept_states:
                                    if w.id_ == y.id_:
                                        token_1 = w.token
                                        break 
                            for y in sn.states:
                                for w in self.accept_states:
                                    if w.id_ == y.id_:
                                        token_2 = w.token
                                        break 
                        
                            t = (r.id_, i, c, token_1, token_2)
                            afd.add(t)
                            afd.add_to_table(t)
                            i += 1
                            R.add(sn)
                        else:
                            token_1 = -1
                            token_2 = -1

                            for y in r.states:
                                for w in self.accept_states:
                                    if w.id_ == y.id_:
                                        token_1 = w.token
                                        break 
                            for y in sn.states:
                                for w in self.accept_states:
                                    if w.id_ == y.id_:
                                        token_2 = w.token
                                        break 

                            t = (r.id_, sn.id_, c, token_1, token_2)
                            afd.add(t)
                            afd.add_to_table(t)
                            
                checked.append(r)

        afd.table_to_file()

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
                    if t.symbol_1 == t.symbol_2:
                        f.edge(str(s.id_), str(d.id_), label= str(t.symbol_1))
                    else:
                        f.edge(str(s.id_), str(d.id_), label= str(t.symbol_1)+"-"+str(t.symbol_2))

        f.view(tempfile.mktemp())
    
    @staticmethod
    def union_to_afd(afns, current_state_id, afn_id):
        
        new_alphabet = []
        new_accept_states = set()
        new_states = set()

        i_s = State(current_state_id+1, [], True, False, -1)

        for afn in afns:
            i_s.add_transition(Transition(chr(400), chr(400), {afn.initial_state}))
            afn.initial_state.is_initial_state = False

            new_alphabet.extend([element for element in afn.alphabet if element not in new_alphabet])
            new_accept_states.update(afn.accept_states)
            new_states.update(afn.states)

        new_states.update({i_s})
        a = AFN(afn_id, i_s, new_alphabet, new_accept_states, new_states)

        return a
