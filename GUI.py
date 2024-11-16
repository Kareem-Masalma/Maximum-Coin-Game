from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
from Coins_Game import Coins
from tkinter import filedialog

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
        self.main_window()

    # This function is to create the main window of the game with two buttons, play and quit. Quit button will close the
    # program and the play button will take us to the next interface to choose the number of players.
    def main_window(self):
        main_window = Tk()
        # Customize the main window with the given width, height and title of the window using the function
        # customize_window
        self.customize_window(main_window, 626, 352, 'Coins Game')
        # Open the image and resize it to fit the window size and convert it to ImageTk
        img = Image.open('Main_Theme.jpeg')
        img = img.resize((626, 352))
        bg = ImageTk.PhotoImage(img)
        label = Label(main_window, image=bg)
        label.place(x=0, y=0)
        # Create the play button and the quit button. The play button will take us to the next interface and the quit
        # button will close the program
        play_button = Button(main_window, text='Play', font=('Arial', 12), fg='#000', bg='#efb539',
                             activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                             command=lambda: self.play(main_window))
        quit_button = Button(main_window, text='Quit', font=('Arial', 12), fg='#000', bg='#efb539',
                             activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                             command=main_window.destroy)
        play_button.place(relx=0.5, rely=0.4, anchor=CENTER)
        quit_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.customize_button(play_button)
        self.customize_button(quit_button)

        main_window.mainloop()

    # This function is to create the play window with two buttons, one player and two players. Pressing any of the
    # buttons will take us to the next interface to choose the data source.
    def play(self, window):
        window.destroy()
        # Creating a new window to present options for the number of players.
        play_window = Tk()
        self.customize_window(play_window, 626, 352, 'Coins Game')
        img = Image.open('Main_Theme.jpeg')
        img = img.resize((626, 352))
        bg = ImageTk.PhotoImage(img)
        label = Label(play_window, image=bg)
        label.place(x=0, y=0)
        one_player_button = Button(play_window, text='One Player', font=('Arial', 12), fg='#000', bg='#efb539',
                                   activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                                   command=lambda: self.game('one_player', play_window))
        two_players_button = Button(play_window, text='Two Players', font=('Arial', 12), fg='#000', bg='#efb539',
                                    activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                                    height=1, command=lambda: self.game('two_players', play_window))
        quit_button = Button(play_window, text='Quit', font=('Arial', 12), fg='#000', bg='#efb539',
                             activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                             command=play_window.destroy)
        one_player_button.place(relx=0.5, rely=0.4, anchor=CENTER)
        two_players_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        quit_button.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.customize_button(one_player_button)
        self.customize_button(two_players_button)
        self.customize_button(quit_button)
        play_window.mainloop()

    # This function is to create the game window with three buttons, random, manual and file.
    def game(self, mode, window):
        window.destroy()
        game_window = Tk()
        self.customize_window(game_window, 626, 352, 'Coins Game')
        img = Image.open('Main_Theme.jpeg')
        img = img.resize((626, 352))
        bg = ImageTk.PhotoImage(img)
        label = Label(game_window, image=bg)
        label.place(x=0, y=0)

        # Random button will take us to the next interface and the data source will be random coins. The action of the
        # button will be to call the random_data function and pass the game_window and the mode(one or two players).
        random_button = Button(game_window, text='Random', font=('Arial', 12), fg='#000', bg='#efb539',
                               activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                               command=lambda: self.random_data(game_window, mode))
        # Manual button will take us to the next interface and the data source will be the user input. The action of the
        # button will be to call the manual_data function and pass the game_window and the mode(one or two players).
        manual_button = Button(game_window, text='Manual', font=('Arial', 12), fg='#000', bg='#efb539',
                               activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                               command=lambda: self.manual_data(game_window, mode))
        # File button will take us to the next interface and the data source will be the data from a text file. The
        # action of the button will be to call the file_data function and pass the game_window and the mode(one or two
        # players).
        file_button = Button(game_window, text='File', font=('Arial', 12), fg='#000', bg='#efb539',
                             activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10, height=1,
                             command=lambda: self.file_data(game_window, mode))
        back_button = Button(game_window, text='Back', font=('Arial', 12), fg='#000', bg='#efb539', relief=FLAT,
                             activebackground='#fed570', activeforeground='#000', width=10, height=1,
                             command=lambda: self.play(game_window))

        random_button.place(relx=0.5, rely=0.4, anchor=CENTER)
        manual_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        file_button.place(relx=0.5, rely=0.6, anchor=CENTER)
        back_button.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.customize_button(random_button)
        self.customize_button(manual_button)
        self.customize_button(file_button)
        self.customize_button(back_button)
        game_window.mainloop()

    # This function is to create the random data window, the user will enter the number of coins, the range of the coins
    # and the data source will be random. The function will take the window and the mode(one or two players) as
    # parameters.
    def random_data(self, window, mode):
        window.destroy()
        random_window = Tk()
        self.customize_window(random_window, 1200, 700, 'Coins Game')
        img = Image.open('Game_theme.png')
        img = img.resize((1200, 700))
        bg = ImageTk.PhotoImage(img)
        label = Label(random_window, image=bg)
        label.place(x=0, y=0)

        # Create the back button to go back to the previous interface and the action of the button will be to call the
        # game function and pass the mode and the random_window.
        back_button = Button(random_window, text='<Back', font=('Arial', 12), fg='#000', bg='#efb539',
                             activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                             height=1, command=lambda: self.game(mode, random_window))
        back_button.place(relx=0.2, rely=0.2, anchor=CENTER)
        self.customize_button(back_button)

        number_of_coins_label = Label(random_window, text='Number of coins:', font=('Arial', 12), bg='#fff7e3',
                                      fg='#000')
        # Create the entry for the user to enter the number of coins
        number_of_coins_entry = Entry(random_window, font=('Arial', 12), bg='#fff', fg='#000')
        from_label = Label(random_window, text='From:', font=('Arial', 12), bg='#fff7e3', fg='#000')
        # Create the entry for the user to enter the from value
        from_entry = Entry(random_window, font=('Arial', 12), bg='#fff', fg='#000', width=5)
        to_label = Label(random_window, text='To:', font=('Arial', 12), bg='#fff7e3', fg='#000')
        # Create the entry for the user to enter the to value
        to_entry = Entry(random_window, font=('Arial', 12), bg='#fff', fg='#000', width=5)
        number_of_coins_label.place(relx=0.45, rely=0.3, anchor=CENTER)
        number_of_coins_entry.place(relx=0.58, rely=0.3, anchor=CENTER)
        from_label.place(relx=0.43, rely=0.35, anchor=CENTER)
        from_entry.place(relx=0.48, rely=0.35, anchor=CENTER)
        to_label.place(relx=0.53, rely=0.35, anchor=CENTER)
        to_entry.place(relx=0.58, rely=0.35, anchor=CENTER)
        number_of_coins_entry.focus()
        # Create the start button to start the game. The action of the button will be to call the start function.
        start_button = Button(random_window, text='Start', font=('Arial', 12), fg='#000', bg='#efb539',
                              activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                              height=1)
        start_button.place(relx=0.5, rely=0.45, anchor=CENTER)
        self.customize_button(start_button)

        # If the mode is one player, the user will enter the number of coins, the range of the coins and the action of
        # the start button will be to call the start function. And the solution will be Dynamic and gives the optimal
        # solution.
        if mode == 'one_player':

            start_button.config(command=lambda: start())

            # Bind the enter key to the start function.
            number_of_coins_entry.bind('<Return>', lambda event: start())
            from_entry.bind('<Return>', lambda event: start())
            to_entry.bind('<Return>', lambda event: start())

            # This function is to start the game, it will take the number of coins, the range of the coins and the call
            # the maximum_money function to get the optimal solution.
            def start():
                try:
                    number_of_coins = int(number_of_coins_entry.get())
                    from_value = int(from_entry.get())
                    to_value = int(to_entry.get())

                    from_entry.delete(0, END)
                    to_entry.delete(0, END)
                    number_of_coins_entry.delete(0, END)

                    # Check if the number of coins is positive and even.
                    if number_of_coins % 2 != 0 or number_of_coins < 0 or from_value < 0 or to_value < 0:
                        raise ValueError

                    # Check if the from value is less than the to value.
                    if from_value > to_value:
                        raise Exception

                    # Generate random coins with the given range and the number of coins.
                    coins = [random.randint(from_value, to_value) for _ in range(number_of_coins)]
                    coins_label = Label(random_window, text='Coins: ' + ' '.join(map(str, coins)), font=('Arial', 12),
                                        bg='#fff7e3', fg='#000')
                    coins_label.place(relx=0.5, rely=0.53, anchor=CENTER)
                    # Create the object of the Coins class and call the maximum_money function to get
                    # the optimal solution.
                    coins_game = Coins(coins)
                    coins_game.maximum_money()
                    max_money_label = Label(random_window, text='Max Money: ' + str(coins_game.dp[0][-1]),
                                            font=('Arial', 12), bg='#fff7e3', fg='#000')
                    max_money_label.place(relx=0.5, rely=0.58, anchor=CENTER)
                    table = coins_game.get_table()
                    moves = coins_game.get_moves()
                    # Create the show table button to show the table of the dynamic programming solution.
                    table_button = Button(random_window, text='Show Table', font=('Arial', 12), fg='#000', bg='#efb539',
                                          activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                                          height=1, command=lambda: self.show_table(table))
                    # Create the show moves button to show the coins that gave the optimal solution.
                    moves_button = Button(random_window, text='Show Moves', font=('Arial', 12), fg='#000', bg='#efb539',
                                          activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                                          height=1, command=lambda: self.show_moves(moves))
                    table_button.place(relx=0.45, rely=0.63, anchor=CENTER)
                    moves_button.place(relx=0.55, rely=0.63, anchor=CENTER)
                    self.customize_button(moves_button)
                    self.customize_button(table_button)

                except ValueError:
                    messagebox.showerror('Error', 'Please enter a Positive and Even number')
                except Exception:
                    messagebox.showerror('Error', 'From value should be less than To value')

        else:
            start_button.configure(command=lambda: start())
            number_of_coins_entry.bind('<Return>', lambda event: start())
            from_entry.bind('<Return>', lambda event: start())

            def start():
                try:
                    number_of_coins = int(number_of_coins_entry.get())
                    from_value = int(from_entry.get())
                    to_value = int(to_entry.get())

                    from_entry.delete(0, END)
                    to_entry.delete(0, END)
                    number_of_coins_entry.delete(0, END)

                    # Check if the number of coins is positive and even.
                    if number_of_coins % 2 != 0 or number_of_coins < 0 or from_value < 0 or to_value < 0:
                        raise ValueError

                    # Check if the from value is less than the to value.
                    if from_value > to_value:
                        raise Exception

                    # Generate random coins with the given range and the number of coins.
                    coins = [random.randint(from_value, to_value) for _ in range(number_of_coins)]

                    to_entry.place_forget()
                    to_label.place_forget()
                    number_of_coins_label.place_forget()
                    number_of_coins_entry.place_forget()
                    from_label.place_forget()
                    from_entry.place_forget()
                    start_button.place_forget()

                    back_button.configure(command=lambda: self.random_data(random_window, mode))

                    frame = Frame(random_window, bg='#fff7e3', relief=RAISED, bd=5)
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
                    player1_label = Label(random_window, text='Player 1:', font=('Arial', 12), bg='#fff7e3', fg='#000')
                    player2_label = Label(random_window, text='Player 2:', font=('Arial', 12), bg='#fff7e3', fg='#000')

                    player1_label.place(relx=0.3, rely=0.78, anchor=CENTER)
                    player2_label.place(relx=0.7, rely=0.78, anchor=CENTER)

                    # Creating the buttons for the coins and the players, the players will take turns to choose
                    # the coins either from first or last.
                    list_buttons = []

                    # Putting each 5 buttons in a row.
                    for i, coin in enumerate(coins):
                        r = i // 5
                        c = i % 5
                        coin_button = Button(frame, text=str(coin), font=('Arial', 12), fg='#000', bg='#efb539',
                                             activebackground='#fed570', activeforeground='#000', relief=FLAT, width=5,
                                             height=2, state=DISABLED)
                        list_buttons.append(coin_button)
                        self.customize_button(coin_button)
                        coin_button.grid(row=r, column=c, padx=3, pady=3)

                    list_buttons[0].config(state=NORMAL)
                    list_buttons[-1].config(state=NORMAL)

                    turn = [0]
                    players = [[], []]  # List to store the coins for each player

                    # Assigning an action for each button to select the coin and add it to the player's list.
                    for button in list_buttons:
                        button.configure(
                            command=lambda bt=button: select_coin(bt, turn[0], list_buttons, list_buttons.index(bt),
                                                                  coins))

                    # This function is to select the coin and add it to the player's list.
                    # It takes the player, the button and the index of the button to add its value to the player's list
                    def select_coin(coins_button, player, buttons, index, coins_list):
                        try:
                            turn[0] = 1 - player
                            coins_button.config(state=DISABLED)

                            # Check which player is playing to add the coin to the right list.
                            if player == 0:
                                if len(buttons) == 1:
                                    players[0].append(int(coins_button['text']))
                                    raise Exception
                                coins_button.config(bg='green')
                                if index == len(buttons) - 1:
                                    buttons[-2].config(state=NORMAL)
                                elif index == 0:
                                    buttons[1].config(state=NORMAL)
                                players[0].append(int(coins_button['text']))
                                player1_label.config(text='Player 1: ' + ', '.join(map(str, players[0])))
                                buttons.remove(coins_button)

                            else:
                                if len(buttons) == 1:
                                    players[1].append(int(coins_button['text']))
                                    player2_label.config(text='Player 2: ' + ', '.join(map(str, players[1])))
                                    raise Exception
                                coins_button.config(bg='red')
                                if index == len(buttons) - 1:
                                    buttons[index - 1].config(state=NORMAL)
                                elif index == 0:
                                    buttons[index + 1].config(state=NORMAL)
                                players[1].append(int(coins_button['text']))
                                player2_label.config(text='Player 2: ' + ', '.join(map(str, players[1])))
                                buttons.remove(coins_button)
                        except Exception as e:
                            # Getting the winner of the game.
                            if sum(players[0]) > sum(players[1]):
                                label_winner = Label(random_window, text='Player 1 Wins, with ' + str(sum(players[0])) +
                                                                         ' coins', font=('Arial', 12), bg='#fff7e3',
                                                     fg='#000')
                                coins_game = Coins(coins_list)
                                coins_game.maximum_money()
                                label_optimal = Label(random_window, text='Optimal Solution: ' +
                                                                          str(coins_game.get_table()[0][-1]),
                                                      font=('Arial', 12), bg='#fff7e3', fg='#000')
                                label_winner.place(relx=0.5, rely=0.7, anchor=CENTER)
                                label_optimal.place(relx=0.5, rely=0.8, anchor=CENTER)
                            elif sum(players[0]) < sum(players[1]):
                                label_winner = Label(random_window, text='Player 2 Wins, with ' + str(sum(players[1])) +
                                                                         ' coins', font=('Arial', 12), bg='#fff7e3',
                                                     fg='#000')
                                coins_game = Coins(coins_list)
                                coins_game.maximum_money()
                                label_optimal = Label(random_window, text='Optimal Solution: ' +
                                                                          str(coins_game.get_table()[0][-1]),
                                                      font=('Arial', 12), bg='#fff7e3', fg='#000')
                                label_winner.place(relx=0.5, rely=0.7, anchor=CENTER)
                                label_optimal.place(relx=0.5, rely=0.8, anchor=CENTER)
                            else:
                                label_winner = Label(random_window, text='It is a Tie', font=('Arial', 12),
                                                     bg='#fff7e3', fg='#000')
                                coins_game = Coins(coins_list)
                                coins_game.maximum_money()
                                label_optimal = Label(random_window, text='Optimal Solution: ' +
                                                                          str(coins_game.get_table()[0][-1]),
                                                      font=('Arial', 12), bg='#fff7e3', fg='#000')
                                label_winner.place(relx=0.5, rely=0.7, anchor=CENTER)
                                label_optimal.place(relx=0.5, rely=0.8, anchor=CENTER)

                except ValueError as e:
                    messagebox.showerror('Error', 'Please enter a Positive and Even number')
                    print(e)

        random_window.mainloop()

    # This function is for the option, manual data, the user will enter the number of the coins and the coins.
    def manual_data(self, window, mode):
        # Closing the past window and open a new window for the manual choice.
        window.destroy()
        manual_window = Tk()
        self.customize_window(manual_window, 1200, 700, 'Coins Game')
        img = Image.open('Game_theme.png')
        img = img.resize((1200, 700))
        bg = ImageTk.PhotoImage(img)
        label = Label(manual_window, image=bg)
        label.place(x=0, y=0)
        back_button = Button(manual_window, text='<Back', font=('Arial', 12), fg='#000', bg='#efb539',
                             activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                             height=1, command=lambda: self.game(mode, manual_window))
        back_button.place(relx=0.2, rely=0.2, anchor=CENTER)
        self.customize_button(back_button)

        # Customizing the manual window with the number of coins and the coins entry.
        number_of_coins_label = Label(manual_window, text='Number of coins:', font=('Arial', 12), bg='#fff7e3',
                                      fg='#000')
        number_of_coins_entry = Entry(manual_window, font=('Arial', 12), bg='#fff', fg='#000', width=5)
        coins_label = Label(manual_window, text='Coins:', font=('Arial', 12), bg='#fff7e3', fg='#000')
        coins_entry = Entry(manual_window, font=('Arial', 12), bg='#fff', fg='#000', width=30)
        number_of_coins_label.place(relx=0.45, rely=0.3, anchor=CENTER)
        number_of_coins_entry.place(relx=0.53, rely=0.3, anchor=CENTER)
        coins_label.place(relx=0.4, rely=0.35, anchor=CENTER)
        coins_entry.place(relx=0.54, rely=0.35, anchor=CENTER)
        number_of_coins_entry.focus()

        # The start button will start the game with the data entered by the user.
        start_button = Button(manual_window, text='Start', font=('Arial', 12), fg='#000', bg='#efb539',
                              activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                              height=1)
        start_button.place(relx=0.58, rely=0.45, anchor=CENTER)
        self.customize_button(start_button)

        # The clear button will clear the entries.
        clear_button = Button(manual_window, text='Clear', font=('Arial', 12), fg='#000', bg='#efb539',
                              activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                              height=1,
                              command=lambda:
                              [number_of_coins_entry.delete(0, END), coins_entry.delete(0, END)])
        clear_button.place(relx=0.48, rely=0.45, anchor=CENTER)
        self.customize_button(clear_button)

        # Check the number of players playing.
        if mode == 'one_player':
            start_button.config(command=lambda: start())
            number_of_coins_entry.bind('<Return>', lambda event: start())
            coins_entry.bind('<Return>', lambda event: start())

            # This function is to start the game with the data entered by the user.
            def start():
                try:
                    # Get the number of coins and the coins entered by the user.
                    number_of_coins = int(number_of_coins_entry.get())
                    coins = list(map(int, coins_entry.get().split()))
                    # Check of the number of coins is equal to the length of the coins list.
                    if number_of_coins != len(coins):
                        raise ValueError

                    if number_of_coins % 2 != 0 or number_of_coins < 0:
                        raise ValueError

                    coins_game = Coins(coins)
                    coins_game.maximum_money()
                    max_money_label = Label(manual_window, text='Max Money: ' + str(coins_game.dp[0][-1]),
                                            font=('Arial', 12), bg='#fff7e3', fg='#000')
                    max_money_label.place(relx=0.5, rely=0.58, anchor=CENTER)
                    table = coins_game.get_table()
                    moves = coins_game.get_moves()
                    table_button = Button(manual_window, text='Show Table', font=('Arial', 12), fg='#000', bg='#efb539',
                                          activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                                          height=1, command=lambda: self.show_table(table))
                    moves_button = Button(manual_window, text='Show Moves', font=('Arial', 12), fg='#000', bg='#efb539',
                                          activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                                          height=1, command=lambda: self.show_moves(moves))
                    table_button.place(relx=0.45, rely=0.63, anchor=CENTER)
                    moves_button.place(relx=0.55, rely=0.63, anchor=CENTER)
                    self.customize_button(moves_button)
                    self.customize_button(table_button)

                except ValueError:
                    messagebox.showerror('Error', 'Please enter a Positive and Even number of coins')
                except Exception:
                    messagebox.showerror('Error', 'Something is wrong')
        else:
            start_button.config(command=lambda: start())
            number_of_coins_entry.bind('<Return>', lambda event: start())
            coins_entry.bind('<Return>', lambda event: start())

            def start():
                try:
                    coins = list(map(int, coins_entry.get().split()))
                    number_of_coins = len(coins)
                    if number_of_coins % 2 != 0:
                        raise ValueError

                    if number_of_coins != int(number_of_coins_entry.get()):
                        raise Exception

                    coins_label.place_forget()
                    coins_entry.place_forget()
                    number_of_coins_label.place_forget()
                    number_of_coins_entry.place_forget()
                    start_button.place_forget()
                    clear_button.place_forget()

                    back_button.configure(command=lambda: self.manual_data(manual_window, mode))

                    # Creating a frame to contain the buttons of the coins.
                    frame = Frame(manual_window, bg='#fff7e3', relief=RAISED, bd=5)
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
                    player1_label = Label(manual_window, text='Player 1:', font=('Arial', 12), bg='#fff7e3', fg='#000')
                    player2_label = Label(manual_window, text='Player 2:', font=('Arial', 12), bg='#fff7e3', fg='#000')

                    player1_label.place(relx=0.3, rely=0.78, anchor=CENTER)
                    player2_label.place(relx=0.7, rely=0.78, anchor=CENTER)

                    list_buttons = []
                    # Putting each 5 buttons in a row.
                    for i, coin in enumerate(coins):
                        r = i // 5 + 1
                        c = i % 5 + 2
                        coin_button = Button(frame, text=str(coin), font=('Arial', 12), fg='#000', bg='#efb539',
                                             activebackground='#fed570', activeforeground='#000', relief=FLAT, width=5,
                                             height=2, state=DISABLED)
                        list_buttons.append(coin_button)
                        self.customize_button(coin_button)
                        coin_button.grid(row=r, column=c, padx=3, pady=3)

                    list_buttons[0].config(state=NORMAL)
                    list_buttons[-1].config(state=NORMAL)

                    turn = [0]
                    players = [[], []]  # List to store the coins for each player
                    # Assigning an action for each button to select the coin and add it to the player's list.
                    for button in list_buttons:
                        button.configure(
                            command=lambda bt=button: select_coin(bt, turn[0], list_buttons, list_buttons.index(bt),
                                                                  coins))

                    # This function is to select the coin and add it to the player's list.
                    def select_coin(coins_button, player, buttons, index, coins_list):
                        try:
                            turn[0] = 1 - player
                            coins_button.config(state=DISABLED)

                            # Check which player is playing to add the coin to the right list.
                            if player == 0:
                                if len(buttons) == 1:
                                    players[0].append(int(coins_button['text']))
                                    raise Exception
                                coins_button.config(bg='green')
                                if index == len(buttons) - 1:
                                    buttons[-2].config(state=NORMAL)
                                elif index == 0:
                                    buttons[1].config(state=NORMAL)
                                players[0].append(int(coins_button['text']))
                                player1_label.config(text='Player 1: ' + ', '.join(map(str, players[0])))
                                buttons.remove(coins_button)

                            else:
                                if len(buttons) == 1:
                                    players[1].append(int(coins_button['text']))
                                    player2_label.config(text='Player 2: ' + ', '.join(map(str, players[1])))
                                    raise Exception
                                coins_button.config(bg='red')
                                if index == len(buttons) - 1:
                                    buttons[index - 1].config(state=NORMAL)
                                elif index == 0:
                                    buttons[index + 1].config(state=NORMAL)
                                players[1].append(int(coins_button['text']))
                                player2_label.config(text='Player 2: ' + ', '.join(map(str, players[1])))
                                buttons.remove(coins_button)
                        except Exception as e:
                            # Getting the winner of the game.
                            if sum(players[0]) > sum(players[1]):
                                label_winner = Label(manual_window, text='Player 1 Wins, with ' + str(sum(players[0])) +
                                                                         ' coins', font=('Arial', 12), bg='#fff7e3',
                                                     fg='#000')
                                coins_game = Coins(coins_list)
                                coins_game.maximum_money()
                                label_optimal = Label(manual_window, text='Optimal Solution: ' +
                                                                          str(coins_game.get_table()[0][-1]),
                                                      font=('Arial', 12), bg='#fff7e3', fg='#000')
                                label_winner.place(relx=0.5, rely=0.7, anchor=CENTER)
                                label_optimal.place(relx=0.5, rely=0.8, anchor=CENTER)
                            elif sum(players[0]) < sum(players[1]):
                                label_winner = Label(manual_window, text='Player 2 Wins, with ' + str(sum(players[1])) +
                                                                         ' coins', font=('Arial', 12), bg='#fff7e3',
                                                     fg='#000')
                                coins_game = Coins(coins_list)
                                coins_game.maximum_money()
                                label_optimal = Label(manual_window, text='Optimal Solution: ' +
                                                                          str(coins_game.get_table()[0][-1]),
                                                      font=('Arial', 12), bg='#fff7e3', fg='#000')
                                label_winner.place(relx=0.5, rely=0.7, anchor=CENTER)
                                label_optimal.place(relx=0.5, rely=0.8, anchor=CENTER)
                            else:
                                label_winner = Label(manual_window, text='It is a Tie', font=('Arial', 12),
                                                     bg='#fff7e3', fg='#000')
                                coins_game = Coins(coins_list)
                                coins_game.maximum_money()
                                label_optimal = Label(manual_window, text='Optimal Solution: ' +
                                                                          str(coins_game.get_table()[0][-1]),
                                                      font=('Arial', 12), bg='#fff7e3', fg='#000')
                                label_winner.place(relx=0.5, rely=0.7, anchor=CENTER)
                                label_optimal.place(relx=0.5, rely=0.8, anchor=CENTER)

                except ValueError:
                    messagebox.showerror('Error', 'Please enter a Positive and Even number of coins')
                except Exception:
                    messagebox.showerror('Error', 'Number of coins is not equal to the '
                                                  'number of coins entered')
        manual_window.mainloop()

    # This function is to create the file data window, the user will choose a file and the data source will be the data
    def file_data(self, window, mode):
        # Creating the file window and customizing it.
        window.destroy()
        file_window = Tk()
        self.customize_window(file_window, 1200, 700, 'Coins Game')
        img = Image.open('Game_theme.png')
        img = img.resize((1200, 700))
        bg = ImageTk.PhotoImage(img)
        label = Label(file_window, image=bg)
        label.place(x=0, y=0)
        back_button = Button(file_window, text='<Back', font=('Arial', 12), fg='#000', bg='#efb539',
                             activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                             height=1, command=lambda: self.game(mode, file_window))
        back_button.place(relx=0.2, rely=0.2, anchor=CENTER)
        read_file_button = Button(file_window, text='Read File', font=('Arial', 12), fg='#000', bg='#efb539',
                                  activebackground='#fed570', activeforeground='#000', relief=FLAT, width=10,
                                  height=1)
        read_file_button.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.customize_button(read_file_button)
        self.customize_button(back_button)

        # Check the number of players playing.
        if mode == 'one_player':
            read_file_button.config(command=lambda: read_file())

            # This function is to read the file and get the data from it.
            def read_file():
                try:
                    # Open a dialog to choose a file.
                    file_path = filedialog.askopenfilename(title='Select a file', initialdir='C:Users/user/Desktop'
                                                                                             '/University/3- Third year'
                                                                                             '/First semester/'
                                                                                             'COMP336/Project #1'
                                                                                             '/Coins Game',
                                                           filetypes=[('Text Files', '*.txt')])
                    # Open the file using with open, to close it automatically after reading it.
                    with open(file_path, 'r') as file:
                        lines = file.readlines()
                        coins = []
                        # Read the lines of the file and append the coins to the coins list.
                        for line in lines:
                            list_line = list(map(int, line.split()))
                            if len(list_line) > 1:
                                coins.append(list_line)

                        # This function is to calculate the maximum money for each line in the file.
                        def calculate(i):
                            current_coins = coins[i]
                            game_class = Coins(current_coins)
                            game_class.maximum_money()
                            table = game_class.get_table()
                            result = table[0][-1]

                            # Create the labels for the coins and the result.
                            list_label = Label(file_window, text=f'The coins are: {current_coins}', font=('Arial', 12),
                                               fg='#000', bg='#fff7e3')

                            result_label = Label(file_window, text=f'The maximum money you can win is: {result}',
                                                 font=('Arial', 12), fg='#000', bg='#fff7e3')
                            list_label.place(relx=0.5, rely=0.5, anchor=CENTER)
                            result_label.place(relx=0.5, rely=0.55, anchor=CENTER)

                            # The next button to go to the next list of coins in the coins list.
                            button_next = Button(file_window, text='>>', font=('Arial', 12), fg='#000', bg='#efb539',
                                                 activebackground='#fed570', activeforeground='#000', relief=FLAT,
                                                 width=5,
                                                 height=1, command=lambda: next_line(i))
                            button_next.place(relx=0.52, rely=0.6, anchor=CENTER)

                            # The previous button to go to the previous list of coins in the coins list.
                            button_pre = Button(file_window, text='<<', font=('Arial', 12), fg='#000', bg='#efb539',
                                                activebackground='#fed570', activeforeground='#000', relief=FLAT,
                                                width=5,
                                                height=1, command=lambda: pre(i))
                            button_pre.place(relx=0.47, rely=0.6, anchor=CENTER)

                            # The table button to present the dp table of the optimal solution.
                            button_table = Button(file_window, text='Show Table', font=('Arial', 12), fg='#000',
                                                  bg='#efb539',
                                                  activebackground='#fed570', activeforeground='#000', relief=FLAT,
                                                  width=10,
                                                  height=1, command=lambda: self.show_table(table))
                            button_table.place(relx=0.45, rely=0.7, anchor=CENTER)

                            # The moves button to present the coins that gave the optimal solution.
                            moves_button = Button(file_window, text='Show Moves', font=('Arial', 12), fg='#000',
                                                  bg='#efb539', activebackground='#fed570', activeforeground='#000',
                                                  relief=FLAT, width=10, height=1,
                                                  command=lambda: self.show_moves(game_class.get_moves()))
                            moves_button.place(relx=0.54, rely=0.7, anchor=CENTER)

                            # This function is the event of the pre button, it gets the previous list of coins.
                            # if it reaches the index 0, it will get the last list of coins.
                            def pre(pre_index):
                                pre_index -= 1
                                if pre_index < 0:
                                    pre_index = len(coins) - 1
                                result_label.config(text='')
                                list_label.config(text='')
                                calculate(pre_index)

                            # This function is the event of the next button, it gets the next list of coins.
                            # if it reaches the last index, it will get the first list of coins.
                            def next_line(next_index):
                                next_index += 1
                                if next_index == len(coins):
                                    next_index = 0
                                result_label.config(text='')
                                list_label.config(text='')
                                calculate(next_index)

                        calculate(0)

                except ValueError:
                    messagebox.showerror('Error', 'File is Corrupted')
                except Exception:
                    messagebox.showerror('Error', 'Choose a File')

        else:
            read_file_button.config(command=lambda: read_file())

            # This function is to read the file and get the data from it.
            def read_file():
                try:
                    file_path = filedialog.askopenfilename(title='Select a file', initialdir='C:Users/user/Desktop'
                                                                                             '/University/3- Third year'
                                                                                             '/First semester/'
                                                                                             'COMP336/Project #1'
                                                                                             '/Coins Game',
                                                           filetypes=[('Text Files', '*.txt')])
                    with open(file_path, 'r') as file:
                        lines = file.readlines()
                        coins = []
                        for line in lines:
                            list_line = list(map(int, line.split()))
                            if len(list_line) > 1:
                                coins.append(list_line)

                    def calculate(i):
                        current_coins = coins[i]

                        list_label = Label(file_window, text=f'The coins are: {current_coins}', font=('Arial', 12),
                                           fg='#000', bg='#fff7e3')


                        list_label.place(relx=0.5, rely=0.4, anchor=CENTER)

                        button_next = Button(file_window, text='>>', font=('Arial', 12), fg='#000', bg='#efb539',
                                             activebackground='#fed570', activeforeground='#000', relief=FLAT,
                                             width=5,
                                             height=1, command=lambda: next_line(i))
                        button_next.place(relx=0.525, rely=0.55, anchor=CENTER)

                        button_pre = Button(file_window, text='<<', font=('Arial', 12), fg='#000', bg='#efb539',
                                            activebackground='#fed570', activeforeground='#000', relief=FLAT,
                                            width=5,
                                            height=1, command=lambda: pre(i))
                        button_pre.place(relx=0.475, rely=0.55, anchor=CENTER)

                        choose_button = Button(file_window, text='Choose', font=('Arial', 12), fg='#000', bg='#efb539',
                                               activebackground='#fed570', activeforeground='#000', relief=FLAT,
                                               width=10,
                                               height=1, command=lambda: choose(i))
                        choose_button.place(relx=0.5, rely=0.5, anchor=CENTER)
                        self.customize_button(choose_button)

                        # Getting the list of coins for the chosen index. And present the data to the users.
                        def choose(index):
                            read_file_button.place_forget()
                            list_label.place_forget()
                            button_next.place_forget()
                            button_pre.place_forget()
                            choose_button.place_forget()
                            back_button.configure(command=lambda: self.file_data(file_window, mode))
                            coins_list = coins[index]
                            # Creating the frame to contain the buttons of the coins.
                            frame = Frame(file_window, bg='#fff7e3', relief=RAISED, bd=5)
                            frame.place(relx=0.5, rely=0.5, anchor=CENTER)
                            player1_label = Label(file_window, text='Player 1:', font=('Arial', 12), bg='#fff7e3',
                                                  fg='#000')
                            player2_label = Label(file_window, text='Player 2:', font=('Arial', 12), bg='#fff7e3',
                                                  fg='#000')

                            player1_label.place(relx=0.3, rely=0.78, anchor=CENTER)
                            player2_label.place(relx=0.7, rely=0.78, anchor=CENTER)

                            # Creating the buttons for the coins and the players, the players will take turns to choose
                            list_buttons = []
                            # Putting each 5 buttons in a row.
                            for i, coin in enumerate(coins_list):
                                r = i // 5
                                c = i % 5
                                coin_button = Button(frame, text=str(coin), font=('Arial', 12), fg='#000', bg='#efb539',
                                                     activebackground='#fed570', activeforeground='#000', relief=FLAT, width=5,
                                                     height=2, state=DISABLED)
                                list_buttons.append(coin_button)
                                self.customize_button(coin_button)
                                coin_button.grid(row=r, column=c, padx=3, pady=3)

                            list_buttons[0].config(state=NORMAL)
                            list_buttons[-1].config(state=NORMAL)

                            turn = [0]
                            players = [[], []]
                            # Assigning an action for each button to select the coin and add it to the player's list.
                            for button in list_buttons:
                                button.configure(
                                    command=lambda bt=button: select_coin(bt, turn[0], list_buttons, list_buttons.index(bt),
                                                                          coins_list))

                            # This function is to select the coin and add it to the player's list.
                            def select_coin(coins_button, player, buttons, index, coins_list):
                                try:
                                    turn[0] = 1 - player
                                    coins_button.config(state=DISABLED)

                                    # Check which player is playing to add the coin to the right list.
                                    if player == 0:
                                        if len(buttons) == 1:
                                            players[0].append(int(coins_button['text']))
                                            raise Exception
                                        coins_button.config(bg='green')
                                        if index == len(buttons) - 1:
                                            buttons[-2].config(state=NORMAL)
                                        elif index == 0:
                                            buttons[1].config(state=NORMAL)
                                        players[0].append(int(coins_button['text']))
                                        player1_label.config(text='Player 1: ' + ', '.join(map(str, players[0])))
                                        buttons.remove(coins_button)

                                    else:
                                        if len(buttons) == 1:
                                            players[1].append(int(coins_button['text']))
                                            player2_label.config(text='Player 2: ' + ', '.join(map(str, players[1])))
                                            raise Exception
                                        coins_button.config(bg='red')
                                        if index == len(buttons) - 1:
                                            buttons[index - 1].config(state=NORMAL)
                                        elif index == 0:
                                            buttons[index + 1].config(state=NORMAL)
                                        players[1].append(int(coins_button['text']))
                                        player2_label.config(text='Player 2: ' + ', '.join(map(str, players[1])))
                                        buttons.remove(coins_button)
                                except Exception as e:
                                    # Getting the winner of the game.
                                    if sum(players[0]) > sum(players[1]):
                                        label_winner = Label(file_window, text='Player 1 Wins, with ' + str(sum(players[0])) +
                                                                             ' coins', font=('Arial', 12), bg='#fff7e3',
                                                             fg='#000')
                                        coins_game = Coins(coins_list)
                                        coins_game.maximum_money()
                                        label_optimal = Label(file_window, text='Optimal Solution: ' +
                                                                              str(coins_game.get_table()[0][-1]),
                                                              font=('Arial', 12), bg='#fff7e3', fg='#000')
                                        label_winner.place(relx=0.5, rely=0.7, anchor=CENTER)
                                        label_optimal.place(relx=0.5, rely=0.8, anchor=CENTER)
                                    elif sum(players[0]) < sum(players[1]):
                                        label_winner = Label(file_window, text='Player 2 Wins, with '
                                                                                + str(sum(players[1])) + ' coins', font=('Arial', 12),
                                                                bg='#fff7e3', fg='#000')
                                        coins_game = Coins(coins_list)
                                        coins_game.maximum_money()
                                        label_optimal = Label(file_window, text='Optimal Solution: ' +
                                                                              str(coins_game.get_table()[0][-1]),
                                                              font=('Arial', 12), bg='#fff7e3', fg='#000')
                                        label_winner.place(relx=0.5, rely=0.7, anchor=CENTER)
                                        label_optimal.place(relx=0.5, rely=0.8, anchor=CENTER)
                                    else:
                                        label_winner = Label(file_window, text='It is a Tie', font=('Arial', 12),
                                                             bg='#fff7e3', fg='#000')
                                        coins_game = Coins(coins_list)
                                        coins_game.maximum_money()
                                        label_optimal = Label(file_window, text='Optimal Solution: ' +
                                                                              str(coins_game.get_table()[0][-1]),
                                                              font=('Arial', 12), bg='#fff7e3', fg='#000')
                                        label_winner.place(relx=0.5, rely=0.7, anchor=CENTER)
                                        label_optimal.place(relx=0.5, rely=0.8, anchor=CENTER)


                        # This function is the event of the pre button, it gets the previous list of coins.
                        # if it reaches the index 0, it will get the last list of coins.
                        def pre(pre_index):
                            pre_index -= 1
                            if pre_index < 0:
                                pre_index = len(coins) - 1
                            list_label.config(text='')
                            calculate(pre_index)

                        # This function is the event of the next button, it gets the next list of coins.
                        # if it reaches the last index, it will get the first list of coins.
                        def next_line(next_index):
                            next_index += 1
                            if next_index == len(coins):
                                next_index = 0
                            list_label.config(text='')
                            calculate(next_index)

                    calculate(0)



                except ValueError:
                    messagebox.showerror('Error', 'File is Corrupted')

        file_window.mainloop()


    # This function to change the background of the button when hovering over it.
    def button_hover(self, event, button):
        button.config(bg='#fed570', fg='#000')

    # This function is to change the color of the button when the mouse leave it
    def button_leave(self, event, button):
        button.config(fg='#000', bg='#efb539')

    # This function is to customize the window with the title, width, height, and icon.
    def customize_window(self, window, width, height, title):
        window.title(title)
        window.geometry(str(width) + "x" + str(height))
        window.resizable(False, False)
        icon = PhotoImage(file='coin.png')
        window.iconphoto(False, icon)

    # This function is to customize the button with the background color, foreground color, font, and relief.
    def customize_button(self, button):
        button.config(bg='#efb539', fg='#000', font=('Arial', 12), relief=FLAT)
        button.bind('<Enter>', lambda event: self.button_hover('<Enter>', button=button))
        button.bind('<Leave>', lambda event: self.button_leave('<Leave>', button=button))

    # This function is to show the table of the dp solution.
    def show_table(self, table):
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

    # This function is to show the coins that gave the optimal solution.
    def show_moves(self, moves):
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


GUI()
