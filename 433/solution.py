class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def dfs(gene, mutations):

            nonlocal min_mutations

            if gene == endGene:
                min_mutations = min(min_mutations, mutations)
                return
            
            seen.add(gene)
            for pos in range(len(gene)):
                for letter in 'ACTG':
                    if letter != gene[pos]:
                        new_gene = gene[:pos] + letter + gene[pos + 1:]
                        if new_gene in bank and new_gene not in seen:
                            dfs(new_gene, mutations + 1)
            
            pass

        min_mutations = math.inf
        seen = set()
        dfs(startGene, 0)
        return min_mutations if min_mutations != math.inf else -1
