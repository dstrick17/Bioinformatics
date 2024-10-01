def NW(seq1, seq2):
    # Create matrix of sequence 1 by sequence 2 and initialize it to zero
    m = [[0 for _ in range(len(seq2)+1)] for _ in range(len(seq1)+1)]
    # for i rows and j columns, decrease by -1 for the first row and column
    for i in range(len(seq1)+1):
        m[i][0] = 0 - i
    for j in range(len(seq2)+1):
        m[0][j] = 0 - j


    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            match = m[i-1][j-1] + (1 if seq1[i-1] == seq2[j-1] else -1) # else = mismatch
            delete = m[i-1][j] - 1
            insert = m[i][j-1] - 1
            m[i][j] = max(match, delete, insert)

    # Print the matrix in a readable format with sequences on axes
    print("    ", end="")  # Space for the corner
    for char in " " + seq2:  # Add a space at the start for alignment
        print(f"{char:4}", end="")
    print()  # New line after seq2

    for i, row in enumerate(m):
        if i == 0:
            print("  ", end="")  # Two spaces for alignment of first row
        else:
            print(f"{seq1[i-1]:2}", end="")  # Print seq1 character
        for item in row:
            print(f"{item:4}", end="")
        print()  # Move to the next line after each row

    # Backtrace to find optimal alignment
    i, j = len(seq1), len(seq2)
    alignmentA = ""
    alignmentB = ""

    while i > 0 or j > 0:
        # If match or mistmatch, add letter to the alignment A and B and move diagonally up and left
        if m[i][j] == m[i-1][j-1] + (1 if seq1[i-1] == seq2[j-1] else -1):
            alignmentA = seq1[i-1] + alignmentA
            alignmentB = seq2[j-1] + alignmentB
            i -= 1
            j -= 1  
        # If deletion, add letter to the alignment A and a gap to alignment B and move up
        # For deletion, keep the same column but move up a row
        elif m[i][j] == m[i-1][j] - 1:
            alignmentA = seq1[i-1] + alignmentA
            alignmentB = '-' + alignmentB
            i -= 1
        # If insertion, add a gap to alignment A and letter to alignment B and move left
        # For insertion, keep the same row but move left a column
        else:
            alignmentA = '-' + alignmentA
            alignmentB = seq2[j-1] + alignmentB
            j -= 1  
    return alignmentA, alignmentB

# Use written problem from HW2 to check answer
#seq1 = 'TTAGCGAGA'
#seq2 = 'TAGCTAA'

seq1 = "ATGTTATA"

seq2 = "ATCGTCC"

dynamic = NW(seq1, seq2)
print(dynamic)

