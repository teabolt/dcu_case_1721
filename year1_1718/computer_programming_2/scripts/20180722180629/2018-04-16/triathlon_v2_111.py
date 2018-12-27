#!/usr/bin/env python3

class Triathlete(object):
    # Model a triathlete

    def __init__(self, name, tid):
        """Create instance with name(forename and surname in one string) and an ID number."""
        self.name = name
        self.tid = tid

    def __str__(self):
        b = []
        b.append('Name: {}'.format(self.name))
        b.append('ID: {}'.format(self.tid))
        return '\n'.join(b)

class Triathlon(object):
    """Model a collection of triathletes"""

    def __init__(self):
        """Constructor -> empty triathlon"""
        self.d = {}

    def add(self, t):
        """Add a triathlete t to the triathlon"""
        self.d[t.tid] = t # map id to object

    def remove(self, tid):
        """Remove a triathlete with the ID 'tid' from the triathlon"""
        del self.d[tid]

    def lookup(self, tid):
        """Look for and return the triathlete (instance) with the ID 'tid'. 
        Else return 'None'"""
        if tid in self.d:
            return self.d[tid]
        else:
            return None

    def sorter(t):
        # Internal key function to sort by a triathlete's attribute
        return t[1].name # sort by name

    def __str__(self):
        """String representation. Print each triathlete, name and id"""
        b = []
        for (tid, obj) in sorted(self.d.items(), key=Triathlon.sorter):
            b.append(obj.__str__()) # call triathlete's __str__
        return '\n'.join(b)