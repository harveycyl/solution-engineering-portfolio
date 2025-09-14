# Business Problem: Expense Report Reconciliation

## 1. Scenario
An accounting department is verifying an employee's expense report. The system has flagged a summary charge of **$37**, but the detailed receipt list shows multiple smaller transactions. The accountant needs to find the **two specific transactions** from the list that add up to the flagged **$37** total to approve the report.

## 2. Technical Solution
This problem can be solved by finding two numbers in an array that sum up to a specific target. The provided `solution.py` uses a hash map (dictionary) for an efficient, one-pass solution with a time complexity of O(n).

*   **Input (`nums`):** `[5, 12, 25, 18, 10]`
*   **Target (`target`):** `37`
*   **Output (Indices):** `[1, 2]` (representing the positions of $12 and $25)

This approach ensures the check is performed instantly, even with thousands of transactions.