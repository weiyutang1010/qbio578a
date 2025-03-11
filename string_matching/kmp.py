#!/usr/bin/env python
import time
import random

def kmp(s):
    pi = [0] * len(s)

    for i in range(1, len(s)):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    return pi

def kmp_matching(s, p):
    """
    s - a string of text of length n
    p - the pattern of length m
    """
    n, m = len(s), len(p)
    pi = kmp(p)

    k = 0
    match = []
    for i in range(n):
        while k > 0 and p[k] != s[i]:
            k = pi[k-1]
        if p[k] == s[i]:
            k += 1
        if k == m:
            match.append(i-m+1)
            k = pi[k-1] # look for the next match

    return match

def naive_method(s):
    n = len(s)
    pi = [0] * n

    for i in range(n):
        for k in range(i+1):
            if s[0:k] == s[i-k+1: i+1]:
                pi[i] = k
    return pi

def generate_string(n):
    characters = ['a', 'b', 'c', 'd']
    return ''.join(random.choice(characters) for _ in range(n))

def test_func(func, s):
    start = time.time()
    out = func(s)
    end = time.time()
    return out, end - start

if __name__ == '__main__':
    random.seed(42)
    test_cases = ['abcabcd', 'ababab', 'abaaba', 'baccbabaccba']
    
    print("Prefix Function")
    for case in test_cases:
        print(f'input: {case}')
        pi_1 = kmp(case)
        pi_ans = naive_method(case)
        print("kmp: ", pi_1)
        print("ans: ", pi_ans)
        print(f"same: {pi_ans == pi_1}")
        print()

    print("--------------------\n")

    matching_test_cases = [("aabacababb", "ab"), ('abcdabcde', 'abc'), ("cadbcabbdabcd", "ab")]
    print("KMP Matching")
    for text, pattern in matching_test_cases:
        print(f'text: {text}, pattern: {pattern}')
        sol = kmp_matching(text, pattern)
        print("kmp: ", sol)
        print()


    print("--------------------\n")

    n, t = 100, 100
    pass_test = 0

    total_time = 0
    naive_time = 0

    for i in range(t):
        s = generate_string(n)

        pi, time1 = test_func(kmp, s)
        ans, time2 = test_func(naive_method, s)
        
        total_time += time1
        naive_time += time2

        if pi == ans:
            pass_test += 1
        else:
            print("s: ", s)
            print("kmp: ", pi)
            print("ans: ", ans)
            print()

    print(f"Passed Tests: {pass_test}/{t}, n={n}")
    print(f"Naive Time: {naive_time:.3f}s")
    print(f"KMP Time: {total_time:.3f}s")
