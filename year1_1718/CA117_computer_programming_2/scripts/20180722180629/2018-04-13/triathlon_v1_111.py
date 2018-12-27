#!/usr/bin/env python3

class Triathlete(object):
    """Model a triathlete"""

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