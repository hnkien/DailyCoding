class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # Count of words passing through this node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1  # Increase count for each character in the word path

    def find_unique_prefix(self, word):
        node = self.root
        prefix = ""
        for char in word:
            prefix += char
            node = node.children[char]
            if node.count == 1:  # Unique prefix found
                return prefix
        return prefix

    def print_trie(self):
        # A helper function for recursive printing
        def print_node(node, prefix):
            for char, child in node.children.items():
                print(f"{prefix}{char}")
                print_node(child, prefix + "-")
            # # Indicate end of a word
            # if node.is_end_of_word:
            #     print(f"{prefix}(end)")
        # Start with the root and an empty prefix
        print_node(self.root, "")

def shortest_unique_prefixes(words):
    trie = Trie()
    # Insert all words into the Trie
    for word in words:
        trie.insert(word)

    trie.print_trie()

    # Find shortest unique prefix for each word
    return [trie.find_unique_prefix(word) for word in words]

# Example usage
words = ["dog", "cat", "apple", "apricot", "fish"]
print(shortest_unique_prefixes(words))  # Output: ['d', 'c', 'app', 'apr', 'f']
