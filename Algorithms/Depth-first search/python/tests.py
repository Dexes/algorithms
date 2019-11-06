from unittest import TestCase

import DFS


class DFSTest(TestCase):
    @property
    def graph(self):
        return {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E'],
        }

    @property
    def cases(self):
        return {
            'A': ['A', 'B', 'D', 'E', 'F', 'C'],
            'B': ['B', 'A', 'C', 'F', 'E', 'D'],
            'C': ['C', 'A', 'B', 'D', 'E', 'F'],
            'D': ['D', 'B', 'A', 'C', 'F', 'E'],
            'E': ['E', 'B', 'A', 'C', 'F', 'D'],
            'F': ['F', 'C', 'A', 'B', 'D', 'E'],
        }

    def test_dfs(self):
        for start, expected in self.cases.items():
            self.assertEqual(DFS.dfs(self.graph, start), expected)
