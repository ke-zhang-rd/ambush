from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

import inspect

def detector():
    previous_frame = inspect.currentframe().f_back.f_back
    (filename, line_number, function_name, lines, index) = inspect.getframeinfo(previous_frame)
    actual_call = lines[index][:-1]
    stack = inspect.stack()
    caller_class = previous_frame.f_locals["self"].__class__.__name__
    caller_line = previous_frame.f_code.co_firstlineno
    print("Who is calling current function")
    print("==========================================================")
    print("In file:") 
    print(f"{filename}")
    print()
    print(f"class {caller_class}:") 
    print("    # by caller function:")
    print(f"    def {function_name} in line {caller_line}")
    print(f"        ...") 
    print(f"        # actually call:") 
    print(f"{actual_call} # in line {line_number}")
    print(f"        ...") 
    print()
    print("Peek:")
    print("---------------------------------------------------------")
    print(inspect.getsource(inspect.currentframe().f_back.f_back))
    print("==========================================================")
