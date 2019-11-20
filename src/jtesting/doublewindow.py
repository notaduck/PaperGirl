# -*- coding: utf-8 -*-
import curses
import curses.panel

def make_panel(nlines, ncols, begin_y, begin_x, a_str):
    a_str_pad = f" {a_str}  "
    win = curses.newwin(nlines, ncols, begin_y, begin_x)
    win.erase()
    win.box()

    x = ncols//2 - len(a_str_pad)//2
    win.addstr(0, x, a_str_pad)
    panel = curses.panel.new_panel(win)
    return win, panel

def getCorners(scr):
    uly = (int(scr.getbegyx()[0]))
    ulx = (int(scr.getbegyx()[1]))
    lry = (int(scr.getmaxyx()[0] - 2))
    lrx = (int(scr.getmaxyx()[1] - 1))

    return ulx, uly, lrx, lry

def main(scr):
    #setup
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    y0, x0, ncols, nlines = getCorners(scr)
    win1, panel1 = make_panel(nlines//2, ncols, y0, x0, "1st panel")
    win2, panel2 = make_panel(nlines//2, ncols, y0+nlines//2, x0, "2nd panel")

    curses.panel.update_panels()
    scr.refresh()

    # specify the current selected row
    current_row = 0
    current_panel = 1

    # run stuff
    while True:
        key = scr.getch()

        if key == curses.KEY_ENTER:
            break
        else:
            scr.addstr(str(key))
        scr.refresh()

if __name__ == '__main__':
    curses.wrapper(main)
