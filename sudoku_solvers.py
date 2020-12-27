def complete_sequence(sequence):
    try:
        offset = sequence.index(0)
    except ValueError:
        return # no zero in list => already complete
    
    missing_value = 0   
    for i in [1,2,3,4]:
        if i not in sequence:
            missing_value = i
    sequence[offset] = missing_value
    return sequence

def is_sequence_complete(sequence):
    return sum(sequence) == 10