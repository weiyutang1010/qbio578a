#!/usr/bin/env python

def match_prefix(s, p, f):
    i = 0
    while i + max(p, f) < len(s):
        if s[i+f] == s[p+i]:
            i += 1
        else:
            break
    return i

def linearZ(s):
    z = [0] * len(s)

    z[0] = 0
    z[1] = match_prefix(s, 1, 0)
    
    l, r = 1, 1 + z[1]
    for i in range(2, len(s)):
        m, b = i - l, r - l - 1

        if i >= r:
            z[i] = match_prefix(s, i, 0)
            l, r = i, i + z[i]
        else:
            if m + z[m] <= b:
                z[i] = z[m]
            else:
                z[i] = min(z[m], r - i) + match_prefix(s, r, r - i)
                l, r = i, i + z[i]

    return z

def naive_matching(s):
    z = [0] * len(s)
    for i in range(1, len(s)):
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1

    return z

def print_match(s, z1, z2):
    print("Test Case: ", end="")
    for i in range(len(s)):
        print(f"{s[i]} ", end="")
    print()
    
    print("LinearZ:   ", end="")
    for i in range(len(s)):
        print(f"{z1[i]} ",end="")
    print()

    print("Correct:   ", end="")
    for i in range(len(s)):
        print(f"{z2[i]} ",end="")
    print()

    print(f"is correct: {z1 == z2}")

"""
# Mark's pseudocode from the lecture slides but there are indexing mistakes
def match_prefix_mark(s, p, f):
    i = 0
    while i < len(s):
        if s[i+f] == s[p+i]:
            i += 1
        else:
            break
    return i

def linearZ_mark(s):
    z = [0] * len(s)

    z[0] = 0
    z[1] = match_prefix_mark(s, 1, 0)
    
    l, r = 1, z[1]
    for i in range(2, len(s)):
        m, b = i - l + 1, r - i
        if z[m] < b:
            z[i] = z[m]
        else:
            z[i] = z[m] + match_prefix_mark(s, r, r - i)
            l, r = i, z[i]

    for i in range(len(s)):
        print(f"{s[i]} ", end="")
    print()
    for i in range(len(s)):
        print(f"{z[i]} ",end="")
    print()
    return z
"""

if __name__ == "__main__":
    print(
        """
Z-function
Algorithm for calculating the Z-function in linear time.
The Z-function for a string s is an array of length n where the i-th element
is equal to the greatest number of characters starting from the position i that
match with a prefix of s
        """
    )
    
    s_list = ["aabxaabx", "aabxaabxcaabxaabxay", "bacabcababacacbacabcaabcabac", "abcdabcabcabdcbadbcadbcacadbcabdca", "acbdadbcdbcbdacbabacabacbabcacba"]
    for s in s_list:
        """
        try:
            linearZ_mark(s)
        except:
            print(f"mark code error: {s}")
        print()
        """


        z1 = linearZ(s)
        z2 = naive_matching(s)

        print_match(s, z1, z2)
        print()
