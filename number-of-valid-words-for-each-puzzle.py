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










if __name__ == '__main__':
    words = ["aaaa","asas","able","ability","actt","actor","access"]
    puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
    inicio = time.time()

    findNumOfValidWordsSlower(words, puzzles)
    findNumOfValidWords(words, puzzles)