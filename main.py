def dfs_n_queens(n):
    if n < 1:
        return []
    
    solutions = []
    board = [-1] * n  # board[row] = column where queen is placed
    
    def is_safe(row, col):
        # Check all previous rows
        for prev_row in range(row):
            prev_col = board[prev_row]
            # Same column or same diagonal
            if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
                return False
        return True
    
    def dfs(row):
        if row == n:
            # Found a valid arrangement
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                dfs(row + 1)
                # Backtrack: board[row] will be overwritten in next iteration
    
    dfs(0)
    return solutions