from stack_092 import Stack

# righty and lefty brackets
d = {
    ')':'(',
    '}':'{',
    ']':'[',
}

def matcher(line):
    # each bracket is characterised by: whether it's lefty or righty, its bracket type
    # brackets 'match' if lefty of a type matches a righty of the same type
    # brackets that match must be at same 'level' (if inside other nested brackets)

    s = Stack() # use a stack to handle nested brackets
    # go through each bracket
    for b in line:
        # bracket is a lefty ({[
        if b in d.values():
            s.push(b) # add bracket to top of stack
        # bracket must be a righty after this )}]
        # if stack is empty then immediatelly the righty 
        # doesn't have a preceding lefty
        elif s.is_empty():
            return False
        # there is a preceding lefty, so check if the lefty is the right one
        # (matching pairs)
        elif d[b] == s.top():
            # brackets match, so remove the most recent lefty
            # (most nested brackets pair with each other)
            s.pop()
            # give way to checking other lefties 
            # (move up a level of nested brackets)
        # bracket pair types did not match
        else:
            return False
    # final check just in case the input had all lefties and no righties
    return s.is_empty()