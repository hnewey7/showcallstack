"""
Module for defining callstack functions.

Created on Sunday 15th June 2025.
@author: Harry New

"""
import traceback
import inspect

# - - - - - - - - - - - - - - - - - - - - -

def get_traceback_info(exclude_offset:int=2) -> list:
    """
    Get trackback info.

    Args:
        exclude_offset (int): Offset to exclude from traceback, must be positive, default = 2
    
    Returns:
        list: List of tracebacks.
    """
    # Check `exclude_offset` argument.
    if exclude_offset < 0:
        raise ValueError("Must be positive offset.")

    # Extract callstack.
    if exclude_offset != 0:
        traceback_info = list(reversed(traceback.extract_stack()[:-exclude_offset]))
    else:
        traceback_info = list(reversed(traceback.extract_stack()))
    
    return traceback_info


def get_all_frames():
    """
    Get all frames.

    Returns:
        list[frame]: List of frames.
    """
    # Creating list of frames.
    frames = []

    # Initial previous frame (excludes call to `get_all_frames`).
    initial_frame = inspect.currentframe().f_back

    # Get previous frame.
    previous_frame = initial_frame.f_back

    # Add all previous frames to list of frames.
    while previous_frame is not None:
        frames.append(previous_frame)
        previous_frame = previous_frame.f_back
    
    return frames
    

def display_call_stack():
    """
    Displaying call stack.
    """
    # Get frames.
    frames = get_all_frames()

    # Display callstack depth message.
    print(f'The callstack is {len(frames)} call(s) deep:')

    
# - - - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":

    # Define test func.
    def a():
        print(get_all_frames())
        
    def b():
        a()

    b()
    
