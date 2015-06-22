/*

Compare and contrast a hash table and an STL map. How is a hash table
implemented? If the number of inputs is small, which data structure
opinions can be used instead of a hash table?

Hash tables using hash function to map a key to an index. It is O(1). Collisions shall be resolved.

STL map insert key/value pair to binary search tree based on the key. O(log N). No collisions.

*/
