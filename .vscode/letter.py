class Letter:
    def __init__(self, letter_id, first_name, last_name, age, approved=None):
        self.id = letter_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self._approved = approved
        self.toys = []

    def set_approved(self, status):
        self._approved = status

    def get_approved(self):
        return self._approved

    def add_toy(self, toy):
        self.toys.append(toy)

    def __repr__(self):
        return f"Letter(id={self.id}, name={self.first_name} {self.last_name}, approved={self._approved}, toys={self.toys})"
