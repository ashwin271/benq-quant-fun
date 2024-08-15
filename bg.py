import time
import os
import random
import sys
import select

class QuantumComputerSimulator:
    def __init__(self):
        self.qubits = [0] * 10
        self.entangled_pairs = []
        self.animation_speed = 0.2
        self.running = True
        self.mode = "normal"

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def matrix_background(  
                            self, 
                            columns=os.get_terminal_size().columns,
                            matrix_characters = "01"
                          ):
        matrix_effect = [random.choice(matrix_characters) for _ in range(columns)]
        return ''.join(matrix_effect)

    def show_menu(self):
        while True:
            self.clear_console()

            start_message = "   Press Enter to Start   "
            vertical_padding = (os.get_terminal_size().lines - 5) // 2 
            horizontal_padding = (os.get_terminal_size().columns - len(start_message)) // 2

            # Show Matrix-like background
            for _ in range(vertical_padding):
                print(self.matrix_background())

            # Show "Start" button centered   
            print("\n")
            print(self.matrix_background(horizontal_padding,"<>") + start_message+self.matrix_background(horizontal_padding,"<>"))
            print("\n")

            for _ in range(vertical_padding-1):
                print(self.matrix_background())

            # Handle user input
            rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
            if rlist:
                key = sys.stdin.readline().strip().lower()
                if key == '':
                    break

    def generate_frame(self, phase, highlight_pair=None):

        x='BENQ'
        a, b, c, d = phase%4, (phase+1)%4, (phase+2)%4, (phase+3)%4

        benq_computer= [
            '''              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.                   ''',
            '''         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||                  ''',
            '''         !...:!TVBBBRPFT||||||||||!!^^""'   ||||                  ''',
            '''         !.......:!?|||||!!^^""'            ||||                  ''',
            '''         !.........||||                     ||||                  ''',
            '''         !.........||||                     ||||                  ''',
            f'''         !.........||||                   {x[d]} ||||                  ''',
            f'''         !.........||||             {x[c]}       ||||                  ''',
            f'''         !.........||||       {x[b]}             ||||                  ''',
            f'''         !.........|||| {x[a]}                   ||||                  ''',
            '''         `.........||||                    ,||||                  ''',
            '''          .;.......||||               _.-!!|||||                  ''',
            '''   .,uodWBBBBb.....||||       _.-!!|||||||||!:"                   ''',
            '''!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....              ''',
            '''!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.            ''',
            '''!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.          ''',
            '''!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.        ''',
            '''!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.  ''',
            '''`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.''',
            '''  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^''',
            '''    `........::::::::::::::::;iof688888888888888888888b.     `    ''',
            '''      `......:::::::::;iof688888888888888888888888888888b.        ''',
            '''        `....:::;iof688888888888888888888888888888888899fT!       ''',
            '''          `..::!8888888888888888888888888888888899fT|!^""         ''',
            '''            `' !!988888888888888888888888899fT|!^""""             ''',
        ]

        frame = [
            "    ╔════════════════════════════════════════╗        ",
            "    ║       QUANTUM COMPUTER SIMULATOR      ║        ",
            "    ╠════════════════════════════════════════╣        ",
            "    ║      ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐     ║        ",
            "    ║ ┌────┤ Q ├─┤ Q ├─┤ Q ├─┤ Q ├─┤ Q ├────┐║        ",
            "    ║ │    └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘    │║        ",
            "    ║ │    ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐    │║        ",
            "    ║ └────┤ Q ├─┤ Q ├─┤ Q ├─┤ Q ├─┤ Q ├────┘║        ",
            "    ║      └───┘ └───┘ └───┘ └───┘ └───┘     ║        ",
            "    ║     │  │  │  │  │  │  │  │  │  │       ║        ",
            "    ║   ┌─┴──┴──┴──┴──┴──┴──┴──┴──┴──┴───┐   ║        ",
            "    ║   │      Quantum Processor         │   ║        ",
            "    ║   └────────────────────────────────┘   ║        ",
            "    ║     │     │     │     │     │     │    ║        ",
            "    ║   ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐  ║        ",
            "    ║   │ C │ │ C │ │ C │ │ C │ │ C │ │ C │  ║        ",
            "    ║   └───┘ └───┘ └───┘ └───┘ └───┘ └───┘  ║        ",
            "    ║    Classical Control Electronics       ║        ",
            "    ╠════════════════════════════════════════╣        ",
            "    ║ Mode: {:<32} ║        ".format(self.mode.capitalize()),
            "    ║ Qubits: {:<30} ║        ".format(''.join(map(str, self.qubits))),
            "    ║ Entangled: {:<27} ║        ".format(str(self.entangled_pairs)),
            "    ╚════════════════════════════════════════╝        ",
            "                                                      ",
            "Controls: Q-Quit, S-Speed, M-Mode, E-Entangle, R-Reset"
        ]

        qubit_chars = ['-', '\\', '|', '/']
        for i in [4, 7]:  # Lines with qubits
            for j, qubit in enumerate([11, 17, 23, 29, 35]):  # Qubit positions
                char = qubit_chars[(phase + j) % 4] if self.qubits[j] or self.qubits[j+5] else ' '
                if highlight_pair and (j in highlight_pair or j+5 in highlight_pair):
                    char = '⚛️'
                frame[i] = frame[i][:qubit] + char + frame[i][qubit+1:]

        connection_chars = ['│', '┼', '─', '┼']
        for i in range(9, 13):  # Lines with connections
            for j in range(10, 40):  # Connection area
                if frame[i][j] in '│─┼':
                    frame[i] = frame[i][:j] + connection_chars[(phase + j) % 4] + frame[i][j+1:]

        for i in range(15, 17):  # Lines with classical control
            for j in range(7, 44, 6):  # Control unit positions
                if random.random() < 0.3:  # 30% chance to change
                    frame[i] = frame[i][:j] + random.choice(['0', '1']) + frame[i][j+1:]

        # Add visual feedback for different modes
        mode_indicator = "⚛️ " if self.mode == "entanglement" else "🔬 "
        frame[1] = frame[1][:6] + mode_indicator + frame[1][8:]

        out_frame = [i + j for i, j in zip(benq_computer,frame)]

        # Add vertical padding 
        

        # Add horizontal padding

        return '\n'.join(out_frame)

    def toggle_qubit(self, index):
        self.qubits[index] = 1 - self.qubits[index]

    def entangle_qubits(self):
        available = [i for i in range(10) if i not in sum(self.entangled_pairs, [])]
        if len(available) >= 2:
            pair = random.sample(available, 2)
            self.entangled_pairs.append(pair)
            self.qubits[pair[0]] = self.qubits[pair[1]] = 1
            self.entanglement_animation(pair)

    def entanglement_animation(self, pair):
        for _ in range(5):  # Short animation loop
            for phase in range(4):
                self.clear_console()
                print(self.generate_frame(phase, highlight_pair=pair))
                time.sleep(self.animation_speed / 2)

    def handle_input(self, key):
        if key == 'q':
            self.running = False
        elif key == 's':
            self.animation_speed = 0.5 if self.animation_speed == 0.2 else 0.2
        elif key == 'm':
            self.mode = "entanglement" if self.mode == "normal" else "normal"
        elif key == 'e' and self.mode == "entanglement":
            self.entangle_qubits()
        elif key == 'r':
            self.qubits = [0] * 10
            self.entangled_pairs = []
        elif key.isdigit():
            index = int(key)
            if 0 <= index <= 9:
                self.toggle_qubit(index)

    def run(self):
        self.show_menu()  # Show the menu first
        phase = 0
        while self.running:
            self.clear_console()
            print(self.generate_frame(phase))
            phase = (phase + 1) % 4

            # Non-blocking input
            rlist, _, _ = select.select([sys.stdin], [], [], self.animation_speed)
            if rlist:
                key = sys.stdin.readline().strip().lower()
                self.handle_input(key)

if __name__ == "__main__":
    simulator = QuantumComputerSimulator()
    simulator.run()
