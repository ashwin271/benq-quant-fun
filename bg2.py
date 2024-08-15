import curses
import time

def draw_quantum_computer_art(stdscr, frame):
    stdscr.clear()

    quantum_computer_frames = [
        r"""
          ________            
         /  _____/_____    _____   ____  
        /   \  ___\__  \  /     \_/ __ \ 
        \    \_\  \/ __ \|  Y Y  \  ___/ 
         \______  (____  /__|_|  /\___  >
                \/     \/      \/     \/ 
         ________                     
        /  _____/_____    _____   ____  
       /   \  ___\__  \  /     \_/ __ \ 
       \    \_\  \/ __ \|  Y Y  \  ___/ 
        \______  (____  /__|_|  /\___  >
               \/     \/      \/     \/ 
        """,
        r"""
          ________            
         /  _____/_____    _____   ____  
        /   \  ___\__  \  /     \_/ __ \ 
        \    \_\  \/ __ \|  Y Y  \  ___/ 
         \______  (____  /__|_|  /\___  >
                \/     \/      \/     \/ 
         ________                     
        /   \  ___\__  \  /     \_/ __ \ 
        \    \_\  \/ __ \|  Y Y  \  ___/ 
        \______  (____  /__|_|  /\___  >
               \/     \/      \/     \/ 
          ________            
         /  _____/_____    _____   ____  
        /   \  ___\__  \  /     \_/ __ \ 
        \    \_\  \/ __ \|  Y Y  \  ___/ 
         \______  (____  /__|_|  /\___  >
                \/     \/      \/     \/ 
        """,
        r"""
          ________            
         /  _____/_____    _____   ____  
        /   \  ___\__  \  /     \_/ __ \ 
        \    \_\  \/ __ \|  Y Y  \  ___/ 
         \______  (____  /__|_|  /\___  >
                \/     \/      \/     \/ 
         ________                     
        /  _____/_____    _____   ____  
        /   \  ___\__  \  /     \_/ __ \ 
        \    \_\  \/ __ \|  Y Y  \  ___/ 
        \______  (____  /__|_|  /\___  >
               \/     \/      \/     \/ 
        """
    ]

    stdscr.addstr(0, 0, quantum_computer_frames[frame])
    stdscr.refresh()


def animate_quantum_computer(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    frame = 0

    while True:
        draw_quantum_computer_art(stdscr, frame)
        frame = (frame + 1) % 3
        time.sleep(0.2)

        # Break loop on user input
        if stdscr.getch() != -1:
            break

curses.wrapper(animate_quantum_computer)
