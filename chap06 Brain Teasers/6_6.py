"""
There are 100 closed lockers in a hallway. A man begins by opening
all 100 lockers. Next, he closes every second locker. Then on his
third pass, he toggles every third locker (closes it if it is open or
opens if it is closed). This process continues for 100 passes, such
that on each pass i, the man toggles every ith locker. After his 100th
pass in the hallway, in which he toggles only locker #100, how many
lockers are open?

- If the lock is open, it means this number has odd number of
dividends, i.e., n must be a square number. So there will be 1^2, 2^2
... 10^2, in total 10 lockers open in the last.
"""
