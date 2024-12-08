import json
import csv
from letter import Letter
from toy import Toy

class Program:
    def __init__(self):
        self.letters = []

    def log_action(self, action):
        with open("logs/ProgramLog.txt", "a") as log_file:
            log_file.write(f"{action}\n")

    def openLetterData(self, filename="data/Letters.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for item in data:
                    toys = [Toy(toy["name"], toy["category"], toy["description"]) for toy in item["toys"]]
                    letter = Letter(item["id"], item["first_name"], item["last_name"], item["age"], item.get("approved"))
                    for toy in toys:
                        letter.add_toy(toy)
                    self.letters.append(letter)
            self.log_action("Loaded letter data")
        except FileNotFoundError:
            print(f"File not found: {filename}")

    def exportChildrenList(self, filename="data/ChildrenListTemplate.csv"):
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Letter ID", "Full Name", "Nice"])
                for letter in self.letters:
                    writer.writerow([letter.id, f"{letter.first_name} {letter.last_name}", ""])
            self.log_action("Exported children list")
        except Exception as e:
            print(f"Error exporting children list: {e}")

    def importChildrenData(self, filename="data/ChildrenList.csv"):
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    letter_id = int(row["Letter ID"])
                    nice_status = row["Nice"].strip().lower()
                    approved = nice_status == "true"
                    for letter in self.letters:
                        if letter.id == letter_id:
                            letter.set_approved(approved)
            self.log_action("Imported children data")
        except FileNotFoundError:
            print(f"File not found: {filename}")

    def exportToyManufacturingData(self, filename="data/RequestedToys.csv"):
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Category", "Description"])
                for letter in self.letters:
                    for toy in letter.toys:
                        writer.writerow([toy.name, toy.category, toy.description])
            self.log_action("Exported toy manufacturing data")
        except Exception as e:
            print(f"Error exporting toy data: {e}")

    def saveLetterData(self, filename="data/Letters.json"):
        try:
            data = []
            for letter in self.letters:
                letter_data = {
                    "id": letter.id,
                    "first_name": letter.first_name,
                    "last_name": letter.last_name,
                    "age": letter.age,
                    "approved": letter.get_approved(),
                    "toys": [{"name": toy.name, "category": toy.category, "description": toy.description} for toy in letter.toys]
                }
                data.append(letter_data)
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            self.log_action("Saved letter data")
        except Exception as e:
            print(f"Error saving letter data: {e}")

    def run(self):
        print("Program started")
        self.openLetterData()
        self.exportChildrenList()
        self.exportToyManufacturingData()
        self.saveLetterData()
        print("Program finished")

if __name__ == "__main__":
    program = Program()
    program.run()
