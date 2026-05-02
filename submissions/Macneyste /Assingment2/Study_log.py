# Author: Macneyste
# Description: A simple study log program that lets the user add and view
# one-line notes. Notes are saved to a text file and loaded on startup.

# ── Section 4: Functions ──────────────────────────────────────────────────────

def load_notes(path):
    """Read notes from file and return them as a list of strings.
    Returns an empty list if the file does not exist yet."""
    # Section 5: try/except FileNotFoundError + with open + encoding
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    """Write every note in the list to the file, one note per line."""
    # Section 5: with open for writing + encoding
    with open(path, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")


def main():
    # Section 1: variables, print, input
    FILE = "notes.txt"

    # Optional: ask for the user's name once
    name = input("What is your name? ").strip()
    if name == "":
        name = "Student"
    print(f"Welcome, {name}!\n")

    # Section 3: a list to hold all notes
    notes = load_notes(FILE)

    # Section 4 / Section 3: while loop + menu
    while True:
        # Section 1: print the menu
        print("1) Add note  2) List  3) Quit")
        choice = input("Pick: ").strip()

        # Section 2: if / elif / else on the input string
        if choice == "1":
            note = input("Note: ").strip()
            notes.append(note)          # Section 3: list append

        elif choice == "2":
            if notes:
                for note in notes:      # Section 3: for loop
                    print(note)
            else:
                print("No notes yet.")

        elif choice == "3":
            save_notes(FILE, notes)     # Section 5: save before quitting
            print("Bye!")
            break                       # exit the while loop

        else:
            print("Please enter 1, 2, or 3.")

        print()  # blank line for readability


# Section 4: entry point guard
if __name__ == "__main__":
    main()
