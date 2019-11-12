import curses
from Papers import *


def print_files(stdscr, selected_row_idx):
    files = get_files()
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(files):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(files) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()
    # for i, file in enumerate(files):
    #    stdscr.addstr(i, 0, file)
    #


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_files(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(files) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_center(stdscr, "You selected '{}'".format(files[current_row]))
            stdscr.getch()
            # if user selected last row, exit the program
            if current_row == len(files) - 1:
                break

        print_files(stdscr, current_row)


curses.wrapper(main)
#main(curses.initscr())
