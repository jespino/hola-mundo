import token
import symbol
from pprint import pprint

def stpp(st):
    def translate_st(st):
        if isinstance(st, tuple):
            return tuple(map(translate_st, st))
        elif isinstance(st, int):
            return token.tok_name.get(st, symbol.sym_name.get(st))
        else:
            return st

    pprint(translate_st(st.totuple()))
