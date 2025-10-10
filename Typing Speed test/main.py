import curses
from curses import wrapper


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test!")
    stdscr.addstr("\nPress any key to begin !")
    stdscr.refresh()
    stdscr.getkey()

def spm_test(stdscr):
    target_text = "Hello world this is some text tape of this app!"
    current_text = []

    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    stdscr.getkey()

    while True:
        key = stdscr.getkey()
        current_text.append(key)

        stdscr.clear()
        stdscr.addstr(target_text)
        
        for char in target_text:
                stdscr.addstr(char, curses.color_pair(1))
           
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
    
        stdscr.refresh()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    key = stdscr.getkey()
    print(key) 

wrapper(main)
