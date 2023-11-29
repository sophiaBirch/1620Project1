from tkinter import *

##a graphical user interface that sits in a window (base)
class Gui():

    def __init__(self, base) -> None:
        '''
            :param: base class (window in which the GUI sits)

            Contains the GUI elements and functions to update GUI with user input
        '''
        self.base = base

        self.john_votes: int = 0
        self.jane_votes: int = 0

        self.vote_count_label = Label(base, text="John - 0 Jane - 0 Total - 0")
        self.vote_entry = Entry(base)
        self.vote_john_button = Button(base, text="Add votes to John", command=self.vote_for_john)
        self.vote_jane_button = Button(base, text="Add votes to Jane", command=self.vote_for_jane)
        self.exit_button = Button(base, text="Exit", command=self.exit_app)
        self.incorrect_value_label = Label(base, text = "")

        self.vote_count_label.pack()
        self.vote_entry.pack()
        self.vote_john_button.pack()
        self.vote_jane_button.pack()
        self.exit_button.pack()
        self.incorrect_value_label.pack()

    def vote_for_john(self) -> None:
        '''
            Adds votes to John and updates the vote count label
        '''
        votes = self.get_number_of_votes()
        self.add_votes_to_john(votes)
        self.update_vote_count()

    def vote_for_jane(self) -> None:
        '''
            Adds votes to Jane and updates the vote count label
        '''
        votes = self.get_number_of_votes()
        self.add_votes_to_jane(votes)
        self.update_vote_count()

    def add_votes_to_john(self, votes) -> None:
        '''
            Increases amount of votes for john
        '''
        self.john_votes += votes

    def add_votes_to_jane(self, votes) -> None:
        '''
            Increases amount of votes for jane
        '''
        self.jane_votes += votes

    def get_vote_count(self) -> int:
        '''
            :return: tuple with number of john and jane votes. 

            gets the number of votes for john and jane
        '''
        return self.john_votes, self.jane_votes

    def update_vote_count(self) -> None:

        '''
            configures the vote count label with the number of votes for each candidate
        '''
        john, jane = self.get_vote_count()
        self.vote_count_label.config(text=f"John - {john} Jane - {jane} Total - {john + jane}")

    def exit_app(self) -> None:
        '''
            exits the GUI upon button click
        '''
        self.base.destroy()

    def get_number_of_votes(self) -> int:
        '''
            extracts number of votes from text box. Raises a value error if the number cannot be parsed to an int, 
            raises a type error if the number is negative.
        '''
        try:
            votes = int(self.vote_entry.get())

            if votes < 0:
                raise TypeError
                
            self.incorrect_value_label.config(text=f"")
            return votes 
        except ValueError:
            self.incorrect_value_label.config(text=f"Please enter a numerical value")
            return 0
        except TypeError:
            self.incorrect_value_label.config(text=f"Please enter a positive number")
            return 0


