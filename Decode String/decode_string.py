class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == ']':
                last_str, num = stack.pop()
                curr_str = last_str + curr_str * num
            else:
                curr_str += ch
        
        return curr_str

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        "3[a]2[bc]",       # Expected: "aaabcbc"
        "3[a2[c]]",        # Expected: "accaccacc"
        "2[abc]3[cd]ef",   # Expected: "abcabccdcdcdef"
        "10[a]",           # Expected: "aaaaaaaaaa"
        "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"  # Complex nested case
    ]

    for s in test_cases:
        result = sol.decodeString(s)
        print(f"Input:  {s}\nDecoded: {result}\n")
