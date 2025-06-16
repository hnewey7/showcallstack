"""
Module for testing showcallstack functions.    
"""

from src.showcallstack import get_all_frames, get_traceback_info, display_call_stack

# - - - - - - - - - - - - - - - - - - - - -

def test_default_get_traceback_info():
    """
    Test function `get_traceback_info`.
    """
    # Get reference traceback info.
    reference_traceback_info = get_traceback_info()
    
    # Defining test function.
    def a():
        # Get traceback.
        traceback_info = get_traceback_info()
        assert len(traceback_info) == len(reference_traceback_info) + 1
    a()

def test_get_all_frames():
    """
    Test function `get_all_frames`.
    """
    # Get all frames.
    reference_frames = get_all_frames()

    # Defining test function.
    def a():
        # Get frames.
        frames = get_all_frames()
        assert len(frames) == len(reference_frames) + 1
    a()