class Letter:
    def __init__(self, letter_id, child_name, age):
        self.id = letter_id
        self.child_name = child_name
        self.age = age
        self._approved = None
        self.toys = []

    def set_approved(self, status):
        self._approved =status

    def get_approved(self):
        return self._approved
    
    def add_toys(self, toy):
        self.toys.appemd(toy)


