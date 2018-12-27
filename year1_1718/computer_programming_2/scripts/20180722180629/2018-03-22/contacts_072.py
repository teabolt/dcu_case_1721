#!/usr/bin/env python3

class Contact(object):
    # Model a contact

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        build = []
        build.append(str(self.name))
        build.append(str(self.phone))
        build.append(str(self.email))
        return ' '.join(build)

class ContactList(object):
    # Model a list of contacts
    
    def __init__(self, d=None):
        # avoid the default mutable argument trap
        if d == None:
            d = {}
        self.d = d

    def __str__(self):
        # string representation of whole contact list
        build = []
        build.append('Contact list')
        n = len('Contact list')
        build.append('-'*n)
        for (k, v) in sorted(self.d.items()): # sorted lexicographically on name
            build.append(v.__str__())
        return '\n'.join(build)

    def add_contact(self, c):
        # Add or update a contact
        self.d[c.name] = c

    def del_contact(self, name):
        # Delete contact with name. No effect if not present
        if name in self.d:
            del self.d[name]

    def get_contact(self, name):
        # String of contact's details. Indicate if not present.
        if name in self.d:
            return self.d[name] # implicitly calls Contact.__str__
        else:
            return '{} : No such contact'.format(name)

def main():
    c1 = Contact('John Millton', '099-99999', 'null@po.int')
    #print(c1)
    c2 = Contact('Joe', '0899432453', 'joejoe00032@gmail.com')
    cl = ContactList({'John Millton':c1})
    #print(cl.d)
    cl.add_contact(c2)
    #print(cl.d)
    cl.del_contact('John Millton')
    #print(cl.d)
    cl.del_contact('Me')
    #print(cl.d)
    #print(cl.get_contact('Joe'))
    #print(cl.get_contact('Rockefeller'))
    cl.add_contact(Contact('Thom', '0982343', 'omron@oil.ie'))
    cl.add_contact(Contact('Thomm', '00', 'a@mai'))
    print(cl)


if __name__ == '__main__':
    main()