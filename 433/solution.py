class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        levels = 0
        q = deque([startGene])
        seen = set()

        while q:

            seen.add(gene)

            if gene == endGene:
                return levels

            levels += 1

            new_q = deque()
            qlen = len(q)
            for _ in range(qlen):
                for pos in range(len(gene)):
                    for letter in 'ACTG':
                        if letter != gene[pos]:
                            new_gene = gene[:pos] + letter + gene[pos + 1:]
                            if new_gene in bank and new_gene not in seen:
                                new_q.append(new_gene)

        return -1
