class Solution:
    def isValid(self, s: str) -> bool:
        # bang anh xa
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = [] # stack luu ky tu

        # duyet chuoi
        for char in s:
            # neu gap ky tu dong
            if char in mapping:
                # lay phan tu tren cung neu stack khong rong
                topElm = stack.pop() if stack else ""

                # neu 2 ky tu khong giong nhau thi return false
                if mapping[char] != topElm:
                    return False

            # gap ky tu mo thi them vao stack
            else:
                stack.append(char)

        # stack rong -> hop le
        return not stack