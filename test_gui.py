import unittest
from tkinter import Tk
from gui import Gui

class TestGui(unittest.TestCase):

    def setUp(self) -> None:
        '''
            Sets up the tester Gui class
        '''
        self.root = Tk()
        self.gui = Gui(self.root)

    def tearDown(self) -> None:
        '''
            Destroys the tester Gui class
        '''
        self.root.destroy()

    def test_initial_values(self) -> None:
        '''
            Tests that the initial values are set up correctly
        '''
        self.assertEqual(self.gui.john_votes, 0)
        self.assertEqual(self.gui.jane_votes, 0)

    def test_vote_for_john(self) -> None:
        '''
            Tests that the "vote john" functionality is working
        '''
        self.gui.vote_entry.insert(0, '3')  # Simulate entering 3 votes
        self.gui.vote_for_john()
        self.assertEqual(self.gui.john_votes, 3)
        self.assertEqual(self.gui.vote_count_label['text'], "John - 3 Jane - 0 Total - 3")

    def test_vote_for_jane(self) -> None:
        '''
            Tests that the "vote jane" functionality is working
        '''
        self.gui.vote_entry.insert(0, '3') # Simulate entering 3 votes
        self.gui.vote_for_jane()
        self.assertEqual(self.gui.jane_votes, 3)
        self.assertEqual(self.gui.vote_count_label['text'], "John - 0 Jane - 3 Total - 3")

    def test_invalid_input(self) -> None:
        '''
            Simulate entering a non-integer
        '''
        self.gui.vote_entry.insert(0, 'abc') 
        self.gui.vote_for_john()
        self.assertEqual(self.gui.incorrect_value_label['text'], "Please enter a numerical value")

    def test_negative_input(self) -> None:
        '''
            Simulates entering a negative number
        '''
        self.gui.vote_entry.insert(0, -32)
        self.gui.vote_for_jane()
        self.assertEqual(self.gui.incorrect_value_label['text'], "Please enter a positive number")

if __name__ == "__main__":
    unittest.main()