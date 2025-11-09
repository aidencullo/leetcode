from functools import reduce
from itertools import batched, chain
batches = batched(range(10), 2)
reduced = reduce(chain, batches)
batches = batched(range(10), 2)
chained = chain.from_iterable(batches)
assert list(reduced) == list(chained)
