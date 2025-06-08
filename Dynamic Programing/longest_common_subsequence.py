# Function to find LCS and print it
def findlcs(S1, S2):
    m = len(S1)
    n = len(S2)

    # Step 1: Build the LCS table (bottom-up DP approach)
    L = [[0 for  x in range(n+1)] for x in range(m+1)]


    # Fill the table using the LCS logic
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Step 2: Reconstruct the LCS from the table
    index = L[m][n]
    lcs = [""] * (index + 1)
    lcs[index] = ""  # End of string

    i = m
    j = n
    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            lcs[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Step 3: Print results
    print("S1 : " + S1)
    print("S2 : " + S2)
    print("LCS: " + "".join(lcs))

findlcs("abaaba","babbab")