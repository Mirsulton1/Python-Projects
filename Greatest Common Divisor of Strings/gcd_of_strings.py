def gcd_of_strings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    
    def gcd(a, b):
        # Euclidean algorithm
        while b != 0:
            a, b = b, a % b
        return a
    
    gcd_length = gcd(len(str1), len(str2))
    return str1[:gcd_length]

# Driver
print(gcd_of_strings("ABCABC", "ABC")) # Output: "ABC"
print(gcd_of_strings("ABABAB", "ABAB")) # Output: "AB"
print(gcd_of_strings("LEET", "CODE")) # Output: ""