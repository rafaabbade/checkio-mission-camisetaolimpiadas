"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [4, [1, 1, 2, 2], 2, 2],
            "answer": "S"
        },
        {
            "input": [5, [1, 1, 1, 2, 2], 2, 2],
            "answer": "N"
        },
        {
            "input": [3, [1, 1, 1], 3, 0],
            "answer": "S"
        }
    ],
    "Extra": [
        {
            "input": [3, [2, 2, 2], 0, 3],
            "answer": "S"
        },
    ]
}
