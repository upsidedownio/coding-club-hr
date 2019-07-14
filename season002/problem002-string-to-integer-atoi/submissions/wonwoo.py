class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        filtered = ''

        for c in str:
            if c is '-' or c is '+':
                if filtered is '':
                    filtered += c
                else:
                    break
            elif c is ' ':
                if filtered is '':
                    continue
                else:
                    break
            elif '0' <= c <= '9':
                filtered += c
            else:
                break
        try:
            parsed = int(filtered)
            if parsed > INT_MAX:
                return INT_MAX
            elif parsed < INT_MIN:
                return INT_MIN
            else:
                return parsed
        except:
            return 0
