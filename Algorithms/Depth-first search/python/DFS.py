from typing import Dict, Optional, List


def dfs(graph: Dict[str, List[str]], start: str, visited: Optional[Dict[str, bool]] = None) -> List[str]:
    if visited is None:
        visited = dict()

    visited[start] = True
    for vertex in graph[start]:
        if vertex not in visited:
            dfs(graph, vertex, visited)

    return list(visited.keys())
