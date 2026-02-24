class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        if hamsters == "H":
            return -1

        if (
            len(hamsters) >= 2
            and (
                hamsters[:2] == "HH"
                or hamsters[-2:] == "HH"
            )
        ):
            return -1

        for space in hamsters:
            pass

        return -1
