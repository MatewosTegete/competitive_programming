class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0
        compressed_index = 0
        current_char = chars[0]
        count = 1

        for i in range(1, len(chars)):
            if chars[i] == current_char:
                count += 1
            else:
                chars[compressed_index] = current_char
                compressed_index += 1
                if count > 1:
                    count_str = str(count)
                    for digit in count_str:
                        chars[compressed_index] = digit
                        compressed_index += 1
                current_char = chars[i]
                count = 1
        chars[compressed_index] = current_char
        compressed_index += 1
        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[compressed_index] = digit
                compressed_index += 1
        return compressed_index
