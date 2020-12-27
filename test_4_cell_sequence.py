import unittest
from parameterized import parameterized

def complete(sequence):
    try:
        offset = sequence.index(0)
    except ValueError:
        return # no zero in list => already complete
    
    missing_value = 0   
    for i in [1,2,3,4]:
        if i not in sequence:
            missing_value = i
    sequence[offset] = missing_value

def is_complete(sequence):
    return sum(sequence) == 10

class AFourCellSequenceWithOneMissingNumber(unittest.TestCase):
    @parameterized.expand([
        ([[1,2,0,4],]),
        ([[1,0,4,3],]),
        ([[0,3,4,2],]),
        ([[0,3,1,2],]),
    ])
    def test_can_be_completed_1(self, sequence):
        complete(sequence)
        self.assertTrue(is_complete(sequence), 'Sequence is not complete' + str(sequence))

class AFourCellSequenceWithTwoMissingNumbers(unittest.TestCase):
    @parameterized.expand([
        ([[1,2,0,0],]),
    ])
    def test_cannot_be_completed(self, sequence):
        complete(sequence)
        self.assertFalse(is_complete(sequence), 'Sequence looks to be complete')

class AFourCellSequenceWithNoMissingNumbers(unittest.TestCase):
    @parameterized.expand([
        ([[1,2,4,3],]),
    ])
    def test_is_already_completed(self, sequence):
        complete(sequence)
        self.assertTrue(is_complete(sequence), 'Sequence is not complete' + str(sequence))

if __name__ == '__main__':
    unittest.main()

