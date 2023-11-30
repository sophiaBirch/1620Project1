import unittest
from tkinter import Tk
from gui import Gui

import unittest
import os
from tkinter import Tk
from gui import Gui

class TestGui(unittest.TestCase):

    def setUp(self) -> None:
        '''
            Sets up the tester Gui class
        '''
        self.root = Tk()
        self.gui = Gui(self.root)
        self.csv_file = 'votes.csv'

        # Ensure a clean state for CSV file
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def tearDown(self) -> None:
        '''
            Destroys the tester Gui class
        '''
        self.root.destroy()
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def test_initial_values(self) -> None:
        '''
            Tests that the initial values are set up correctly
        '''
        self.assertEqual(self.gui.john_votes, 0)
        self.assertEqual(self.gui.jane_votes, 0)

    def test_require_name_for_voting(self) -> None:
        '''
            Tests that a name is required before voting
        '''
        self.gui.vote_entry.insert(0, '3')
        self.gui.vote_for_john()
        self.assertNotEqual(self.gui.status_label['text'], "Vote recorded. Thank you!")

    def test_prevent_duplicate_voting(self) -> None:
        '''
            Tests that a user cannot vote more than once
        '''
        self.gui.name_entry.insert(0, 'Alice')
        self.gui.vote_entry.insert(0, '1')
        self.gui.vote_for_john()
        self.assertEqual(self.gui.status_label['text'], "Vote recorded. Thank you!")

        self.gui.vote_for_jane()
        self.assertEqual(self.gui.status_label['text'], "You have already voted.")

    def test_csv_file_update(self) -> None:
        '''
            Test if the CSV file is updated with a new vote
        '''
        self.gui.name_entry.insert(0, 'Bob')
        self.gui.vote_entry.insert(0, '1')
        self.gui.vote_for_jane()

        # Check if the CSV file contains the expected entry
        with open(self.csv_file, 'r') as file:
            last_line = file.readlines()[-1]
            self.assertIn('Bob,Jane', last_line)

    def test_vote_for_john(self) -> None:
        '''
            Tests that the "vote john" functionality is working
        '''
        self.gui.name_entry.insert(0, "Sophia")
        self.gui.vote_entry.insert(0, '3')  # Simulate entering 3 votes
        self.gui.vote_for_john()
        self.assertEqual(self.gui.john_votes, 3)
        self.assertEqual(self.gui.vote_count_label['text'], "John - 3 Jane - 0 Total - 3")

    def test_vote_for_jane(self) -> None:
        '''
            Tests that the "vote jane" functionality is working
        '''
        self.gui.name_entry.insert(0, "Sophia Birch")
        self.gui.vote_entry.insert(0, '3') # Simulate entering 3 votes
        self.gui.vote_for_jane()
        self.assertEqual(self.gui.jane_votes, 3)
        self.assertEqual(self.gui.vote_count_label['text'], "John - 0 Jane - 3 Total - 3")

    def test_invalid_input(self) -> None:
        '''
            Simulate entering a non-integer
        '''
        self.gui.name_entry.insert(0,"Sophia")
        self.gui.vote_entry.insert(0, 'abc') 
        self.gui.vote_for_john()
        self.assertEqual(self.gui.incorrect_value_label['text'], "Please enter a numerical value")

    def test_negative_input(self) -> None:
        '''
            Simulates entering a negative number
        '''
        self.gui.name_entry.insert(0,"Sophia")
        self.gui.vote_entry.insert(0, -32)
        self.gui.vote_for_jane()
        self.assertEqual(self.gui.incorrect_value_label['text'], "Please enter a positive number")

if __name__ == "__main__":
    unittest.main()