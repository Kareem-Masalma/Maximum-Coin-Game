from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
from Coins_Game import Coins

"""
    This class is for the Graphical User Interface, I used Tkinter library to create the GUI and Pillow library to
    manipulate the images. 
    The main window will have two buttons, play button and quit button, the quit button will
    close the program, the play button will take us to the next interface with four buttons.
    The buttons for the use ti choose the data source, Random data will allow the user to enter the number of coins
    which is the length of our list. 
    The manual will allow user to enter the data manually. 
    The file button will read data from a text file, the text file have the data on the following order:
    number of coins
    values of coins separated by space
"""


class GUI:

    def __init__(self):
        # The main window
        self.main_window = Tk()
        self.custom_window(self.main_window, 626, 352)
        self.bg = Image.open('Main_Theme.jpeg')
        self.bg = self.bg.resize((626, 352))
        self.main_image = ImageTk.PhotoImage(self.bg)
        self.main_label = Label(self.main_window, image=self.main_image)
        self.main_label.place(x=0, y=0, relwidth=1, relheight=1)

        # The play button which starts the game and goes to the next window
        self.button_play = Button(self.main_window, text='Play', font=('Arial', 12), fg='#000', bg='#efb539',
                                  activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                                  command=self.play)
        self.button_play.place(relx=0.5, rely=0.4, anchor=CENTER)

        # The quit button which closes the program
        self.button_quit = Button(self.main_window, text='Quit', font=('Arial', 12), fg='#000', bg='#efb539',
                                  activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                                  command=self.main_window.quit)
        self.button_quit.place(relx=0.5, rely=0.5, anchor=CENTER)

        # The bind method is used to connect the button with the hover and leave functions to change color when hover
        self.button_quit.bind("<Enter>", lambda button: self.button_hover("<Enter>", self.button_quit))
        self.button_quit.bind("<Leave>", lambda button: self.button_leave("<Leave>", self.button_quit))
        self.button_play.bind("<Enter>", lambda button: self.button_hover("<Enter>", self.button_play))
        self.button_play.bind("<Leave>", lambda button: self.button_leave("<Leave>", self.button_play))
        self.main_window.mainloop()

    # This function is to change the color of the button when the mouse hover on it
    def button_hover(self, event, button):
        button.config(bg='#fed570', fg='#000')

    # This function is to change the color of the button when the mouse leave it
    def button_leave(self, event, button):
        button.config(fg='#000', bg='#efb539')

    # This function is to customize the window with the given width and height
    def custom_window(self, window, x, y):
        window.geometry(f'{x}x{y}')
        window.title('Coin Game')
        window.resizable(False, False)
        icon = PhotoImage(file='coin.png')
        window.iconphoto(False, icon)

    # This function is the action of the play button. It will show the three ways to enter the data and quit button.
    def play(self, first=True):

        # Remove the button
        self.button_play.place_forget()

        # Create the random button which takes the user to the game window which allows the user
        # to enter the number of coins
        button_random = Button(self.main_window, text='Random Data', font=('Arial', 12), fg='#000', bg='#efb539',
                               activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                               command=lambda: game('random'))
        button_random.place(relx=0.5, rely=0.3, anchor=CENTER)

        # Create the manual button which takes the user to the game window which allows the use
        # to enter the data manually
        button_manual = Button(self.main_window, text='Manual Data', font=('Arial', 12), fg='#000', bg='#efb539',
                               activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                               command=lambda: game('manual'))
        button_manual.place(relx=0.5, rely=0.4, anchor=CENTER)

        # Create the file button which takes the user to the game window and reads the data from the file
        button_file = Button(self.main_window, text='File Data', font=('Arial', 12), fg='#000', bg='#efb539',
                             activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                             command=lambda: game('file'))
        button_file.place(relx=0.5, rely=0.5, anchor=CENTER)

        # The quit button
        self.button_quit.place(relx=0.5, rely=0.6, anchor=CENTER)

        # We used the bind method to connect the button with the hover and leave functions to change color when hover
        button_random.bind("<Enter>", lambda button: self.button_hover("<Enter>", button_random))
        button_random.bind("<Leave>", lambda button: self.button_leave("<Leave>", button_random))
        button_manual.bind("<Enter>", lambda button: self.button_hover("<Enter>", button_manual))
        button_manual.bind("<Leave>", lambda button: self.button_leave("<Leave>", button_manual))
        button_file.bind("<Enter>", lambda button: self.button_hover("<Enter>", button_file))
        button_file.bind("<Leave>", lambda button: self.button_leave("<Leave>", button_file))

        # This function for the game to start with the method we have chosen to get the data with
        def game(game_type):
            # Create the game window
            self.main_window.destroy()

            # The game window that contains all the widgets
            game_window = Tk()
            self.custom_window(game_window, 1000, 700)
            bg = Image.open('background.jpg')
            bg = bg.resize((1000, 700))
            game_image = ImageTk.PhotoImage(bg)
            game_label = Label(game_window, image=game_image)
            game_label.place(x=0, y=0, relwidth=1, relheight=1)

            # The player image
            player_image = Image.open('player.png')
            player_image = player_image.resize((100, 100))
            player = ImageTk.PhotoImage(player_image)
            player_label = Label(game_window, image=player)
            player_label.place(relx=0.3, rely=0.5, anchor=CENTER)
            player_name = Label(game_window, text='Player', font=('Arial', 12), fg='#000')
            player_name.place(relx=0.3, rely=0.6, anchor=CENTER)

            computer_image = Image.open('computer.jpeg')
            computer_image = computer_image.resize((100, 100))
            computer = ImageTk.PhotoImage(computer_image)
            computer_label = Label(game_window, image=computer)
            computer_label.place(relx=0.7, rely=0.5, anchor=CENTER)
            computer_name = Label(game_window, text='Computer', font=('Arial', 12), fg='#000')
            computer_name.place(relx=0.7, rely=0.6, anchor=CENTER)

            # The back button to go back to the main window
            back_button = Button(game_window, text='<Back', font=('Arial', 10), fg='#000', bg='#efb539',
                                 activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                                 command=lambda: back(game_window))
            back_button.place(relx=0.1, rely=0.1, anchor=CENTER)
            back_button.bind("<Enter>", lambda button: self.button_hover("<Enter>", back_button))
            back_button.bind("<Leave>", lambda button: self.button_leave("<Leave>", back_button))

            # Check which method is used for the data
            if game_type == 'random':
                label = Label(game_window, text='Enter the number of coins:', font=('Arial', 12), fg='#000')
                label.place(relx=0.4, rely=0.2, anchor=CENTER)
                entry = Entry(game_window, font=('Arial', 12), width=10, bg='#F5F5DC')
                entry.place(relx=0.55, rely=0.2, anchor=CENTER)
                # The start button to get the number of coins and start the game
                start = Button(game_window, text='Start', font=('Arial', 8), fg='#000', bg='#efb539',
                               activebackground='#fed570', activeforeground='#000', relief=FLAT, width=8, height=1,
                               command=lambda: start_random(game_window, entry))
                start.place(relx=0.65, rely=0.2, anchor=CENTER)
                entry.bind("<Return>", lambda event: start_random(game_window, entry))
                start.bind("<Enter>", lambda button: self.button_hover("<Enter>", start))
                start.bind("<Leave>", lambda button: self.button_leave("<Leave>", start))
            elif game_type == 'manual':
                label = Label(game_window, text='Enter the values of the coins separated by space:', font=('Arial', 12),
                              fg='#000')
                label.place(relx=0.5, rely=0.2, anchor=CENTER)
                entry = Entry(game_window, font=('Arial', 12), width=50, bg='#F5F5DC')
                entry.place(relx=0.5, rely=0.3, anchor=CENTER)
                start = Button(game_window, text='Start', font=('Arial', 8), fg='#000', bg='#efb539',
                               activebackground='#fed570', activeforeground='#000', relief=FLAT, width=8, height=1,
                               command=lambda: start_manual(game_window, entry))
                start.place(relx=0.5, rely=0.4, anchor=CENTER)
                entry.bind("<Return>", lambda event: start_manual(game_window, entry))
                start.bind("<Enter>", lambda button: self.button_hover("<Enter>", start))
                start.bind("<Leave>", lambda button: self.button_leave("<Leave>", start))
            else:
                with open('data.txt', 'r') as file:
                    lines = file.readlines()
                    coins = []
                    for line in lines:
                        coins.append(list(map(int, line.strip().split())))

                    def calculate(i):
                        current_coins = coins[i]
                        game_class = Coins(current_coins)
                        game_class.maximum_money()
                        table = game_class.get_table()
                        result = table[0][-1]

                        list_label = Label(game_window, text=f'The coins are: {current_coins}', font=('Arial', 12),
                                           fg='#000')

                        result_label = Label(game_window, text=f'The maximum money you can win is: {result}',
                                             font=('Arial', 12), fg='#000')
                        list_label.place(relx=0.5, rely=0.2, anchor=CENTER)
                        result_label.place(relx=0.5, rely=0.25, anchor=CENTER)

                        button_next = Button(game_window, text='>>', font=('Arial', 12), fg='#000', bg='#efb539',
                                             activebackground='#fed570', activeforeground='#000', relief=FLAT, width=5,
                                             height=1, command=lambda: next_line(i))
                        button_next.place(relx=0.6, rely=0.3, anchor=CENTER)

                        button_pre = Button(game_window, text='<<', font=('Arial', 12), fg='#000', bg='#efb539',
                                            activebackground='#fed570', activeforeground='#000', relief=FLAT, width=5,
                                            height=1, command=lambda: pre(i))
                        button_pre.place(relx=0.4, rely=0.3, anchor=CENTER)

                        button_table = Button(game_window, text='Show Table', font=('Arial', 12), fg='#000',
                                              bg='#efb539',
                                              activebackground='#fed570', activeforeground='#000', relief=FLAT,
                                              width=10,
                                              height=1, command=lambda: show_table(table))
                        button_table.place(relx=0.5, rely=0.3, anchor=CENTER)

                        moves_button = Button(game_window, text='Show Moves', font=('Arial', 12), fg='#000',
                                              bg='#efb539', activebackground='#fed570', activeforeground='#000',
                                              relief=FLAT, width=10, height=1,
                                              command=lambda: show_moves(game_class.get_moves()))
                        moves_button.place(relx=0.5, rely=0.35, anchor=CENTER)

                        def pre(pre_index):
                            pre_index -= 1
                            if pre_index < 0:
                                pre_index = len(coins) - 1
                            result_label.config(text='')
                            list_label.config(text='')
                            calculate(pre_index)

                        def next_line(next_index):
                            next_index += 1
                            if next_index == len(coins):
                                next_index = 0
                            result_label.config(text='')
                            list_label.config(text='')
                            calculate(next_index)

                        button_next.bind("<Enter>", lambda button: self.button_hover("<Enter>", button_next))
                        button_next.bind("<Leave>", lambda button: self.button_leave("<Leave>", button_next))
                        button_table.bind("<Enter>", lambda button: self.button_hover("<Enter>", button_table))
                        button_table.bind("<Leave>", lambda button: self.button_leave("<Leave>", button_table))
                        button_pre.bind("<Enter>", lambda button: self.button_hover("<Enter>", button_pre))
                        button_pre.bind("<Leave>", lambda button: self.button_leave("<Leave>", button_pre))

                    index = 0
                    calculate(index)

            game_window.mainloop()

        def back(pre_window):
            pre_window.destroy()
            self.main_window = Tk()
            self.custom_window(self.main_window, 626, 352)
            self.bg = Image.open('Main_Theme.jpeg')
            self.bg = self.bg.resize((626, 352))
            self.main_image = ImageTk.PhotoImage(self.bg)
            self.main_label = Label(self.main_window, image=self.main_image)
            self.main_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.button_play = Button(self.main_window, text='Play', font=('Arial', 12), fg='#000', bg='#efb539',
                                      activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                                      height=1,
                                      command=self.play)
            self.button_play.place(relx=0.5, rely=0.4, anchor=CENTER)
            self.button_quit = Button(self.main_window, text='Quit', font=('Arial', 12), fg='#000', bg='#efb539',
                                      activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                                      height=1,
                                      command=lambda: self.main_window.destroy())
            self.button_quit.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.button_quit.bind("<Enter>", lambda button: self.button_hover("<Enter>", self.button_quit))
            self.button_quit.bind("<Leave>", lambda button: self.button_leave("<Leave>", self.button_quit))
            self.button_play.bind("<Enter>", lambda button: self.button_hover("<Enter>", self.button_play))
            self.button_play.bind("<Leave>", lambda button: self.button_leave("<Leave>", self.button_play))
            self.main_window.mainloop()

        def start_random(window, entry):
            try:
                # Get the number of coins from the user
                coins_number = int(entry.get())
                # Check if the number is positive and even
                if coins_number <= 0 or coins_number % 2 != 0:
                    raise ValueError

                # Clear the text field
                entry.delete(0, END)
                # Create a list with random values
                coins = [random.randint(1, 100) for _ in range(coins_number)]
                # Create the game object and get the table and the value of the maximum money
                game_class = Coins(coins)
                game_class.maximum_money()
                table = game_class.get_table()
                moves = game_class.get_moves()
                result = table[0][-1]

                result_label = Label(window, text=f'The maximum money you can win is: {result}', font=('Arial', 12),
                                     fg='#000')
                result_label.place(relx=0.5, rely=0.3, anchor=CENTER)

                # This button will show the moves of the player
                moves_button = Button(window, text='Show Moves', font=('Arial', 12), fg='#000',
                                      bg='#efb539',
                                      activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                                      height=1, command=lambda: show_moves(moves))
                moves_button.place(relx=0.5, rely=0.45, anchor=CENTER)

                # This button will pop a new table with the values of the table
                button_table = Button(window, text='Show Table', font=('Arial', 12), fg='#000', bg='#efb539',
                                      activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                                      height=1, command=lambda: show_table(table))
                button_table.place(relx=0.5, rely=0.4, anchor=CENTER)

                # We used the bind method to connect the button with the hover and leave functions to change
                # color when hover
                button_table.bind("<Enter>", lambda button: self.button_hover("<Enter>", button_table))
                button_table.bind("<Leave>", lambda button: self.button_leave("<Leave>", button_table))
                moves_button.bind("<Enter>", lambda button: self.button_hover("<Enter>", moves_button))
                moves_button.bind("<Leave>", lambda button: self.button_leave("<Leave>", moves_button))

            except ValueError:
                messagebox.showerror('Error', 'Please enter a even and positive number')
                entry.delete(0, END)

        def start_manual(window, entry):
            try:
                # Get the number of coins from the user
                coins = []

                # Split the values by space
                coins_string = entry.get().split()
                if len(coins_string) == 0:
                    raise ValueError

                for coin in coins_string:
                    value = int(coin)
                    if value <= 0:
                        raise ValueError
                    coins.append(value)

                # Check if the number of coins is even
                if len(coins) % 2 != 0:
                    raise ValueError

                # Clear the text field

                entry.delete(0, END)

                # Create the game object and get the table and the value of the maximum money
                game_class = Coins(coins)
                game_class.maximum_money()
                table = game_class.get_table()
                result = table[0][-1]

                result_label = Label(window, text=f'The maximum money you can win is: {result}', font=('Arial', 12),
                                     fg='#000')
                result_label.place(relx=0.5, rely=0.5, anchor=CENTER)

                # This button will show the moves of the player
                moves_button = Button(window, text='Show Moves', font=('Arial', 12), fg='#000',
                                      bg='#efb539',
                                      activebackground='#fed570', activeforeground='#000', relief=FLAT,
                                      width=10,
                                      height=1, command=lambda: show_moves(game_class.get_moves()))
                moves_button.place(relx=0.5, rely=0.65, anchor=CENTER)

                # This button will pop a new table with the values of the table
                button_table = Button(window, text='Show Table', font=('Arial', 12), fg='#000', bg='#efb539',
                                      activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                                      height=1, command=lambda: show_table(table))
                button_table.place(relx=0.5, rely=0.6, anchor=CENTER)

                # We used the bind method to connect the button with the hover and leave functions to change
                # color when hover
                button_table.bind("<Enter>", lambda button: self.button_hover("<Enter>", button_table))
                button_table.bind("<Leave>", lambda button: self.button_leave("<Leave>", button_table))
                moves_button.bind("<Enter>", lambda button: self.button_hover("<Enter>", moves_button))
                moves_button.bind("<Leave>", lambda button: self.button_leave("<Leave>", moves_button))

            except ValueError:
                messagebox.showerror('Error', 'Please enter a even and positive number')
                entry.delete(0, END)

        # This function is to pop a new window with the dynamic table
        def show_table(table):
            table_window = Tk()
            table_window.geometry('1000x500')
            table_window.title('Dynamic Table')
            table_window.resizable(False, False)
            text = Text(table_window, font=('Courier New', 12))

            # Insert the values of the table in the text area separated by spaces
            text.insert('end', '  '.join(f'{i:5}' for i in range(len(table))) + '\n')

            # Loop through the table and insert the values in the text area
            for i, row in zip(range(len(table)), table):
                # Format a string with the values of the row separated by spaces
                row_list = '  '.join(f'{coin:5}' for coin in row)
                # Insert the string in the text area
                text.insert('end', str(i) + row_list + '\n')

            text.pack()
            text.config(state=DISABLED)

            table_window.mainloop()

        # This function is to pop a new window with the coins the player chose to get to the final answer
        def show_moves(moves):
            moves_window = Tk()
            moves_window.geometry('500x200')
            moves_window.title('Coins')
            moves_window.resizable(False, False)
            text = Text(moves_window, font=('Arial', 12))

            text.insert('end', 'player Coins' + '\n')
            text.insert('end', ', '.join(str(move) for move in moves) + '\n')

            text.pack(padx=10, pady=10)
            text.config(state=DISABLED)

            moves_window.mainloop()
