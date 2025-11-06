class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def next_char(i, s):
            return s[i]

        def next_char_frequency(i, s):
            j = i
            c = s[j]
            while j < len(s) and s[j] == c:
                j += 1
            return j - i

        def get_index_of_next_char(i, s):
            j = next_char_frequency(i, s)
            return i + j
        
        name_index, typed_index = 0, 0

        while name_index < len(name) and typed_index < len(typed):
            next_name_char = next_char(name_index, name)
            next_typed_char = next_char(typed_index, typed)
            next_name_char_frequency = next_char_frequency(name_index, name)
            next_typed_char_frequency = next_char_frequency(typed_index, typed)

            if next_name_char != next_typed_char:
                return False
            if next_name_char_frequency > next_typed_char_frequency:
                return False

            name_index = get_index_of_next_char(name_index, name)
            typed_index = get_index_of_next_char(typed_index, typed)


        return typed_index == len(typed) and name_index == len(name)
