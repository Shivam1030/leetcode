class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = {}
        for x, y in pairs: 
            graph.setdefault(x, set()).add(y)
            graph.setdefault(y, set()).add(x)
        
        ans = 1 
        ancestors = set()
        for n in sorted(graph, key=lambda x: len(graph[x]), reverse=True): 
            p = min(ancestors & graph[n], key=lambda x: len(graph[x]), default=None) # immediate ancestor 
            ancestors.add(n)
            if p: 
                if graph[n] - (graph[p] | {p}): return 0 # impossible to have more than ancestor
                if len(graph[n]) == len(graph[p]): ans = 2
            elif len(graph[n]) != len(graph)-1: return 0
        return ans 