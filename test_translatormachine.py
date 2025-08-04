# test_translatormachine.py
"""
Tests for TranslatorMachine module.
"""

import unittest
from translatormachine import TranslatorMachine

class TestTranslatorMachine(unittest.TestCase):
    """Test cases for TranslatorMachine class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TranslatorMachine()
        self.assertIsInstance(instance, TranslatorMachine)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TranslatorMachine()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
