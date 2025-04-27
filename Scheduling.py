class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

class ProcessScheduler:
    def __init__(self):
        self.processes = []

    def add_process(self, pid, arrival_time, burst_time, priority=0):
        self.processes.append(Process(pid, arrival_time, burst_time, priority))

    def fcfs(self):
        self.processes.sort(key=lambda x: x.arrival_time)
        current_time = 0
        
        for process in self.processes:
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            
            process.completion_time = current_time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            current_time = process.completion_time

    def sjf(self):
        remaining_processes = self.processes.copy()
        current_time = 0
        
        while remaining_processes:
            available_processes = [p for p in remaining_processes if p.arrival_time <= current_time]
            if not available_processes:
                current_time += 1
                continue
                
            process = min(available_processes, key=lambda x: x.burst_time)
            process.completion_time = current_time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            current_time = process.completion_time
            remaining_processes.remove(process)

    def priority_scheduling(self):
        remaining_processes = self.processes.copy()
        current_time = 0
        
        while remaining_processes:
            available_processes = [p for p in remaining_processes if p.arrival_time <= current_time]
            if not available_processes:
                current_time += 1
                continue
                
            process = min(available_processes, key=lambda x: x.priority)
            process.completion_time = current_time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            current_time = process.completion_time
            remaining_processes.remove(process)

    def round_robin(self, quantum):
        remaining_processes = self.processes.copy()
        current_time = 0
        
        while remaining_processes:
            process = remaining_processes.pop(0)
            
            if process.remaining_time <= quantum:
                current_time += process.remaining_time
                process.remaining_time = 0
                process.completion_time = current_time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
            else:
                current_time += quantum
                process.remaining_time -= quantum
                remaining_processes.append(process)

    def display_results(self):
        print("\nProcess ID  Arrival Time  Burst Time  Completion Time  Turnaround Time  Waiting Time")
        print("-" * 80)
        
        for process in self.processes:
            print(f"{process.pid:^10d} {process.arrival_time:^13d} {process.burst_time:^11d}", end="")
            print(f" {process.completion_time:^16d} {process.turnaround_time:^16d}", end="")
            print(f" {process.waiting_time:^12d}")
        
        avg_turnaround = sum(p.turnaround_time for p in self.processes) / len(self.processes)
        avg_waiting = sum(p.waiting_time for p in self.processes) / len(self.processes)
        print(f"\nAverage Turnaround Time: {avg_turnaround:.2f}")
        print(f"Average Waiting Time: {avg_waiting:.2f}")

def main():
    scheduler = ProcessScheduler()
    
    scheduler.add_process(1, 0, 4, 2)
    scheduler.add_process(2, 1, 3, 1)
    scheduler.add_process(3, 2, 2, 3)
    scheduler.add_process(4, 3, 1, 4)

    print("\nFirst Come First Serve (FCFS)")
    scheduler.fcfs()
    scheduler.display_results()

    print("\nShortest Job First (SJF)")
    scheduler.sjf()
    scheduler.display_results()

    print("\nPriority Scheduling")
    scheduler.priority_scheduling()
    scheduler.display_results()

    print("\nRound Robin (Quantum = 2)")
    scheduler.round_robin(2)
    scheduler.display_results()

if __name__ == "__main__":
    main()