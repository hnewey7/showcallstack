"""
Module for defining ShowCallStack class.

Created on Sunday 15th June 2025.
@author: Harry New

"""
import traceback
import inspect

# - - - - - - - - - - - - - - - - - - - - -

class ShowCallStack:
    def __init__(self):
        """
        Class for extracting callstack, and displaying results.
        """

    def get_traceback_info(self,exclude_offset:int=2) -> list:
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

    def get_all_frames(self):
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

    
# - - - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    # Show call stack.
    global call_stack
    call_stack = ShowCallStack()

    # Define test func.
    def a():
        call_stack.get_all_frames()
        print(call_stack.frames)

    def b():
        a()

    b()
    
