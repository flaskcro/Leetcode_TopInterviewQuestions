class Solution:
    def myAtoi(self, s: str) -> int:
        int_list = []

        for c in s:
            if len(int_list) == 0:
                if c.isdigit() or c in ["+", "-", " "]:
                    if c != ' ':
                        int_list.append(c)
                else:
                    break
            else:
                if c.isdigit():
                    int_list.append(c)
                else:
                    break

        if "+" in int_list:
            int_list.remove('+')

        if len(int_list) == 0:
            return 0

        if len(int_list) == 1 and int_list[0] in ["+", "-"]:
            return 0

        answer = int("".join(int_list))
        answer = max(min(answer, 2 ** 31 - 1), -2 ** 31)
        return answer


if __name__ == "__main__":
    strs = [" -42","42","+42","3.14519","number is 34878","0000-1234","+2147483648","-2147483649"]
    answer = [-42, 42, 42, 3, 0, 0, 2**31-1, -2**31]

    solution = Solution()
    for s, a in zip(strs, answer):
        assert solution.myAtoi(s) == a
