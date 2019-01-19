"""A function represents a module"""

# Cohesion examples


# 7. Coincidental

def MiscProcessing(store_to):
    i = 10
    if store_to is not None:
        store_to = i
    else:
        for i in range(10):
            store_to = i
        i = i + 1
    return [x**2 for x in range(10)]


# 6. Logical

def WriteOutput(data, output_location, output_type, output_buffer_size):
    """Shared data structure output_buffer, multiple functions - pick 1, dummy parameter 'output_type'"""
    output_buffer = []*output_buffer_size
    if output_location is 'file':
        f = open('output.txt', 'w')
        for bit in data:
            output_buffer.append(bit)
        f.write(output_buffer)
    elif output_location is 'console':
        if output_type == 'str':
            for char in data:
                output_buffer.append(char)
            print(output_buffer)
        elif output_type == 'int':
            output_buffer.append(data)
            print(output_buffer)


WriteOutput([2, 3, 4], 'file', None, 15)
WriteOutput('ababa', 'console', 'str', 10)


# 5. Classical

def initialiseGame():
    data_buffer = initialiseBuffer()    
    stripe_count = initialiseStripes()
    loop_invariant = initialiseInvariant()
    return (data_buffer, stripe_count, loop_invariant)


# 4. Procedural

def stopPod(distance, speed, health):
    if not health or (distance < 500 and speed > 0):
        motorsOff()
        brakesOn()
        setState(state=3)
        return True
    else:
        return False 


# 3. Communicational

def daysUpdate():
    table = getTable()
    writeProfit(table)
    writeCustomers(table)
    writeStock(table)
    writeMeta(table)


# 2. Informational

class List(object):
    def __init__(self):
        self.list = []

    def listAppend(self, data):
        self.list.append(data)

    def listDelete(self):
        self.list.pop()


# 1. Functional

def calculateFactorial(n):
    total = 1
    while 0 < n:
        total *= n
        n -= 1
    return total



# Coupling


# 6. Content

def negateList(lst):
    lst.list = [-x for x in lst.list]


# 5. Common

table = {
    'filesystem':['ntfs', 'ext'],
    'os':['windows', 'linux', 'mac'],
    10: 'ten',
    'code':-31234,
    'floats':-1.0,
}
secret = 431234342

def writeFile():
    global table
    f = open()
    for x in table['filesystem']:
        for y in table['os']:
            f.write(fs=x, os=y)


def checkNumberCode():
    global table
    try:
        global secret
        return (table[10]*2, abs(table['code']), table['floats'], secret)
    except NameError:
        return (table[10]*2, abs(table['code']), table['floats'], 0) # faked the 'secret' structure


def hackTheSystem():
    global secret
    table = enterPasswordVault(secret)
    getAllData(table)


# 4. External

codes = [10, 32, 4532, 123]
names = ['aba', 'baba', 'lala']

def codeName():
    global codes
    global names
    return (codes[0]*2, names[0].capitalize())

def formalName():
    global names
    return names[0].capitalize() + ' ' names[1].upper()


# 3. Control

def controller():
    value = controlled(want='height', output=False)
    if value < 10:  # called controls the caller - even worse!
        return 0
    elif 10 < value:
        return 1
    else:
        return -1

def controlled(want, output):
    if want = 'height':
        if output:
            print(10)
        return 10
    elif want = 'width':
        if output:
            print(5)
        return 5
    else:
        if output:
            print(0)
        return 0


# 2. Stamp

# list_params is the shared non-global D.S.

def transformList(lst, list_params):
    case = list_params['case']
    lst = getattr(lst, case)
    alphabet = list_params['alphabet']
    lst = getattr(lst, translate)
    return lst


def showListConfig(list_params):
    return (list_params['codec'], list_params['datetime'])


# 1. Data

def generateBankDetails(customer_reference):
    number = calculateBankNumber(customer_reference.customer_name, customer_reference.customer_dob)
    balance = retrieveBalance(customer_reference.customer_id)
    return (number, balance)

def calculateBankNumber(customer_name, customer_dob):
    pass

def retrieveBalance(customer_id):
    pass