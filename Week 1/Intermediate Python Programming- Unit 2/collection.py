'''
Given an array of strings (str), group the anagrams together. You can return the
answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.
'''

from collections import defaultdict

def group_anagrams(words):
    """
    Group the anagrams together in the given list of words.

    Args:
        words (List[str]): A list of strings (words).

    Returns:
        List[List[str]]: A list of lists containing grouped anagrams.

    """
    anagram_groups = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)

    return list(anagram_groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

