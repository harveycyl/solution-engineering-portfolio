# Business Problem: Product Serial Number Validation

## 1. Scenario
A manufacturing company produces high-precision equipment with serial numbers that serve as unique identifiers. For quality control purposes, they've implemented a special validation system where certain critical components must have palindromic serial numbers (numbers that read the same forwards and backwards, like 12321). This helps quickly identify authentic parts from counterfeits, as legitimate critical components must pass this palindrome check.

The quality control team needs an efficient way to verify if a given serial number is palindromic. They need to handle various serial number formats, including:
- Standard positive serial numbers (e.g., 12321)
- Invalid formats with negative signs (e.g., -12321)
- Numbers with leading zeros which should be considered invalid (e.g., 0440)

## 2. Technical Solution
This problem can be solved by checking if a number reads the same forwards and backwards. The provided `solution.py` implements this check without converting the number to a string, using pure mathematical operations for better performance. This approach has a time complexity of O(log n), where n is the input number.

### Examples:
1. **Valid Serial Number:**
   * Input: `12321`
   * Output: `true`
   * Explanation: The serial number reads the same from left to right and right to left.

2. **Invalid Serial Number (Negative):**
   * Input: `-12321`
   * Output: `false`
   * Explanation: Negative numbers are invalid in the serial number system.

3. **Invalid Serial Number (Leading Zero):**
   * Input: `10`
   * Output: `false`
   * Explanation: When read from right to left, it becomes '01', making it invalid.

This system helps the quality control team quickly validate authentic components and identify potential counterfeits.
