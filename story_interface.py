def display_puzzles(window):
     
    window.title("All John's MadLibs Puzzles")
    frame = Frame(window)

    game = None

    def puzzle_clicked(puzzle):
        frame.destroy()
        play_puzzle(window, 0, puzzle)

    manager = PuzzleManager()
    for i, game in enumerate(manager.puzzles):
        if not game.blanks:
            continue
        game_button = Button(frame, text=game.title, pady=10, command=lambda puzzle=game: puzzle_clicked(puzzle))
        r = int(int(i)/3)+1
        c = int(i) % 3
        game_button.grid(row=r, column=c)
        frame.columnconfigure(c, weight=1)
        frame.rowconfigure(r, weight=1)
    frame.grid()
    frame.pack(expand=True)

    window.mainloop()

def fill_blank(window, frame, fill_val, puzzle, blank_index):
    print(fill_val.get())
    puzzle.fill_blank(blank_index, fill_val.get())
    frame.destroy()
    if blank_index >= len(puzzle.blanks)-1:
        puzzle.completed = True
        show_puzzle_result(window, puzzle)
    else:
        play_puzzle(window, blank_index+1, puzzle)
    return puzzle

def play_puzzle(window, blank_index, puzzle):
    frame = Frame(window)

    def go_back():
        frame.destroy()
        display_puzzles(window)

    total = len(puzzle.blanks)
    curr_blank = puzzle.blanks[blank_index]
    label = Label(frame, font='Helvetica 20', text=str(blank_index)+"/"+str(total)+" "+curr_blank[1], anchor=CENTER, pady=10)
    fill_val = StringVar()
    entry = Entry(frame, textvariable=fill_val)
    entry.bind('<Return>', lambda _, w=window, f=frame, v=fill_val, p=puzzle, i=blank_index: fill_blank(w, f, v, p, i))
    entry.focus()
    label.grid(row=1, column=1)
    entry.grid(row=2, column=1)

    back_button = Button(frame, text="Back", pady=10, command=go_back)
    back_button.grid(column=0, row=2)

    frame.grid()
    frame.pack(expand=True)

    window.mainloop()


def show_puzzle_result(window, puzzle):
    frame = Frame(window)

    def go_back():
        frame.destroy()
        display_puzzles(window)

    story_title = Label(frame, font='Helvetica 20', text=puzzle.title, anchor=CENTER, pady=10)
    story_text = Label(frame, font='Helvetica 20', text=puzzle.story, anchor=CENTER, pady=10, justify=CENTER, wraplength=500)
    back_button = Button(frame, text="Back", pady=10, command=go_back)
    story_title.grid(column=0, row=0)
    story_text.grid(column=0, row=1)
    back_button.grid(column=0, row=2)

    frame.grid()
    frame.pack(expand=True)
    window.mainloop()


def run_main_menu():
    window = Tk()
     
    window.title("Welcome to John's Mad Libs")
    window.geometry('500x600')

    menu = Menu(window)
    new_item = Menu(menu)
    new_item.add_command(label='New', command=run_main_menu)
    new_item.add_separator()
    new_item.add_command(label='Edit')
    menu.add_cascade(label='File', menu=new_item)
    window.config(menu=menu)

    frame = Frame(window)
     
    def see_puzzles_clicked(window):
        frame.destroy()
        display_puzzles(window)
        return

    def exit_clicked():
        window.destroy()
        return

    # add greeting
    lbl = Label(frame, font='Helvetica 20', text="Main Menu", anchor=CENTER, pady=10)
    lbl.grid(column=0, row=0)

    # add exit button
    exit_button = Button(frame, text="Exit", pady=20, command=exit_clicked)
    exit_button.grid(column=0, row=2)

    # add link to puzzles
    btn = Button(frame, text="See puzzles", pady=10, command=lambda w=window: see_puzzles_clicked(w))
    btn.grid(column=0, row=1)

    frame.columnconfigure(0, weight=1)
    # window.rowconfigure(0, weight=1)
     
    frame.grid()
    frame.pack(expand=True)
    window.mainloop()

if __name__ == '__main__':
    from tkinter import *
    from puzzle_manager import *

    run_main_menu()
