import sys
from io import StringIO
import pytest


def test_output_something():
    """Test that output_something.py prints 'foo bar'."""
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Execute the script
    exec(open('output_something.py').read())
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check output
    assert captured_output.getvalue().strip() == 'foo bar'
