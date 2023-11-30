from tkinter import *
import csv
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
        self.voted_users = set()

        self.vote_count_label = Label(base, text="John - 0 Jane - 0 Total - 0")
        self.name_label = Label(base, text="Your Name:")
        self.name_entry = Entry(base)
        self.vote_label = Label(base, text="Num. votes:")
        self.vote_entry = Entry(base)

        self.status_label = Label(base, text="")
        self.vote_john_button = Button(base, text="Add votes to John", command=self.vote_for_john)
        self.vote_jane_button = Button(base, text="Add votes to Jane", command=self.vote_for_jane)
        self.exit_button = Button(base, text="Exit", command=self.exit_app)
        self.incorrect_value_label = Label(base, text = "")
        
        self.vote_count_label.pack()
        self.name_label.pack()
        self.name_entry.pack()
        self.vote_label.pack()
        self.vote_entry.pack()
        self.vote_john_button.pack()
        self.vote_jane_button.pack()
        self.status_label.pack()
        self.exit_button.pack()
        self.incorrect_value_label.pack()

    def vote_for_john(self) -> None:
        '''
            Adds votes to John and updates the vote count label
        '''
        if self.check_and_save_vote("John"):
            votes = self.get_number_of_votes()
            self.add_votes_to_john(votes)
            self.update_vote_count()

    def vote_for_jane(self) -> None:
        '''
            Adds votes to Jane and updates the vote count label
        '''
        if self.check_and_save_vote("Jane"):
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

    def check_and_save_vote(self, candidate) -> bool:
        '''
            Check if the user has already voted, save vote to CSV
        '''
        name = self.name_entry.get().strip()
        if not name:
            self.status_label.config(text="Please enter your name.")
            return False

        if name in self.voted_users:
            self.status_label.config(text="You have already voted.")
            return False

        self.voted_users.add(name)
        self.save_vote_to_csv(name, candidate)
        self.status_label.config(text="Vote recorded. Thank you!")
        return True

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

    def save_vote_to_csv(self, name, candidate) -> None:
        '''
            Save name and vote to csv file
        '''
        with open('votes.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, candidate, self.get_number_of_votes()])


