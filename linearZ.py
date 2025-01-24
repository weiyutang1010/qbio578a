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
        m, b = i - l, r - i + 1

        if i >= r:
            z[i] = match_prefix(s, i, 0)
            l, r = i, i + z[i]
        else:
            if z[m] < b:
                z[i] = z[m]
            else:
                z[i] = z[m] + match_prefix(s, r, r - i)
                l, r = i, i + z[i]

#        print(f"i: {i}, [l, r): [{l}, {r}), b: {b}, m: {m}, z[m]: {z[m]}")

    for i in range(len(s)):
        print(f"{s[i]} ", end="")
    print()
    for i in range(len(s)):
        print(f"{z[i]} ",end="")
    print()
    return z

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
if __name__ == "__main__":
    s_list = ["aabxaabx", "aabxaabxcaabxaabxay", "bacabcababacacbacabcaabcabac", "abcdabcabcabdcbadbcadbcacadbcabdca", "acbdadbcdbcbdacbabacabacbabcacba"]
    for s in s_list:
        """
        try:
            linearZ_mark(s)
        except:
            print(f"mark code error: {s}")
        print()
        """
    
        try:
            linearZ(s)
        except:
            print(f"my code error: {s}")
        print()
