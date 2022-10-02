#!/usr/bin/env python3

import unittest


def collatz_steps(n: int) -> int:
    steps = 0
    while n > 1:
        if n & 1 == 0:
            n = n >> 1
        else:
            n = 3 * n + 1
        steps += 1

    return steps


class CollatzStepsTest(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(collatz_steps(1), 0)

    def test_larger(self):
        self.assertEqual(collatz_steps(27), 111)
