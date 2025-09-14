class AIModelPairing:
    """A class that handles both traditional number matching and AI model capability matching."""
    
    @staticmethod
    def two_sum(nums, target):
        """
        Traditional Use Case: Given an array of integers (nums) and an integer (target),
        this function returns the indices of the two numbers in the array that add up to the target.

        AI Orchestration Use Case: Find two AI models whose capabilities sum to a required threshold.
        For example: If we need a total capability score of 0.9, find two models (like GPT-3 with 0.7
        and DALL-E with 0.2) that together meet this requirement.

        This solution uses a hash map (a Python dictionary) to achieve a time
        complexity of O(n), which is highly efficient.

        Args:
            nums (list[int/float]): A list of numbers (e.g., transaction amounts or model capabilities).
            target (int/float): The target sum to find (e.g., total charge or required capability score).

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
            num_map[num] = index

        # Return an empty list if no solution is found
        return []

# --- Example Usage ---
def run_tests():
    """Run test cases for both traditional and AI orchestration scenarios."""
    
    print("\nBusiness Problem: Expense Report Reconciliation & AI Model Orchestration")
    print("-" * 60)
    
    # Test Case 1: Traditional expense matching
    print("\n1. Traditional Use Case - Expense Matching:")
    transactions = [5, 12, 25, 18, 10]
    total_to_match = 37
    result = AIModelPairing.two_sum(transactions, total_to_match)
    if result:
        print(f"Input Transactions: {transactions}")
        print(f"Target Sum: ${total_to_match}")
        print(f"Found match at indices: {result}")
        print(f"Matching transactions: ${transactions[result[0]]} and ${transactions[result[1]]}")
    else:
        print(f"No matching transactions found for sum ${total_to_match}")

    # Test Case 2: AI model capability matching
    print("\n2. AI Orchestration Use Case - Model Capability Matching:")
    models = [
        {"name": "text-analysis", "capability": 0.4},
        {"name": "sentiment", "capability": 0.3},
        {"name": "classification", "capability": 0.7},
        {"name": "summarization", "capability": 0.6}
    ]
    capabilities = [model["capability"] for model in models]
    target_capability = 1.0
    
    result = AIModelPairing.two_sum(capabilities, target_capability)
    if result:
        print(f"Available Models:")
        for i, model in enumerate(models):
            print(f"  - {model['name']}: {model['capability']} capability score")
        print(f"\nTarget Capability Score: {target_capability}")
        print(f"Found Compatible Models:")
        print(f"  1. {models[result[0]]['name']} ({capabilities[result[0]]} capability)")
        print(f"  2. {models[result[1]]['name']} ({capabilities[result[1]]} capability)")
        print(f"Combined Capability: {capabilities[result[0]] + capabilities[result[1]]}")
    else:
        print(f"No compatible model combination found for capability score {target_capability}")

if __name__ == "__main__":
    run_tests()