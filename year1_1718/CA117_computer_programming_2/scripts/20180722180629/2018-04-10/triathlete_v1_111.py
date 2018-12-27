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