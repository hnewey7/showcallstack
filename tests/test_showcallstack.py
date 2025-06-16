"""
Module for testing `ShowCallStack` class.    
"""

import pytest

from src.showcallstack import ShowCallStack

# - - - - - - - - - - - - - - - - - - - - -

def test_init():
    """
    Test initialisation of `ShowCallStack` class.

    Returns:
        ShowCallStack
    """
    # Init
    show_call_stack = ShowCallStack()
    assert show_call_stack

def test_default_get_traceback_info():
    """
    Test method `get_traceback_info`.
    """
    # Init
    show_call_stack = ShowCallStack()

    # Get reference traceback info.
    reference_traceback_info = show_call_stack.get_traceback_info(0)
    
    # Defining test function.
    def a():
        # Get traceback.
        traceback_info = show_call_stack.get_traceback_info(0)
        assert len(traceback_info) == len(reference_traceback_info) + 1
    a()

def test_get_all_frames():
    """
    Test method `get_all_frames`.
    """
    # Init
    show_call_stack = ShowCallStack()

    # Get all frames.
    reference_frames = show_call_stack.get_all_frames()

    # Defining test function.
    def a():
        # Get frames.
        frames = show_call_stack.get_all_frames()
        assert len(frames) == len(reference_frames) + 1
    a()