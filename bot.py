from collections import UserDict


class AddressBook(UserDict):
    
    
    def add_record(self, record):
        
        self.data[record.name.value] = record


class Field:
    pass


class Name(Field):

    def __init__(self, value):

        self.value = value


class Phone(Field):
   
   def __init__(self, value):
       
       self.value = value


class Record:


    def __init__(self, name, phone):

        self.name = name
        self.phones = [phone]


    def add_phone(self, phone):

        self.phones.append(phone)


    def delete_phone(self, phone):

        self.phones.remove(phone)

    
    def edit_phone(self, phone, new_phone):

        index = self.phones.index(phone)
        self.phones[index] = new_phone


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')