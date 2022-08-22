from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dic=defaultdict(list)
        for i in range(len(rooms)):
            dic[i]=rooms[i]
        path=set()
        def dfs(curr):
            path.add(curr)
            for nd in dic[curr]:
                if nd not in path:
                    dfs(nd)
        dfs(0)
        if len(path)==len(rooms):
            return True
        else:
            return False