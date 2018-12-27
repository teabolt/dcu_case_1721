from collections import namedtuple

Module = namedtuple('Module', 'code title ects')

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
               'CA106': Module('CA106', 'Web Design', 5),
               'CA115': Module('CA115', 'Digital Innovation', 5),
               'CA116': Module('CA116', 'Computer Programming I', 10),
               'CA117': Module('CA117', 'Computer Programming II', 10),
               'CA169': Module('CA169', 'Networks and Internet', 5),
               'CA170': Module('CA170', 'Operating Systems', 5),
               'CA172': Module('CA172', 'Problem Solving', 5),
               'MS121': Module('MS121', 'IT Mathematics', 10)}

class Student(object):

    def __init__(self, idnum, surname, firstname):
        self.idnum = idnum
        self.surname = surname
        self.firstname = firstname
        self.mods = CA1_MODULES # modules the student takes
        # dictionary comprehension
        # give a mark of 0 by default for each module (referenced by module code)
        self.marks = {code: 0 for code in self.mods.keys()} 

    def __str__(self):
        name = '{} : {} {}'.format(self.idnum,
                                   self.firstname,
                                   self.surname)
        uline = '-' * len(name)
        # list comprehension gives the string of all the results
        # sorted by the module code (lexicographically)
        results =  '\n'.join([
                              code + ' : ' + self.mods[code].title + ' : ' + str(self.marks[code])
                              for code in sorted(self.mods.keys())
                              ])
        pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
        if self.passed():
            outcome = 'Pass'
        elif self.passed_by_compensation():
            outcome = 'Pass by compensation'
        else:
            outcome = 'Fail'

        return '\n'.join([name, uline, results, pm, outcome])

    def add_mark(self, code, mark):
        # Add/update the mark a student got for a module
        self.marks[code] = mark

    def precision_mark(self):
        # Return the precision mark for the year
        # Precision mark is the *weighted* average of all the module marks
        # Weight of each module mark is proportional to the credits of the module
        total = 0
        for (code, mark) in self.marks.items():
            # mark*weight(credits)
            total += mark * self.mods[code].ects
        weights = [mod.ects for mod in self.mods.values()]
        return total / sum(weights)

    def passed(self):
        # A student passes if all of the marks are equal to or above 40
        for m in self.marks.values():
            if m < 40:
                return False
        return True

    def passed_by_compensation(self):
        # A student passes by compensation under three conditions

        # 1. the precision mark is at minimum 45%
        if self.precision_mark() < 45:
            return False

        # 2. maximally 1/6 of the credits have been failed
        total_ects = sum([mod.ects for mod in self.mods.values()])
        ects_failed = sum([self.mods[code].ects for code in self.mods
                        if self.marks[code] < 40])
        if 1/6 < ects_failed/total_ects:
            return False

        # 3. each mark obtained is 35%+
        for m in self.marks.values():
            if m < 35:
                return False        

        return True