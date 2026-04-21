import tkinter as tk
from ui.gui import CharacterCreatorGUI  # pylint: disable=import-error
# pylint herjaa virheestä, koska minulla on Windows kone, joten poistin käytöstä...


def main():
    root = tk.Tk()
    CharacterCreatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
