from collections import defaultdict

class Solution:
    def checkWays(self, P):
        adj = defaultdict(set)
        for u, v in P:
            adj[u].add(v)
            adj[v].add(u)

        def explore_component(node, component, visited):
            component.add(node)
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    explore_component(neighbor, component, visited)

        def analyze(nodes):
            degree_groups = defaultdict(list)
            max_degree = len(nodes) - 1
            for node in nodes:
                degree_groups[len(adj[node])].append(node)

            if len(degree_groups[max_degree]) == 0:
                return 0
            root = degree_groups[max_degree][0]

            for neighbor in adj[root]:
                adj[neighbor].remove(root)

            connected_components = defaultdict(set)
            visited_nodes = set()
            group_counter = 0
            for node in nodes:
                if node != root and node not in visited_nodes:
                    explore_component(node, connected_components[group_counter], visited_nodes)
                    group_counter += 1

            results = [analyze(connected_components[i]) for i in connected_components]
            if 0 in results:
                return 0
            if 2 in results:
                return 2
            if len(degree_groups[max_degree]) > 1:
                return 2
            return 1

        return analyze(set(adj.keys()))