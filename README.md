# ShowCallStack

Shows a simplified view of the call stack.

This module is similar to Python's built-in `traceback` and `inspect` modules, but is easier to use and displays more simple output. This module is useful for demonstrating what the call stack looks like during recursive function calls. Simply add a `from showcallstack import display_call_stack` line and then call `display_call_stack()` from wherever you wish to see the state of the call stack and the local variables in each call frame.

Example Usage
=============

This program...

    from showcallstack import display_call_stack

    def a():
        varA = 42
        b()

    def b():
        varB = 86
        c()

    def c():
        varC = 99
        display_call_stack()

    spam = 'SPAM!
    a()

...outputs this:

    The call stack is 3 call(s) deep:
    (Here is the "bottom" of the call stack.)
    Local variables of call to a():
      varA (type: int) == 42
    Local variables of call to b():
      varB (type: int) == 86
    Local variables of call to c():
      varC (type: int) == 99
    (Here is the "top" of the call stack.)

    Global variables:
      spam (type: str) == 'SPAM!'

This recursive factorial program...

    from showcallstack import display_call_stack

    def factorial(num):
        display_call_stack()
        if num == 1:
            return 1
        else:
            return num * factorial(num - 1)

    factorial(4)

...outputs this:

    The call stack is 1 call(s) deep:
    (Here is the "bottom" of the call stack.)
    Local variables of call to factorial():
      num (type: int) == 4
    (Here is the "top" of the call stack.)

    Global variables:
      No global variables.

    The call stack is 2 call(s) deep:
    (Here is the "bottom" of the call stack.)
    Local variables of call to factorial():
      num (type: int) == 4
    Local variables of call to factorial():
      num (type: int) == 3
    (Here is the "top" of the call stack.)

    Global variables:
      No global variables.

    The call stack is 3 call(s) deep:
    (Here is the "bottom" of the call stack.)
    Local variables of call to factorial():
      num (type: int) == 4
    Local variables of call to factorial():
      num (type: int) == 3
    Local variables of call to factorial():
      num (type: int) == 2
    (Here is the "top" of the call stack.)

    Global variables:
      No global variables.

    The call stack is 4 call(s) deep:
    (Here is the "bottom" of the call stack.)
    Local variables of call to factorial():
      num (type: int) == 4
    Local variables of call to factorial():
      num (type: int) == 3
    Local variables of call to factorial():
      num (type: int) == 2
    Local variables of call to factorial():
      num (type: int) == 1
    (Here is the "top" of the call stack.)

    Global variables:
      No global variables.

You can also call the `showcallstack.get_traceback_info()` to get the current traceback info or the `showcallstack.get_all_frames` to get all the current frames on the stack.

Support
-------

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon](https://www.patreon.com/AlSweigart).
