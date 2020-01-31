# -*- coding: utf-8 -*-
from Papers import get_info, get_files
from curses import panel as cpanel
import curses

MENU = ['Home', 'Play', 'Scoreboard', 'Exit']
FILEMENU = get_files() + ['Exit']

class paperPanel:
    def __init__(self, h, l, y, x, title='', items=['']):
        # create window with a bounding box
        self.win = curses.newwin(h, l, y, x)
        self.win.erase()
        self.win.box()

        # set title and items
        self.title = title
        self.items = items

        # create paper title if not empty
        if title != '':
            self.writeTitle(l, title)

        # init active row to 0
        self.currentRow = 0
        self.panel = cpanel.new_panel(self.win)

    def writeTitle(self, l, title):
        """ Writes the title in top center of the bounding box

        :param l: width of window
        :param title: title of window to be written
        :returns: Nothing
        :rtype: Null
        """

        # write title centered on top of bounding box
        titlePadded = f" {title} "
        titleBeginning = l//2 - len(titlePadded)//2
        self.win.addstr(0, titleBeginning, titlePadded)


def shortenLine(listOfStrings, maxWidth):
    for i, elem in enumerate(listOfStrings):
        if len(elem) > maxWidth:
            # should we show extension?
            listOfStrings[i] = elem[:maxWidth-7] + '...'
    return listOfStrings


def printMenu(scr, selected_row_idx, items=[], hide_cursor=False):
    # scr.clear()
    h, w = scr.getmaxyx()

    # Make sure strings within a single line
    if items:
        items = shortenLine(items, w-2)
        for y in range(1, h-1):
            scr.addstr(y, 1, " "*(w-2))

    for idx, row in enumerate(items):

        # Check if index is out of panel
        if idx > h-3:
            break
        x = 1
        y = 1 + idx

        if idx == selected_row_idx and not hide_cursor:
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
    except curses.error:
        pass
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # find window corners to init paper windows
    y0, x0, ncols, nlines = getCorners(scr)
    topPaper = paperPanel(nlines//2, ncols, y0, x0, "1st panel", MENU)
    botPaper = paperPanel(nlines//2, ncols, y0+nlines//2, x0, "2nd panel",
                          FILEMENU)
    panels = [botPaper, topPaper]

    # initial display of windows before loop
    printMenu(topPaper.win, topPaper.currentRow, topPaper.items, hide_cursor=True)
    printMenu(botPaper.win, botPaper.currentRow, botPaper.items)

    # run stuff
    while True:

        key = scr.getch()

        if key in [27, 113]:
            # exit
            break
        elif (key == curses.KEY_UP) and (panels[0].currentRow > 0):
            # go down a row
            panels[0].currentRow -= 1
        elif (key == curses.KEY_DOWN and
              panels[0].currentRow < len(panels[0].items)-1):
            # go up a row
            panels[0].currentRow += 1
        elif key == 9:
            # tab changes avtive paper window
            panels = panels[::-1]
        else:
            pass

        # Print menu in current window only
        printMenu(panels[0].win, panels[0].currentRow, panels[0].items)
        printMenu(panels[1].win, panels[1].currentRow, panels[1].items, hide_cursor=True)

if __name__ == '__main__':
    curses.wrapper(main)
