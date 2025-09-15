class RomanToIntegerConverter:
    """A class that handles Roman numeral conversion for both legacy system integration and modern data parsing."""
    
    def __init__(self):
        """Initialize the Roman numeral to integer mapping."""
        self.roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    def roman_to_int(self, s):
        """
        Legacy Integration Use Case: Convert Roman numerals from legacy mainframe systems
        to modern integer format for database migration and digital transformation.

        Modern AI Use Case: Parse diverse numerical formats from historical documents,
        legal texts, and manuscripts for AI training data preparation and OCR post-processing.

        This solution processes Roman numerals from left to right, handling both
        standard notation and subtraction cases (IV, IX, XL, XC, CD, CM).

        Args:
            s (str): A valid Roman numeral string (e.g., "MCMXCIV", "LVIII", "III")

        Returns:
            int: The corresponding integer value

        Examples:
            "III" -> 3 (legacy transaction sequence)
            "LVIII" -> 58 (historical record number)
            "MCMXCIV" -> 1994 (mainframe transaction ID)
        """
        if not s:
            return 0
        
        total = 0
        prev_value = 0
        
        # Process from right to left for easier subtraction logic
        for char in reversed(s):
            current_value = self.roman_values[char]
            
            # If current value is less than previous, we subtract (IV, IX, etc.)
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            prev_value = current_value
        
        return total
    
    def validate_roman_numeral(self, s):
        """
        Validate if the input string is a properly formatted Roman numeral.
        
        Args:
            s (str): String to validate
            
        Returns:
            bool: True if valid Roman numeral, False otherwise
        """
        if not s:
            return False
        
        # Check if all characters are valid Roman numerals
        valid_chars = set(self.roman_values.keys())
        return all(char in valid_chars for char in s.upper())
    
    def process_batch(self, roman_list):
        """
        Process a batch of Roman numerals for bulk migration scenarios.
        
        Args:
            roman_list (list): List of Roman numeral strings
            
        Returns:
            list: List of dictionaries with original and converted values
        """
        results = []
        for roman in roman_list:
            try:
                if self.validate_roman_numeral(roman):
                    integer_value = self.roman_to_int(roman)
                    results.append({
                        'original': roman,
                        'converted': integer_value,
                        'status': 'success'
                    })
                else:
                    results.append({
                        'original': roman,
                        'converted': None,
                        'status': 'invalid_format'
                    })
            except Exception as e:
                results.append({
                    'original': roman,
                    'converted': None,
                    'status': f'error: {str(e)}'
                })
        
        return results

# --- Example Usage ---
def run_tests():
    """Run test cases for both legacy integration and modern AI parsing scenarios."""
    
    converter = RomanToIntegerConverter()
    
    print("\nBusiness Problem: Legacy System Migration & AI Data Parsing")
    print("-" * 65)
    
    # Test Case 1: Legacy system transaction IDs
    print("\n1. Legacy Mainframe Transaction Migration:")
    legacy_transactions = ["III", "LVIII", "MCMXCIV"]
    for roman in legacy_transactions:
        result = converter.roman_to_int(roman)
        print(f"   Transaction {roman} -> Modern ID: {result}")
    
    # Test Case 2: Historical document processing
    print("\n2. Historical Document AI Processing:")
    document_numerals = ["IV", "IX", "XL", "XC", "CD", "CM"]
    for roman in document_numerals:
        result = converter.roman_to_int(roman)
        print(f"   Document reference {roman} -> Standardized: {result}")
    
    # Test Case 3: Batch processing for data migration
    print("\n3. Batch Migration Processing:")
    batch_data = ["XII", "XXVII", "INVALID", "CDXLIV"]
    results = converter.process_batch(batch_data)
    for result in results:
        status = result['status']
        if status == 'success':
            print(f"   ✅ {result['original']} -> {result['converted']}")
        else:
            print(f"   ❌ {result['original']} -> {status}")
    
    # Test Case 4: Edge cases for robust system integration
    print("\n4. Edge Case Validation:")
    edge_cases = [
        ("I", 1, "Minimum value"),
        ("MMMCMXCIX", 3999, "Maximum value"),
        ("MMCDXLIV", 2444, "Complex subtraction"),
        ("", 0, "Empty input")
    ]
    
    for roman, expected, description in edge_cases:
        try:
            result = converter.roman_to_int(roman)
            status = "✅ PASS" if result == expected else "❌ FAIL"
            print(f"   {status} {description}: '{roman}' -> {result}")
        except Exception as e:
            print(f"   ❌ ERROR {description}: {str(e)}")
    
    # Test Case 5: AI Training Data Statistics
    print("\n5. Data Processing Statistics:")
    all_test_data = ["III", "LVIII", "MCMXCIV", "IV", "IX", "XL", "XC", "CD", "CM"]
    successful_conversions = 0
    total_converted_value = 0
    
    for roman in all_test_data:
        try:
            value = converter.roman_to_int(roman)
            successful_conversions += 1
            total_converted_value += value
        except:
            pass
    
    print(f"   📊 Successfully processed: {successful_conversions}/{len(all_test_data)} records")
    print(f"   📊 Total converted value: {total_converted_value}")
    print(f"   📊 Average value: {total_converted_value/successful_conversions:.2f}")
    
    print("\n" + "="*65)
    print("BUSINESS IMPACT SUMMARY:")
    print("• Legacy System Integration: Automated conversion of historical data")
    print("• AI Data Pipeline: Standardized numerical format for ML processing")
    print("• Quality Assurance: Robust validation and error handling")
    print("• Scalability: Batch processing capability for large datasets")
    print("="*65)

if __name__ == "__main__":
    run_tests()