def symtablepp(symtable, indentation=''):
    print("{} {}".format(
        indentation,
        symtable,
    ))

    for symbol in symtable.get_symbols():
        print("{} {}".format(
            indentation + '  ',
            symbol
        ))

    for child in symtable.get_children():
        symtablepp(child, indentation=indentation + '  ')
