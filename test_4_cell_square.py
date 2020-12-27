import unittest
import sudoku_solvers
from parameterized import parameterized

def complete_square(square):
    completed_sequence = sudoku_solvers.complete_sequence(square[0] + square[1])
    square[0][0] = completed_sequence[0]
    square[0][1] = completed_sequence[1]
    square[1][0] = completed_sequence[2]
    square[1][1] = completed_sequence[3]

def is_square_complete(square):
    return sudoku_solvers.is_sequence_complete(square[0] + square[1])

class AFourCellSquareWithOneMissingNumber(unittest.TestCase):
    @parameterized.expand([
        ([[[1,2],[0,4]],]),
    ])
    def test_can_be_completed(self, square):
        print('Square to complete: ' + str(square))
        complete_square(square)
        print('Completed square: ' + str(square))
        self.assertTrue(is_square_complete(square), 'Square is not complete' + str(square))