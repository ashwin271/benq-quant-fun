import time
import os
import random

def clear_console():
    """Clear the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_frame(phase):
    """Generate a single frame of the animation."""
    frame = [
        "    ╔════════════════════════════════════════╗    ",
        "    ║    ___  _   _  ___  _   _ _____ _   _  ║    ",
        "    ║   / _ \\| | | |/ _ \\| \\ | |_   _| | | | ║    ",
        "    ║  | | | | | | | | | |  \\| | | | | | | | ║    ",
        "    ║  | |_| | |_| | |_| | |\\  | | | | |_| | ║    ",
        "    ║   \\__\\_\\\\___/ \\___/|_| \\_| |_|  \\___/  ║    ",
        "    ║   ____   ___  __  __ ____  _   _ _____ ║    ",
        "    ║  / ___| / _ \\|  \\/  |  _ \\| | | |_   _|║    ",
        "    ║ | |    | | | | |\\/| | |_) | | | | | |  ║    ",
        "    ║ | |___ | |_| | |  | |  __/| |_| | | |  ║    ",
        "    ║  \\____  \\___/|_|  |_|_|    \\___/  |_|  ║    ",
        "    ║                                        ║    ",
        "    ║      ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐     ║    ",
        "    ║ ┌────┤ Q ├─┤ Q ├─┤ Q ├─┤ Q ├─┤ Q ├────┐║    ",
        "    ║ │    └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘    │║    ",
        "    ║ │    ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐    │║    ",
        "    ║ └────┤ Q ├─┤ Q ├─┤ Q ├─┤ Q ├─┤ Q ├────┘║    ",
        "    ║      └───┘ └───┘ └───┘ └───┘ └───┘     ║    ",
        "    ║     │  │  │  │  │  │  │  │  │  │       ║    ",
        "    ║   ┌─┴──┴──┴──┴──┴──┴──┴──┴──┴──┴─┐     ║    ",
        "    ║   │      Quantum Processor       │     ║    ",
        "    ║   └────────────────────────────────┘   ║    ",
        "    ║     │     │     │     │     │     │    ║    ",
        "    ║   ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐  ║    ",
        "    ║   │ C │ │ C │ │ C │ │ C │ │ C │ │ C │  ║    ",
        "    ║   └───┘ └───┘ └───┘ └───┘ └───┘ └───┘  ║    ",
        "    ║    Classical Control Electronics       ║    ",
        "    ╚════════════════════════════════════════╝    "
    ]
    
    # Animate qubits
    qubit_chars = ['-', '\\', '|', '/']
    for i in [13, 16]:  # Lines with qubits
        for j in [11, 17, 23, 29, 35]:  # Qubit positions
            frame[i] = frame[i][:j] + qubit_chars[(phase + j) % 4] + frame[i][j+1:]
    
    # Animate connections
    connection_chars = ['│', '┼', '─', '┼']
    for i in range(18, 22):  # Lines with connections
        for j in range(10, 40):  # Connection area
            if frame[i][j] in '│─┼':
                frame[i] = frame[i][:j] + connection_chars[(phase + j) % 4] + frame[i][j+1:]
    
    # Animate classical control
    for i in range(24, 26):  # Lines with classical control
        for j in range(7, 44, 6):  # Control unit positions
            if random.random() < 0.3:  # 30% chance to change
                frame[i] = frame[i][:j] + random.choice(['0', '1']) + frame[i][j+1:]
    
    return '\n'.join(frame)

def animate_quantum_computer():
    """Animate the quantum computer ASCII art."""
    try:
        phase = 0
        while True:
            clear_console()
            print(generate_frame(phase))
            phase = (phase + 1) % 4
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nAnimation stopped.")

if __name__ == "__main__":
    animate_quantum_computer()
