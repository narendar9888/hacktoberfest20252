def deleteWord(self, word: str) -> None:
    def delete(node, word, depth):
        if depth == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            return len(node.children) == 0
        char = word[depth]
        if char not in node.children:
            return False
        should_delete = delete(node.children[char], word, depth + 1)
        if should_delete:
            del node.children[char]
            return len(node.children) == 0 and not node.is_end_of_word
        return False
    delete(self.root, word, 0)
