def tower_of_hanoi(n, source, auxiliary, destination):
    # Base case: only one disk to move
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    # Step 1: Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    
    # Step 2: Move the nth (largest) disk to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Step 3: Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# --- Main program ---
# Input: Number of disks
num_disks = int(input("Enter the number of disks: "))

# Print the steps to solve the puzzle
print(f"\nSolution for {num_disks} disks:")
tower_of_hanoi(num_disks, 'A', 'B', 'C')
