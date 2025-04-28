def is_safe(processes, available, max_need, allocation):
    n = len(processes)  
    m = len(available) 
    
    need = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max_need[i][j] - allocation[i][j]

    finish = [False] * n
    safe_sequence = []
    work = available.copy()

    while len(safe_sequence) < n:
        allocated_in_this_round = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allocation[i][j]
                    safe_sequence.append(processes[i])
                    finish[i] = True
                    allocated_in_this_round = True
                    break
        if not allocated_in_this_round:
            print("System is in a deadlock!")
            print("System is NOT in a safe state!")
            return False, []

    print("System is in a safe state.")
    print(f"Safe sequence is: {safe_sequence}")
    return True, safe_sequence

def main():
    processes = ['P0', 'P1', 'P2', 'P3', 'P4']
    available = [3, 3, 2]

    max_need = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    is_safe(processes, available, max_need, allocation)

if __name__ == "__main__":
    main()
