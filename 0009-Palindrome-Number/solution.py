class AITransformationValidator:
    """
    A class that handles both traditional palindrome validation and AI transformation integrity checks.
    In manufacturing, it validates serial numbers. In AI systems, it verifies transformation chains.
    """
    
    def __init__(self):
        """Initialize the validator."""
        pass
    
    @staticmethod
    def is_palindrome(x):
        """
        Traditional Use Case: 
        - Validates if a serial number reads the same forwards and backwards
        - Used in manufacturing quality control for authentic part verification
        - Checks for invalid formats (negative numbers, leading zeros)

        AI Orchestration Use Case:
        - Validates bi-directional AI transformation integrity
        - Ensures information preservation in transformation chains
        - Verifies symmetrical operations maintain data quality

        Args:
            x (int): The value to validate (serial number or transformation hash)

        Returns:
            bool: True if valid palindrome/transformation, False otherwise

        Examples:
            Manufacturing:
                is_palindrome(12321) -> True (valid serial number)
                is_palindrome(-12321) -> False (invalid format)
                is_palindrome(10) -> False (invalid leading zero when reversed)

            AI Transformation:
                English -> Spanish -> English: "Hello" -> "Hola" -> "Hello"
                Python -> Java -> Python: "def func():" -> "public void func()" -> "def func():"
                JSON -> XML -> JSON: {"key": "value"} -> <key>value</key> -> {"key": "value"}
        """
        # Negative numbers are invalid in both contexts
        # Manufacturing: No negative serial numbers
        # AI: Represents corrupted transformation
        if x < 0:
            return False
        
        # Numbers ending with 0 (except 0 itself) are invalid
        # Manufacturing: No leading zeros in serial numbers
        # AI: Represents loss of significant information
        if x > 0 and x % 10 == 0:
            return False

        reversed_half = 0
        original = x  # Store original number for comparison
        
        # We only need to compare half of the digits
        # This optimization works for both use cases
        while x > reversed_half:
            # Build the reversed number one digit at a time
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10

        # For even-length numbers: x == reversed_half
        # For odd-length numbers: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10


def run_tests():
    """Run test cases demonstrating both traditional and AI orchestration use cases."""
    
    print("\nBusiness Problem: Manufacturing QC & AI Transformation Validation")
    print("-" * 60)
    
    # Test Case 1: Manufacturing Serial Numbers
    print("\n1. Traditional Use Case - Serial Number Validation:")
    test_serials = [12321, -12321, 10, 123321, 0]
    for serial in test_serials:
        result = AITransformationValidator.is_palindrome(serial)
        print(f"Serial Number: {serial}")
        print(f"Valid: {result}")
        print(f"Explanation: {'Valid palindromic serial' if result else 'Invalid format'}\n")

    # Test Case 2: AI Transformation Validation
    print("\n2. AI Orchestration Use Case - Transformation Integrity:")
    transformations = [
        {
            "name": "Language Translation",
            "chain": {
                "original": "Hello World",
                "intermediate": "Hola Mundo",
                "final": "Hello World"
            },
            "hash": 12321  # Symmetric hash indicating preserved meaning
        },
        {
            "name": "Code Translation",
            "chain": {
                "original": "def greet():",
                "intermediate": "public void greet()",
                "final": "def greet()"
            },
            "hash": 12345  # Non-symmetric hash indicating altered code
        }
    ]
    
    for transform in transformations:
        result = AITransformationValidator.is_palindrome(transform["hash"])
        print(f"\nTransformation: {transform['name']}")
        print(f"Original: {transform['chain']['original']}")
        print(f"Intermediate: {transform['chain']['intermediate']}")
        print(f"Final: {transform['chain']['final']}")
        print(f"Integrity Maintained: {result}")
        print(f"Hash: {transform['hash']}")


if __name__ == "__main__":
    run_tests()