#!/usr/bin/env python3

class Triathlete(object):
    # Model a triathlete

    def __init__(self, name, tid):
        """Create instance with name(forename and surname in one string) and an ID number."""
        self.name = name
        self.tid = tid
        self.pdt = {} # per discipline times

    def __str__(self):
        b = []
        b.append('Name: {}'.format(self.name))
        b.append('ID: {}'.format(self.tid))
        b.append('Race time: {}'.format(self.get_rtime()))
        return '\n'.join(b)

    def add_time(self, disc, time):
        """Add a time (in seconds) for a discipline (swimming, cycling, running)"""
        self.pdt[disc] = time

    def get_time(self, disc):
        """Get the time for a discpline"""
        return self.pdt[disc]

    def get_rtime(self):
        """Return the race time (sum of all per discipline times) of a triathlete"""
        return sum(self.pdt.values())

    def __eq__(self, other):
        # self == other
        return self.get_rtime() == other.get_rtime()

    def __lt__(self, other):
        # self < other
        return self.get_rtime() < other.get_rtime()

    def __gt__(self, other):
        # self > other
        return self.get_rtime() > other.get_rtime()
