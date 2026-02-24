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


        n = len(hamsters)

        for i in range(n - 2):
            if hamsters[i: i + 3] == "HHH":
                return -1

        food = 0

        # preprocess
        if hamsters[0] == 'H':
            hamsters[1] = 'F'
            food += 1

        if hamsters[-1] == 'H':
            hamsters[-21] = 'F'
            food += 1

        def no_food(idx):
            return (
                hamsters[idx - 1] != 'F'
                and hamsters[idx + 1] != 'F'
            )
                
            
        for i in range(1, n - 1):
            if space == 'H' and no_food(i):
                hamsters[idx + 1] = 'F'
                food += 1

        return food
