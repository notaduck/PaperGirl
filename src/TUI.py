# https://raw.githubusercontent.com/nikhilkumarsingh/python-curses-tut/master/code/example5.py

import curses
from Papers import *

# menu = ['Home', 'Play', 'Scoreboard', 'Exit']
menu = get_files() + ['Exit']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
            stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

def drawRrectangle(win, corners):                                         
    """Draw a rectangle with corners at the provided upper-left                 
    and lower-right coordinates.                                                
    """                                                                         
    (ulx,uly,lrx,lry) = corners 
    win.vline(uly+1, ulx, curses.ACS_VLINE, lry - uly - 1)                      
    win.hline(uly, ulx+1, curses.ACS_HLINE, lrx - ulx - 1)                      
    win.hline(lry, ulx+1, curses.ACS_HLINE, lrx - ulx - 1)                      
    win.vline(uly+1, lrx, curses.ACS_VLINE, lry - uly - 1)                      
    win.addch(uly, ulx, curses.ACS_ULCORNER)                                    
    win.addch(uly, lrx, curses.ACS_URCORNER)                                    
    win.addch(lry, lrx, curses.ACS_LRCORNER)                                    
    win.addch(lry, ulx, curses.ACS_LLCORNER)

def getCorners(stdscr):
    uly = (int(stdscr.getbegyx()[0]))
    ulx = (int(stdscr.getbegyx()[1]))
    lry = (int(stdscr.getmaxyx()[0] * 0.7))
    lrx = (int(stdscr.getmaxyx()[1] - 1))

    return ulx, uly, lrx, lry


def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row)
    
    while 1:
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            stdscr.getch()
            current_file = menu[current_row]
            # if user selected last row, exit the program
            if current_row == len(menu)-1:
                break


        print_menu(stdscr, current_row)


curses.wrapper(main)
