class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name, phone):
        self.contacts[name] = phone
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
    def search_contact(self, name):
        return self.contacts.get(name, "Not found")
