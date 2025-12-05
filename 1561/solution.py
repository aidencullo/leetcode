'''

constraint:
- nonunique

ex
1, 2, 3, 1, 2, 3, 10, 11, 100 => sort => 1, 1, 2, 2, 3, 3, 10, 11, 100


let's boil this down to a smaller example, given these 6 numbers

7, 8, 9, 10, 11, 12

how do I maximize my coins..

select 10, 11, 12 -> I take 11
then
select 7, 8, 9 -> I take 8

total = 19

alternatively..

    select 8, 11, 12 -> I take 11
    then
    select 7, 9, 10 -> I take 9

    total = 20

so the second approach is more optimal, why?

'''


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        pass
