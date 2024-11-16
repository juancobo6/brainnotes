import json
from itertools import islice

from bond_brainnotes import Bond, Prompt

NOTES_PATH = r"C:\Users\JuanC\Documents\Projectos\brainnotes\notes"


class Brainnote:
    def __init__(self, note, path):
        self.note = note
        self.path = path
        self.index = self.get_index()


    def get_index(self):
        if not self.note["content"]:
            return 0
        else:
            return self.note["content"][-1]["index"] + 1


    def write_note(self):
        while True:
            user_input = input("> ")
            if user_input == "":
                continue
            elif user_input[0:2] == (".1" or ".2" or ".3"):
                self.parse_title(user_input)
            elif user_input[0:2] == ".e":
                break
            else:
                self.parse_paragraph(user_input)
        print("Applying AI to the note...")

        self.apply_ai()

        with open(self.path, 'w') as f:
            json.dump(self.note, f, indent=4)


    def parse_title(self, user_input):
        title = user_input[3:]
        grade = int(user_input[1])
        self.note["content"].append({"index": self.index, "type": str(grade), "content": title, "summary": ""})
        self.index += 1


    def parse_paragraph(self, user_input):
        self.note["content"].append({"index": self.index, "type": "4", "content": user_input, "revision": ""})
        self.index += 1


    def apply_ai(self):
        raise NotImplementedError



def intro():
    with open("notes.json") as f:
        notes = json.load(f)

    index = 1
    for note in notes:
        print(f"{index}. {note}")
        index += 1
    print("n. New note")

    note_index = input("Enter the note number: ")

    if note_index == "n":
        note_title = input("Enter the note title: ")
        note_context = input("Enter the note context: ")
        notes[note_title] = f"{NOTES_PATH}\\{note_title}.json"
        with open("notes.json", "w") as f:
            json.dump(notes, f, indent=4)
        new_note = {"title": note_title, "context": note_context, "content": []}
        with open(f"{NOTES_PATH}\\{note_title}.json", "w") as f:
            json.dump(new_note, f, indent=4)
        return {"title": note_title, "content": []}, f"{NOTES_PATH}\\{note_title}.json"

    else:
        note_index = int(note_index) - 1
        note_title, note_path = next(islice(notes.items(), note_index, note_index + 1))

        print(f"Opening {note_title}...")
        with open(note_path) as f:
            note = json.load(f)

        return note, note_path


def main():
    print("Welcome to Brain notes!")

    note, path = intro()

    bn = Brainnote(note, path)

    bn.write_note()


if __name__ == "__main__":
    main()