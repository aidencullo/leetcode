class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        unique_letters = set(letters)
        import string

        alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
        target_index = alphabet.index(target)

        for i in range(target_index + 1, len(alphabet)):
            if alphabet[i] in unique_letters:
                return alphabet[i]
        return letters[0]
        
        

