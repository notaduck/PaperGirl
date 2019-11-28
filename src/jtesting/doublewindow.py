# -*- coding: utf-8 -*-
from curses import panel as cpanel
import curses
from Papers import get_info, get_files

# MENU = ['Home', 'Play', 'Scoreboard', 'Exit']
MENU = get_files() + ['Exit']

class paperPanel:
    def __init__(self, h: int, l: int, y: int, x: int, panelName: str):
        self.win = curses.newwin(h, l, y, x)


def printMenu(scr, selected_row_idx, items):
    # scr.clear()
    h, w = scr.getmaxyx()
    for y in range(1, h-1):
        scr.addstr(y, 1, " "*(w-2))

    for idx, row in enumerate(items):

        # Check if index is out of panel
        if idx > h-3:
            break
        # x = w//2 - len(row)//2 - 20
        # y = h//2 - len(MENU)//2 + idx
        x = 1
        y = 1 + idx

        if idx == selected_row_idx:
            scr.attron(curses.color_pair(1))
            scr.addstr(y, x, row)
            scr.attroff(curses.color_pair(1))
        else:
            scr.addstr(y, x, row)
    scr.refresh()
    curses.panel.update_panels()

def init_panel(nlines, ncols, begin_y, begin_x, a_str):
    str_pad = f" {a_str}  "
    win = curses.newwin(nlines, ncols, begin_y, begin_x)
    win.erase()
    win.box()

    x = ncols//2 - len(str_pad)//2
    win.addstr(0, x, str_pad)
    panel = cpanel.new_panel(win)
    return win, panel

def getCorners(scr):
    uly = (int(scr.getbegyx()[0]))
    ulx = (int(scr.getbegyx()[1]))
    lry = (int(scr.getmaxyx()[0] - 2))
    lrx = (int(scr.getmaxyx()[1] - 1))

    return ulx, uly, lrx, lry

def main(scr):
    #setup
    try:
        curses.curs_set(0)
    except:
        pass
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    y0, x0, ncols, nlines = getCorners(scr)
    win1, panel1 = init_panel(nlines//2, ncols, y0, x0, "1st panel")
    win2, panel2 = init_panel(nlines//2, ncols, y0+nlines//2, x0, "2nd panel")
    wins = [win1, win2]
    panels = [panel1, panel2]



    # specify the current selected row
    current_row = 0
    current_win = win1
    current_pan = panel1

    printMenu(win2, current_row, MENU)
    scr.refresh()

    # run stuff
    while True:
        key = scr.getch()

        if key == 27:
            break
        elif (key == curses.KEY_UP) and (current_row > 0):
            current_row -= 1
        elif (key == curses.KEY_DOWN) and (current_row < len(MENU)-1):
            current_row += 1
        elif key == 9:
            current_win = wins[-1]
            currentPanel = panels[-1]
            wins = wins[::-1]
            panels = panels[::-1]

        else:
            pass

        if current_win == win2:
            printMenu(win2, current_row, MENU)

        # scr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
