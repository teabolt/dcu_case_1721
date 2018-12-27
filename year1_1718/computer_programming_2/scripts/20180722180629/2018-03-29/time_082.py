#!/usr/bin/env python3

class Time(object):
    # Model a 24-hour time
    
    @classmethod
    def seconds_to_time(cls, secs):
        h, m = divmod(secs, 60*60)
        m, s = divmod(m, 60)
        return cls(h, m, s)

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.normalise()

    def __str__(self):
        self.normalise()
        return 'The time is {:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second)

    def __eq__(self, other):
        return self.time_to_seconds() == other.time_to_seconds()

    def __gt__(self, other):
        return self.time_to_seconds() > other.time_to_seconds()

    def __add__(self, other):
        h = self.hour + other.hour
        m = self.minute + other.minute
        s = self.second + other.second
        return Time(h, m, s)

    def __iadd__(self, other):
        self.hour += other.hour
        self.minute += other.minute
        self.second += other.second
        self.normalise()
        return self

    def time_to_seconds(self):
        return self.hour*60*60 + self.minute*60 + self.second

    def normalise(self):
        # Modify instance's values such that time overflows are removed
        # hour = max 23, minute = max 59, second = max 59
        h_secs = 60*60 # seconds in an hour
        m_secs = 60 # seconds in a minute
        secs = self.time_to_seconds()

        h = secs//h_secs # get hours
        secs -= h*h_secs # subtract hours in seconds
        h = h % 24 # remove overflow from hours
        m = secs//m_secs # get minutes
        secs -= m*m_secs # subract minutes
        s = secs # get remaining seconds

        self.hour = h
        self.minute = m
        self.second =s
        return self

        ### could just use divmod() instead in time_to_seconds()
