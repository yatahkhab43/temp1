class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.completion = 0
        self.turnaround = 0
        self.waiting = 0

class Scheduler:
    def __init__(self):
        self.processes = []
    
    def add(self, pid, arrival, burst):
        self.processes.append(Process(pid, arrival, burst))
    
    def fcfs(self):
        self.processes.sort(key=lambda x: x.arrival)
        time = 0
        for p in self.processes:
            if time < p.arrival:
                time = p.arrival
            p.completion = time + p.burst
            p.turnaround = p.completion - p.arrival
            p.waiting = p.turnaround - p.burst
            time = p.completion
    
    def display(self):
        print("\nPID  Arrival  Burst  Completion  Turnaround  Waiting")
        for p in self.processes:
            print(f"{p.pid:3d} {p.arrival:8d} {p.burst:6d} {p.completion:10d}", end="")
            print(f" {p.turnaround:11d} {p.waiting:8d}")
        avg_tat = sum(p.turnaround for p in self.processes) / len(self.processes)
        avg_wt = sum(p.waiting for p in self.processes) / len(self.processes)
        print(f"\nAverage Turnaround: {avg_tat:.2f}")
        print(f"Average Waiting: {avg_wt:.2f}")

if __name__ == "__main__":
    s = Scheduler()
    s.add(1, 0, 4)
    s.add(2, 1, 3)
    s.add(3, 2, 2)
    s.fcfs()
    s.display()