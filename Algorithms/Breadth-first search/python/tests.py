from unittest import TestCase

import BFS


class BFSTest(TestCase):
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
            'A': ['A', 'B', 'C', 'D', 'E', 'F'],
            'B': ['B', 'A', 'D', 'E', 'C', 'F'],
            'C': ['C', 'A', 'F', 'B', 'E', 'D'],
            'D': ['D', 'B', 'A', 'E', 'C', 'F'],
            'E': ['E', 'B', 'F', 'A', 'D', 'C'],
            'F': ['F', 'C', 'E', 'A', 'B', 'D'],
        }

    def test_bfs(self):
        for start, expected in self.cases.items():
            self.assertEqual(BFS.bfs(self.graph, start), expected)
