from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        radiant_queue=deque()
        dire_queue=deque()
        for i,party in enumerate(senate):
            if party.capitalize()=='R':
                radiant_queue.append(i)
            else:
                radiant_queue.append(i)
        while radiant_queue and dire_queue:
            u=radiant_queue.popleft()
            v=dire_queue.popleft()
            if u<v:
                radiant_queue.append(u+n)
            else:
                dire_queue.append(v+n)
        return "Radiant" if radiant_queue else "Dire"
