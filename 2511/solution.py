class Solution:
    def captureForts(self, forts: list[int]) -> int:
        friendly = False
        cnt = 0
        captured = 0
        i = 0
        n = len(forts)

        while i < n:

            while i < n and forts[i] != 1:
                i += 1
            if i == n:
                break

            i += 1

            cnt = 0
            while i < n and forts[i] == 0:
                i += 1
                cnt += 1
            if i == n:
                break
            captured = max(captured, cnt)


        forts = list(reversed(forts))
        i = 0
        while i < n:

            while i < n and forts[i] != 1:
                i += 1
            if i == n:
                break

            i += 1

            cnt = 0
            while i < n and forts[i] == 0:
                i += 1
                cnt += 1
            if i == n:
                break
            captured = max(captured, cnt)

        return captured
