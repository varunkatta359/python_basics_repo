def next_move(player, positions):
    jakoof_x, jakoof_y, cop1_x, cop1_y, cop2_x, cop2_y, cop3_x, cop3_y = positions
    
    if player == 'C':
        # Cops' turn to move
        # Cops move 1 step north, new positions for cops
        new_cop1_x, new_cop1_y = cop1_x, min(cop1_y + 1, 19)
        new_cop2_x, new_cop2_y = cop2_x, min(cop2_y + 1, 19)
        new_cop3_x, new_cop3_y = min(cop3_x + 1, 19), cop3_y
        
        return new_cop1_x, new_cop1_y, new_cop2_x, new_cop2_y, new_cop3_x, new_cop3_y
    
    elif player == 'R':
        # Dr. Jakoof's turn to move
        # Dr. Jakoof moves 1 step diagonally towards the top left corner
        new_jakoof_x, new_jakoof_y = max(0, jakoof_x - 1), max(0, jakoof_y - 1)
        
        return new_jakoof_x, new_jakoof_y

# Sample input
player = input().strip()
positions = list(map(int, input().strip().split()))

# Get next positions based on the player's character
new_positions = next_move(player, positions)

# Output the new positions
print(*new_positions)
