# these test are copied from https://edabit.com/challenge/QWAqDyd9RXqyrNyo3

from unittest import TestCase
from edabit_challenges.abbreviating_a_sentence import abbreviate


class TestAbbreviatingASentence(TestCase):

    def test_abbreviate(self):
        self.assertEqual(abbreviate("do it yourself", 2), "DIY")
        self.assertEqual(abbreviate("attention AND deficit OR hyperactivity THE disorder"), "ADHD")
        self.assertEqual(abbreviate("the acronym of long word lengths", 5), "AL")
        self.assertEqual(abbreviate("laugh out loud"), "LL")
        self.assertEqual(abbreviate("Keep It Simple Stupid"), "KSS")
        self.assertEqual(abbreviate("laugh out loud", 3), "LOL")
        self.assertEqual(abbreviate("Keep It Simple Stupid", 2), "KISS")
