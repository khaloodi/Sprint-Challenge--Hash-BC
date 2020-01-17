Interview Questions
During your challenge, you will be pulled aside by a PM for a 5 minute interview. During this interview, you will be expected to answer the following two topics:

Explain in detail the workings of a dynamic array:

What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
What is the worse case scenario if you try to extend the storage size of a dynamic array?
Explain how blockchain networks remain in consensus:

What does a node do if it gets a message from another in the network with a new block?
Why can't someone cheat by changing a transaction from an earlier block to give themselves coins?

A brute-force solution would involve two nested loops, yielding a quadratic-runtime solution. How can we use a hash table in order to implement a solution with a better runtime?
Think about what we can store in the hash table in order to help us to solve this problem more efficiently.
What if we store each weight in the input list as keys? What would be a useful thing to store as the value for each key?
If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for limit - weight. If it does, then we've found the two items whose weights sum up to the limit!