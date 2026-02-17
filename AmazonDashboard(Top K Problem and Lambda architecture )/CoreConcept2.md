Top K Heavy Hitters Using a Heap

Core Idea:

You want to find the K most frequent items (heavy hitters) from a large dataset.

Instead of sorting all items (O(n log n)), you can use a min-heap of size K to track the top K efficiently.

How It Works

Count Frequencies

Use a hash map to count how many times each item appears.

Maintain Min-Heap of Size K

For each item in the frequency map:

Add it to the heap

If the heap size exceeds K, remove the smallest frequency item

After processing all items, the heap contains only the top K frequent items

Extract Results

Pop items from the heap to get the K heavy hitters

Optionally sort them by frequency

Why Use a Heap?

Keeps top K items dynamically without sorting the entire dataset.

Time complexity: O(n log K) (much faster than O(n log n) when K << n).

Space complexity: O(K)