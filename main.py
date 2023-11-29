from gui import *

def main() -> None:
    '''
        Generates a GUI of fixed size for a voting app
    '''
    window = Tk()
    window.title("Project Part 1 - Voting App")
    window.geometry('330x240')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()
    
if __name__ == "__main__":
    main()