import time
import os
import random
import select
import sys

class QuantumComputerSimulator:
    def __init__(self):
        self.qubits = [0] * 10
        self.entangled_pairs = []
        self.animation_speed = 0.2
        self.running = True
        self.mode = "normal"

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def generate_frame(self, phase, highlight_pair=None):
        frame = [
            "    ╔════════════════════════════════════════╗    ",
            "    ║       QUANTUM COMPUTER SIMULATOR       ║    ",
            "    ╠════════════════════════════════════════╣    ",
            "    ║      ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐     ║    ",
            "    ║ ┌────┤ Q ├─┤ Q ├─┤ Q ├─┤ Q ├─┤ Q ├────┐║    ",
            "    ║ │    └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘    │║    ",
            "    ║ │    ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐    │║    ",
            "    ║ └────┤ Q ├─┤ Q ├─┤ Q ├─┤ Q ├─┤ Q ├────┘║    ",
            "    ║      └───┘ └───┘ └───┘ └───┘ └───┘     ║    ",
            "    ║     │  │  │  │  │  │  │  │  │  │       ║    ",
            "    ║   ┌─┴──┴──┴──┴──┴──┴──┴──┴──┴──┴───┐   ║    ",
            "    ║   │      Quantum Processor         │   ║    ",
            "    ║   └────────────────────────────────┘   ║    ",
            "    ║     │     │     │     │     │     │    ║    ",
            "    ║   ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐ ┌─┴─┐  ║    ",
            "    ║   │ C │ │ C │ │ C │ │ C │ │ C │ │ C │  ║    ",
            "    ║   └───┘ └───┘ └───┘ └───┘ └───┘ └───┘  ║    ",
            "    ║    Classical Control Electronics       ║    ",
            "    ╠════════════════════════════════════════╣    ",
            "    ║ Mode: {:<34} ║    ".format(self.mode.capitalize()),
            "    ║ Qubits: {:<32} ║    ".format(''.join(map(str, self.qubits))),
            "    ║ Entangled: {:<30} ║    ".format(str(self.entangled_pairs)),
            "    ╚════════════════════════════════════════╝    ",
            "",
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

        return '\n'.join(frame)

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
