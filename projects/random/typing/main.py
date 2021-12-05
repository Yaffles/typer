from typingGame import main
from curses import wrapper


#ios
def main2(stdscr):
    """Gives option to start different programs"""
    main(stdscr)


wrapper(main2)

# Comment