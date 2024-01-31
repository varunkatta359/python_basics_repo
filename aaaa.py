def combine_stones(test_cases):
    results = []
    
    for case in test_cases:
        n, white_spells, black_spells = case
        combined_stones = []
        
        for i in range(n):
            if white_spells[i] != black_spells[i]:
                combined_stones.append(black_spells[i])
                combined_stones.append(white_spells[i])
            else:
                combined_stones.append(black_spells[i])
        
        combined_sequence = ''.join(combined_stones)
        results.append(combined_sequence if len(set(combined_sequence)) != 1 else "Impossible")
    
    return results

# Test cases provided in the input
test_cases = [
    (4, "WWBWW", "WWBWW"),
    (3, "BBB", "BBB")
]

# Get the results
results = combine_stones(test_cases)

# Output the results
for result in results:
    print(result)
