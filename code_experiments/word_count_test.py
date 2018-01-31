"""Module to test readability and efficiency of differnent ways of performing a list word count.
    
   Uses @times and @ntimes decorators to time the total time of running each function 50 times.

   Counter was consistantly the most performant of the three.
   Example run: standard = 0.0159, default_dict = 0.0154, counter = 0.00903

   Using Counter is also the most concise although not the most explicit in showing what's happening.
   It does, however, have the benefit of most_common(n) method for easily selecting the n most common words.

   Conclusion: I will use collections.Counter to perform iterable counts.
"""
import collections
import loremipsum
from helper_code.functions.decorators import timer, ntimes



_, _, TEST_PARAGRAPH = loremipsum.generate_paragraph()
TEST_LIST = TEST_PARAGRAPH.split()


@timer
@ntimes(50)
def standard():
    """Test standard way of using dictionary as word count."""
    words = {}
    for word in TEST_LIST:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words


@timer
@ntimes(50)
def default_dict():
    """Test using default_dict with int callable."""
    words = collections.defaultdict(int)
    for word in TEST_LIST:
        words[word] += 1
    return words


@timer
@ntimes(50)
def counter():
    """Test using collections Counter class"""
    return collections.Counter(TEST_LIST)


standard()
default_dict()
counter()
