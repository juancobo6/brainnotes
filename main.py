import json
from itertools import islice


def parse_command(user_input):
    if user_input[0] == "c":
        print("New chapter")
    elif user_input[0] == "s":
        print("New section")


def parse(user_input):
    if user_input[0] == ".":
        parse_command(user_input[1:])
    else:
        print(user_input)


def intro():
    with open("notes.json") as f:
        notes = json.load(f)

    index = 1
    for note in notes:
        print(f"{index}. {note}")
        index += 1

    note_index = int(input("Enter the note number: ")) - 1

    note_title, note_path = next(islice(notes.items(), note_index, note_index + 1))

    print(f"Opening {note_title}...")
    with open(note_path) as f:
        note = json.load(f)

    return note


def main():
    print("Welcome to Brain notes!")

    note = intro()

    while True:
        # Take user input and print it
        user_input = input()
        parse(user_input)


if __name__ == "__main__":
    main()
