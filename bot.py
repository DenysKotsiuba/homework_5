from collections import UserDict


class AddressBook(UserDict):
    
    
    def add_record(self, record):
        
        self.data[record.name] = record.phones


class Field:
    pass


class Name(Field):

    def __init__(self, name):

        self.name = name


class Phone(Field):
   
   def __init__(self, phone):
       
       self.phone = phone


class Record:


    def __init__(self, name):

        self.name = name
        self.phones = []


    def add_phone(self, phone):

        self.phones.append(phone)


    def delete_phone(self, phone):

        self.phones.remove(phone)

    
    def edit_phone(self, phone, new_phone):

        index = self.phones.index(phone)
        self.phones[index] = new_phone
