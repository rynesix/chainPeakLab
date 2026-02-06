# test_chainpeak.py
"""
Tests for chainPeak module.
"""

import unittest
from chainpeak import chainPeak

class TestchainPeak(unittest.TestCase):
    """Test cases for chainPeak class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = chainPeak()
        self.assertIsInstance(instance, chainPeak)
        
    def test_run_method(self):
        """Test the run method."""
        instance = chainPeak()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
