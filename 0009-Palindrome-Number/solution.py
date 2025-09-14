def is_palindrome(x):
    """
    Validates if a given number is a palindrome (reads the same forwards and backwards).
    This function is used to verify if a serial number follows the palindromic requirement
    for critical manufacturing components.

    Args:
        x (int): The serial number to validate (e.g., 12321)

    Returns:
        bool: True if the number is a valid palindromic serial number,
              False if it's invalid (negative, leading zeros, or non-palindromic)
    """
    # Negative numbers are not valid serial numbers
    if x < 0:
        return False
    
    # Numbers ending with 0 (except 0 itself) are not valid
    # as they would have leading zeros when reversed
    if x > 0 and x % 10 == 0:
        return False

    reversed_half = 0
    # We only need to compare half of the digits
    while x > reversed_half:
        # Build the reversed number one digit at a time
        reversed_half = reversed_half * 10 + x % 10
        x = x // 10

    # For even-length numbers: x == reversed_half
    # For odd-length numbers: x == reversed_half // 10
    # (we remove the middle digit from reversed_half)
    return x == reversed_half or x == reversed_half // 10


# Test cases
def run_tests():
    """
    Run test cases to verify the palindrome checker functionality.
    """
    test_cases = [
        (12321, True, "Valid palindromic serial number"),
        (-12321, False, "Invalid: negative number"),
        (10, False, "Invalid: has leading zero when reversed"),
        (123321, True, "Valid palindromic serial number (even length)"),
        (0, True, "Valid palindromic serial number (zero)"),
    ]

    for number, expected, description in test_cases:
        result = is_palindrome(number)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {description}")
        print(f"Input: {number}")
        print(f"Expected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    run_tests()
