from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Where to write the next character
        i = 0      # Read pointer

        while i < len(chars):
            current_char = chars[i]
            count = 0

            # Count how many times current_char repeats consecutively
            while i < len(chars) and chars[i] == current_char:
                i += 1
                count += 1
            
            # Write the character
            chars[write] = current_char
            write += 1

            # If count > 1, write its digits
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        
        return write # New length after compression
    
# Example usage
sol = Solution()

chars1 = ['a','a','b','b','c','c','c']
len1 = sol.compress(chars1)
print("Length:", len1)
print("Compressed:", chars1[:len1])  # ['a', '2', 'b', '2', 'c', '3']

chars2 = ['a']
len2 = sol.compress(chars2)
print("Length:", len2)
print("Compressed:", chars2[:len2])  # ['a']

chars3 = ['a','b','b','b','b','b','b','b','b','b','b','b','b']
len3 = sol.compress(chars3)
print("Length:", len3)
print("Compressed:", chars3[:len3])  # ['a', 'b', '1', '2']