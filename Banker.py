class BankersAlgorithm:
    def __init__(self, processes, resources):
        self.processes = processes
        self.resources = resources
        self.available = []
        self.max_need = []
        self.allocation = []
        self.need = []
    
    def initialize_values(self, available, max_need, allocation):
        self.available = available
        self.max_need = max_need
        self.allocation = allocation
        self.need = []
        for i in range(self.processes):
            self.need.append([])
            for j in range(self.resources):
                self.need[i].append(self.max_need[i][j] - self.allocation[i][j])
    
    def is_safe_state(self):
        work = self.available.copy()
        finish = [False] * self.processes
        safe_sequence = []
        
        while True:
            found = False
            for p in range(self.processes):
                if not finish[p] and self.is_need_satisfied(p, work):
                    for r in range(self.resources):
                        work[r] += self.allocation[p][r]
                    finish[p] = True
                    safe_sequence.append(p)
                    found = True
            if not found:
                break
        
        return all(finish), safe_sequence
    
    def is_need_satisfied(self, process, work):
        for r in range(self.resources):
            if self.need[process][r] > work[r]:
                return False
        return True
    
    def request_resources(self, process, request):
        for r in range(self.resources):
            if request[r] > self.need[process][r]:
                return False, "Request exceeds maximum claim"
            if request[r] > self.available[r]:
                return False, "Resources unavailable"
        
        for r in range(self.resources):
            self.available[r] -= request[r]
            self.allocation[process][r] += request[r]
            self.need[process][r] -= request[r]
        
        is_safe, sequence = self.is_safe_state()
        
        if is_safe:
            return True, f"Allocation successful. Safe sequence: {sequence}"
        
        for r in range(self.resources):
            self.available[r] += request[r]
            self.allocation[process][r] -= request[r]
            self.need[process][r] += request[r]
        
        return False, "Unsafe state"

if __name__ == "__main__":
    processes = 5
    resources = 3
    
    available = [3, 3, 2]
    max_need = [[7,5,3], [3,2,2], [9,0,2], [2,2,2], [4,3,3]]
    allocation = [[0,1,0], [2,0,0], [3,0,2], [2,1,1], [0,0,2]]
    
    banker = BankersAlgorithm(processes, resources)
    banker.initialize_values(available, max_need, allocation)
    
    is_safe, sequence = banker.is_safe_state()
    print(f"System state: {'safe' if is_safe else 'unsafe'}")
    if is_safe:
        print(f"Safe sequence: {sequence}")
    
    process = 1
    request = [1, 0, 2]
    success, message = banker.request_resources(process, request)
    print(f"\nProcess {process} requesting {request}")
    print(message)