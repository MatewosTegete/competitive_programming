class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            xy = str(x) + str(y)
            yx = str(y) + str(x)

            if xy < yx:
                return 1
            elif xy > yx:
                return -1
            else:
                return 0

        nums.sort(key=functools.cmp_to_key(compare))
        largest_num = ''.join(map(str, nums))

        if largest_num[0] == '0':
            return '0'

        return largest_num
