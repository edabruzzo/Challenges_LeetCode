import time

def contarTempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        func(*args, **kwargs)
        fim = time.time()
        print('Tempo de execução: %f' %(fim - inicio))
    return wrapper


@contarTempo
def findNumOfValidWordsSlower(words, puzzles) -> [int]:
    '''

    https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/discuss/1567623/Python3-Solution

    :param words:
    :param puzzles:
    :return:
    '''

    n = len(words)
    m = len(puzzles)

    from collections import defaultdict
    freq = defaultdict(int)  # Hash the words in this dictionary

    for w in words:
        freq[tuple(sorted(list(set(w))))] += 1

    ans = [0] * m

    for i, w in enumerate(puzzles):
        puzzleSet = list(w)
        # Try all subsets of puzzles[i] because 2nd condition in question is word should be subset of puzzle
        for x in range(1 << (len(puzzleSet) - 1)):  # Using the fact that length of puzzles[i] is 7 --> 64  terations (2^6)
            puzzleSubSet = [w[0]]  # First letter should be included in the subset of puzzles[i]
            for c in puzzleSet[1:]:  # --> 6 iterations
                if x & 1:  # Select the characters whose bit is set to 1
                    puzzleSubSet.append(c)
                x = x >> 1  # Divide x by 2
            ans[i] += freq[tuple(sorted(puzzleSubSet))]  # Add answer of that subset for puzzles[i]

    print(ans)



@contarTempo
def findNumOfValidWords(words, puzzles) -> [int]:


    '''
    
    Constraints:

    1 <= words.length <= 105
    4 <= words[i].length <= 50
    1 <= puzzles.length <= 104
    puzzles[i].length == 7
    words[i] and puzzles[i] consist of lowercase English letters.
    Each puzzles[i] does not contain repeated characters.

    '''
    english_alphabet = """a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"""

    for word in puzzles:
        if len(word) != 7:
            puzzles.pop(word)
        for char in word:
            count = word.count(char)
            if char not in english_alphabet or count > 1:
                puzzles.pop(word)

    for word in words:
        if len(word) < 4 and len(word) > 50:
            words.pop(word)
        if len(words) < 1 or len(words) > 10 ** 5:
            words.pop(word)
        for char in word:
            if char not in english_alphabet:
                words.pop(word)

    meet_criteria = []
    if len(puzzles) >= 1 and len(puzzles) <= 10**4:
        for word_puzzle in puzzles:
            contagem = 0
            for word in words:
                if word_puzzle[0] not in word:
                    continue
                for char in word:
                    if char not in word_puzzle:
                        break
                else:
                    contagem = contagem + 1
                    continue

            meet_criteria.append(contagem)

        print(meet_criteria)



class Trie:
    '''
    https://www.geeksforgeeks.org/trie-insert-and-search/
    https://www.baeldung.com/trie-java


    '''

    def __init__(self):
        from collections import defaultdict
        self.chars, self.termino = defaultdict(Trie), 0

    def busca_trie_insert_search(self, palavra):
        cur = self
        for character in palavra:
            cur = cur.chars[character]
        cur.termino += 1

    def busca_profundidade_recursiva(self, palavra_puzzle, cur, hasFirst):
        ans = cur.endsHere if hasFirst else 0
        for character in palavra_puzzle:
            ans += self.busca_trie_insert_search(palavra_puzzle, cur.chars[character], hasFirst or character == palavra_puzzle[0]) if character in cur.chars else 0
        return ans


@contarTempo
def findNumOfValidWordsBuscaProfundidade(words: [str], puzzles: [str]) -> [int]:
    raiz = Trie()
    for word in words:
        raiz.mapear_para_dicionario(set(word))
    print([raiz.busca_profundidade_recursiva(puzzle, raiz, False) for puzzle in puzzles])


# Python program for insert and search
# operation in a Trie

class TrieNode():

    english_alphabet = """a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z""".split(',')

    # Trie node class
    def __init__(self):
        self.children = [None] * len(self.english_alphabet)
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False



class Trie__:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        index = ord(ch) - ord('a')
        return index

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl.isEndOfWord


@contarTempo
def findNumOfValidWordsTrieNode(words, puzzles):
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie__()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    words = ["aaaa","asas",]
    words_1 = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]


    findNumOfValidWordsTrieNode(words, puzzles)
    findNumOfValidWordsBuscaProfundidade(words_1,puzzles)
    findNumOfValidWordsSlower(words, puzzles)
    findNumOfValidWords(words, puzzles)