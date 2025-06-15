"""
Module for defining ShowCallStack class.

Created on Sunday 15th June 2025.
@author: Harry New

"""
import traceback

# - - - - - - - - - - - - - - - - - - - - -

class ShowCallStack:
    def __init__(self):
        """
        Class for extracting callstack, and displaying results.
        """
        self.traceback_info = []

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
            self.traceback_info = list(reversed(traceback.extract_stack()[:-exclude_offset]))
        else:
            self.traceback_info = list(reversed(traceback.extract_stack()))
        
        return self.traceback_info

# - - - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    # Show call stack.
    global call_stack
    call_stack = ShowCallStack()
    call_stack.get_traceback_info(0)

    # Define test func.
    def a():
        call_stack.get_traceback_info(0)

    def b():
        a()

    b()
    
