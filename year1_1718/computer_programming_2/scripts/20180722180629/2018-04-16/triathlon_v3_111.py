#!/usr/bin/env python3

class Triathlete(object):
    """Model a triathlete"""

    def __init__(self, name, tid):
        """Create instance with name(forename and surname in one string) and an ID number."""
        self.name = name
        self.tid = tid
        self.pdt = {} # per discipline times

    def __str__(self):
        """String representation returning a triathlete's attributes, per line:
        the name, id, and race time(all the per-discipline times summed up)"""
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

    def best(self):
        """Return the triathlate object with the lowest(best) summed up per-discipline time."""
        return min(self.d.values(), key=Triathlete.get_rtime)

    def worst(self):
        """Return the triathlete with the longest(worst) performing time."""
        return max(self.d.values(), key=Triathlete.get_rtime)