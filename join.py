#!/usr/bin/env python3

def bsearch(table, colname, val):
    """
    Returns all rows matching val in table[*][colname] == val
    """
    matches = []
    minIndex = 0
    maxIndex = len(table) - 1
    while minIndex <= maxIndex:
        middle = int((minIndex + maxIndex) / 2)
        if table[middle][colname] == val:
            # Left matches
            for i in range(middle-1, minIndex-1, -1):
                if table[i][colname] == val:
                    matches.append(table[i])
                else:
                    break
            matches = matches[::-1]
            for i in range(middle, maxIndex+1):
                if table[i][colname] == val:
                    matches.append(table[i])
                else:
                    break
            break
        elif table[middle][colname] < val:
            minIndex = middle + 1
        else:
            maxIndex = middle - 1
    return matches

def join(table1, table2, colname1, colname2, fast=True):
    """
    For each row in table1, find all rows in table2 for which
    row1[colname1] is equivalent to row2[colname2]
    and add row1 and row2 to matching_rows
    """
    table2 = sorted(table2, key = lambda r: r[colname2])
    if fast:
        return [[row1, row2] for row1 in table1 for row2 in bsearch(table2, colname2, row1[colname1])]
    else:
        return [[row1, row2] for row1 in table1 for row2 in table2 if row1[colname1] == row2[colname2]]

if __name__ == "__main__":
    # Test consistency between algorithms
    # Load (deserialize) tables
    import pickle
    table1 = pickle.load(open("table1", "rb"))
    table2 = pickle.load(open("table2", "rb"))
    size = 2000
    fastAns = join(table1[:size], table2[:size], "zip1", "zip2", True)
    slowAns = join(table1[:size], table2[:size], "zip1", "zip2", False)
    assert(fastAns == slowAns)

