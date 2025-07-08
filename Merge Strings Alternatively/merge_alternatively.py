def merge_alternatively(word1, word2):
    merged = []
    i, j = 0, 0
    len1, len2 = len(word1), len(word2)

    while i < len1 or j < len2:
        if i < len1:
            merged.append(word1[i])
            i += 1
        if j < len2:
            merged.append(word2[j])
            j += 1
    return ''.join(merged)


# example usage
print(merge_alternatively("abc", "pqr")) # Output: apbqcr
print(merge_alternatively("ab", "pqrs")) # Output: apbqrs
print(merge_alternatively("abcd", "pq")) # Output: apbqcd