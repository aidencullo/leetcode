# Source - https://stackoverflow.com/a/59114478
# Posted by user4815162342, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-08, License - CC BY-SA 4.0

import time

for size in 1_000_000, 10_000_000, 100_000_000, 1_000_000_000:
    l = [None] * size
    t0 = time.time()
    l.clear()
    t1 = time.time()
    print(size, t1 - t0)
