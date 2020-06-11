class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]: 
        ext = [0 for i in range(n)]
        jobs = [(int(s.split(":")[2]), int(s.split(":")[0]), s.split(":")[1][0]) for s in logs] #(time, id, s|e) format
        curr_fun = None
        for t, id_, event in jobs:
            if event == 's':
                if curr_fun != None:
                    ext[curr_fun[0]] += t - curr_fun[1]
                curr_fun = (id_, t) 
            else:#end
                if curr_fun != None:
                    ext[id] += t - curr_fun[1]
                    curr_fun = None
                    last_end = t
                else:
                    ext[id] += t - last_end
                
        return ext

