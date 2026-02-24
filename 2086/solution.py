class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        if hamsters == "H":
            return -1

        if hamsters == ".":
            return 0

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
        buckets = list(hamsters)

        # preprocess
        if hamsters[0] == 'H':
            buckets[1] = 'F'
            food += 1

        if hamsters[-1] == 'H' and buckets[-2] != 'F':
            buckets[-2] = 'F'
            food += 1

        def no_food(idx):
            return (
                buckets[idx - 1] != 'F'
                and buckets[idx + 1] != 'F'
            )
                
            
        for i in range(1, n - 1):
            if hamsters[i] == 'H' and no_food(i):
                if hamsters[i + 1] == 'H':
                    buckets[i - 1] = 'F'
                else:
                    buckets[i + 1] = 'F'
                food += 1

        return food
