from itertools import repeat


s = "      Your Board  \t\t       Enemy Board\n\r"
s += f"{1}\t\t"
s += f"{2}\t\t"



def create_empty_board():
    """
    Returns a 10x10 array of zeros.
    """
    return [10 * [0] for _ in repeat(0, 10)]

print(create_empty_board())
