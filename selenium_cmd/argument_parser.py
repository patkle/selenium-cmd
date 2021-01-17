def split_args(line):
    """split line into arguments"""
    chars = list(__mark_argument_position(line))
    args = ''.join(chars).split('\n')
    args = __remove_quotes(*args)
    return args

def __mark_argument_position(line):
    """mark position at which an argument ends with \n"""
    open_double = False
    open_single = False
    for char in line:
        if char == ' ' and not open_double and not open_single:
            char = '\n'
        elif char == '"':
            open_double = not open_double
        elif char == "'":
            open_single = not open_single
        yield char
    
def __remove_quotes(*args):
    """remove leading and trailing quotation mark from every arg in args"""
    for arg in args:
        if arg.startswith("'") and arg.endswith("'") or arg.startswith('"') and arg.endswith('"'):
            arg = arg[1:-1]
        yield arg
