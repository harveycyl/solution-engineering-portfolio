def two_sum(nums, target):
    """
    Given an array of integers (nums) and an integer (target), this function
    returns the indices of the two numbers in the array that add up to the target.

    This solution uses a hash map (a Python dictionary) to achieve a time
    complexity of O(n), which is highly efficient.

    Args:
        nums (list[int]): A list of integers (e.g., transaction amounts).
        target (int): The target sum to find (e.g., the total charge).

    Returns:
        list[int]: A list containing the indices of the two numbers that sum
                   to the target. Returns an empty list if no solution is found.
    """
    num_map = {}  # Dictionary to store each number and its index

    # Iterate through the list with both index and value
    for index, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # Check if the complement already exists in our map
        if complement in num_map:
            # If it exists, we have found our pair
            return [num_map[complement], index]

        # If the complement is not found, add the current number and its index to the map
        # for future checks.
        num_map[num] = index

    # Return an empty list if no solution is found (though the problem guarantees one)
    return []

# --- Example Usage based on the Expense Report Business Problem ---

# The list of individual transaction amounts from the receipt
transactions = [5, 12, 25, 18, 10]

# The summary charge that needs to be matched
total_to_match = 37

# Call the function to find the two transactions
result_indices = two_sum(transactions, total_to_match)

# Print the results in a clear, business-friendly format
if result_indices:
    print(f"Business Problem: Expense Report Reconciliation")
    print(f"-------------------------------------------------")
    print(f"List of Transactions: {transactions}")
    print(f"Summary Charge to Match: ${total_to_match}")
    print(f"Found a match!")
    print(f"The transactions at line numbers (indices) {result_indices[0]} and {result_indices[1]} add up to the total.")
    print(f"Transaction 1: ${transactions[result_indices[0]]}")
    print(f"Transaction 2: ${transactions[result_indices[1]]}")
else:
    print(f"No two transactions were found that sum to ${total_to_match}.")