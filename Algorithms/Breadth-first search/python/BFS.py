from typing import Dict, List


def bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    visited = {start: True}
    queue = [start]

    while queue:
        current = queue.pop(0)
        for i in graph[current]:
            if i not in visited:
                queue.append(i)
                visited[i] = True

    return list(visited.keys())
