What Is a Trie?

A Trie (also called a prefix tree) is a tree-like data structure used to store and retrieve strings efficiently — especially when you care about prefix search.

It is heavily used in:

Autocomplete systems

Spell checkers

Dictionaries

Routing tables

IDE symbol lookup

Core Idea

Instead of storing full words as separate entries, a trie stores characters as nodes along shared paths.

Words that share prefixes share the same path in the tree.

Example words:

car
card
care
cat


Trie structure (conceptual):

        (root)
         |
         c
         |
         a
       /   \
      r     t
    /   \
   d     e


car, card, care share c → a → r

cat shares c → a

Why Trie Is Powerful
1️⃣ Prefix Search is Fast

To find all words starting with "car":

Traverse c → a → r

Return all descendants

Time complexity:

O(L)


Where L = length of prefix

Not dependent on total number of words.

That’s the key advantage over scanning a list.

2️⃣ Efficient for Autocomplete

Each node can store:

A flag: is this a complete word?

Frequency (weight)

Top K suggestions below this prefix

So when user types "ca":

Traverse to node "ca"

Instantly return top suggestions stored at that node