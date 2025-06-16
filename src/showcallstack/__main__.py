"""
Module for defining callstack functions.
"""
import traceback
import inspect

# - - - - - - - - - - - - - - - - - - - - -

def get_traceback_info(exclude_offset:tuple=(1,2)) -> list:
    """
    Get trackback info.

    Args:
        exclude_offset (tuple): Start and end offset to exclude from traceback, must be positive, default = 2

    Returns:
        list: List of tracebacks (from top to bottom of callstack).
    """
    # Check `exclude_offset` argument.
    if type(exclude_offset) is not tuple and len(exclude_offset) != 2:
        raise ValueError("Please provide tuple of length 2 for `exclude_offset` arg.")
    if exclude_offset[0] < 0 or exclude_offset[1] < 0:
        raise ValueError("Must be positive `exclude_offset` arg.")

    # Extract callstack.
    if exclude_offset != 0:
        traceback_info = list(reversed(traceback.extract_stack()[exclude_offset[0]:-exclude_offset[1]]))
    else:
        traceback_info = list(reversed(traceback.extract_stack()))
    
    return traceback_info


def get_all_frames(exclude_offset:tuple=(1,2)) -> list:
    """
    Get all frames.

    Args:
        exclude_offset (tuple): Start and end offset to exclude from traceback, must be positive, default = 2

    Returns:
        list[frame]: List of frames (from top to bottom of callstack).
    """
    # Check `exclude_offset` argument.
    if type(exclude_offset) is not tuple and len(exclude_offset) != 2:
        raise ValueError("Please provide tuple of length 2 for `exclude_offset` arg.")
    if exclude_offset[0] < 0 or exclude_offset[1] < 0:
        raise ValueError("Must be positive `exclude_offset` arg.")
    
    # Creating list of frames.
    frames = []

    # Initial frame.
    initial_frame = inspect.currentframe()
    frames.append(initial_frame)

    # Get previous frame.
    previous_frame = initial_frame.f_back

    # Add all previous frames to list of frames.
    while previous_frame is not None:
        frames.append(previous_frame)
        previous_frame = previous_frame.f_back
    
    # Reverse frames.
    if exclude_offset:
        frames = frames[exclude_offset[1]:-exclude_offset[0]]

    return frames
    

def display_call_stack():
    """
    Displaying call stack.
    """
    # Get traceback info and frames.
    traceback_info = get_traceback_info()
    frames = get_all_frames()

    # Reverse for printing.
    rev_traceback_info = list(reversed(traceback_info))
    rev_frames =  list(reversed(frames))

    # Output strings.
    outputStrings = []

    # Add callstack depth message.
    outputStrings.append('The call stack is %s call(s) deep:' % (len(frames)))

    if len(frames) == 0:
        # Message for calling from global scope.
        outputStrings.append('  showcallstack() was called in the global scope and not in a function call.')
    else:

        outputStrings.append('(Here is the "bottom" of the call stack.)')
        for i, v in enumerate(rev_traceback_info):
            outputStrings.append('Local variables of call to %s():' % (v.name))

            if rev_frames[i].f_locals is not None:
                for localVarName, localVarValue in rev_frames[i].f_locals.items():
                    outputStrings.append('  ' + localVarName + ' (type: ' + type(localVarValue).__qualname__ + ') == ' + repr(localVarValue))

        outputStrings.append('(Here is the "top" of the call stack.)')
    outputStrings.append('')

    # Filter the global variables.
    reportedGlobalVars = {}
    for k, v in rev_frames[0].f_globals.items():
        if k.startswith('__') or inspect.isfunction(v) or inspect.ismodule(v) or inspect.isclass(v):
            # Skip variables that are functions, modules, classes, etc:
            continue
        reportedGlobalVars[k] = (type(v).__qualname__, v)

    outputStrings.append('Global variables:')
    if len(reportedGlobalVars) == 0:
        outputStrings.append('  No global variables.')
    else:
        for k in sorted(list(reportedGlobalVars.keys())):
            varTypeAsStr = reportedGlobalVars[k][0]
            varValueAsStr = repr(reportedGlobalVars[k][1])
            outputStrings.append('  ' + k + ' (type: ' + varTypeAsStr + ') == ' + varValueAsStr)

    outputStrings.append('')
    print('\n'.join(outputStrings))

    
# - - - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":

    # Define test func.
    def a():
        varA = 42
        display_call_stack()
        
    def b():
        varB = 50
        a()

    b()
    
