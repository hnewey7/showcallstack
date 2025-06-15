"""
Module for testing `ShowCallStack` class.    
"""

import pytest

from src.showcallstack import ShowCallStack

# - - - - - - - - - - - - - - - - - - - - -

def test_init():
    """
    Test initialisation of `ShowCallStack` class.
    """
    # Init
    show_call_stack = ShowCallStack()
    assert show_call_stack.traceback_info == []

def test_default_get_traceback_info():
    """
    Test method `get_traceback_info`.
    """
    # Init
    show_call_stack = ShowCallStack()
    assert show_call_stack.traceback_info == []

    # Get reference traceback info.
    reference_traceback_info = show_call_stack.get_traceback_info(0)

    # Get traceback for default args.
    default_args_traceback_info = show_call_stack.get_traceback_info(2)
    assert len(default_args_traceback_info) == len(reference_traceback_info) - 2