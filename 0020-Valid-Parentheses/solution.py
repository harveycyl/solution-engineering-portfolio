class BracketValidator:
    """A class that handles bracket validation for both code quality assurance and AI data validation."""
    
    def __init__(self):
        """Initialize the bracket mapping for validation."""
        self.bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        self.opening_brackets = set(['(', '{', '['])
        self.closing_brackets = set([')', '}', ']'])
    
    def is_valid(self, s):
        """
        Code Quality Use Case: Validate syntax correctness in code files, configuration
        files, and JSON/XML documents to prevent deployment failures and production issues.

        AI Data Validation Use Case: Ensure structured data integrity for AI model inputs,
        template validation for prompt engineering, and schema validation for training datasets.

        This solution uses a stack-based approach to track opening brackets and validate
        proper closing order, ensuring O(n) time complexity for efficient validation.

        Args:
            s (str): String containing brackets to validate (e.g., code snippet, JSON, template)

        Returns:
            bool: True if brackets are properly matched and nested, False otherwise

        Examples:
            "()" -> True (valid function call)
            "()[]{}" -> True (valid mixed brackets)
            "(]" -> False (mismatched brackets)
            "([)]" -> False (incorrect nesting order)
        """
        if not s:
            return True
        
        stack = []
        
        for char in s:
            if char in self.opening_brackets:
                # Push opening bracket onto stack
                stack.append(char)
            elif char in self.closing_brackets:
                # Check if there's a matching opening bracket
                if not stack:
                    return False  # Closing bracket without opening
                
                # Pop and validate the matching pair
                last_opening = stack.pop()
                if last_opening != self.bracket_map[char]:
                    return False  # Mismatched bracket types
        
        # Valid only if all brackets are matched (empty stack)
        return len(stack) == 0
    
    def validate_code_file(self, code_content):
        """
        Validate bracket syntax in code files for CI/CD pipeline integration.
        
        Args:
            code_content (str): Source code content to validate
            
        Returns:
            dict: Validation results with detailed analysis
        """
        # Extract only bracket characters for validation
        brackets_only = ''.join(char for char in code_content if char in '()[]{}\'"')
        
        # Remove string literals to avoid false positives
        filtered_brackets = self._filter_string_literals(brackets_only)
        
        is_valid = self.is_valid(filtered_brackets)
        
        return {
            'is_valid': is_valid,
            'total_brackets': len(filtered_brackets),
            'bracket_sequence': filtered_brackets,
            'error_type': self._get_error_type(filtered_brackets) if not is_valid else None
        }
    
    def validate_json_config(self, json_string):
        """
        Validate JSON configuration files for deployment safety.
        
        Args:
            json_string (str): JSON configuration content
            
        Returns:
            dict: Validation results for configuration management
        """
        brackets_only = ''.join(char for char in json_string if char in '()[]{}\'"')
        filtered_brackets = self._filter_string_literals(brackets_only)
        
        is_valid = self.is_valid(filtered_brackets)
        bracket_count = {
            'curly': filtered_brackets.count('{') + filtered_brackets.count('}'),
            'square': filtered_brackets.count('[') + filtered_brackets.count(']'),
            'round': filtered_brackets.count('(') + filtered_brackets.count(')')
        }
        
        return {
            'is_valid': is_valid,
            'bracket_counts': bracket_count,
            'complexity_score': sum(bracket_count.values()),
            'deployment_safe': is_valid and bracket_count['curly'] > 0
        }
    
    def batch_validate(self, file_contents):
        """
        Perform batch validation for multiple files in CI/CD pipeline.
        
        Args:
            file_contents (list): List of file content strings
            
        Returns:
            dict: Batch validation summary
        """
        results = []
        total_files = len(file_contents)
        valid_files = 0
        
        for i, content in enumerate(file_contents):
            validation_result = self.validate_code_file(content)
            validation_result['file_index'] = i
            results.append(validation_result)
            
            if validation_result['is_valid']:
                valid_files += 1
        
        success_rate = (valid_files / total_files * 100) if total_files > 0 else 0
        
        return {
            'individual_results': results,
            'summary': {
                'total_files': total_files,
                'valid_files': valid_files,
                'invalid_files': total_files - valid_files,
                'success_rate': round(success_rate, 2),
                'deployment_ready': success_rate == 100.0
            }
        }
    
    def _filter_string_literals(self, brackets_string):
        """Helper method to remove brackets inside string literals."""
        # Simplified version - in production, would need more sophisticated parsing
        result = []
        in_string = False
        quote_char = None
        
        for char in brackets_string:
            if char in '\'"' and not in_string:
                in_string = True
                quote_char = char
            elif char == quote_char and in_string:
                in_string = False
                quote_char = None
            elif not in_string and char in '()[]{}':
                result.append(char)
        
        return ''.join(result)
    
    def _get_error_type(self, brackets):
        """Determine the type of bracket validation error."""
        stack = []
        
        for char in brackets:
            if char in self.opening_brackets:
                stack.append(char)
            elif char in self.closing_brackets:
                if not stack:
                    return "unmatched_closing_bracket"
                
                last_opening = stack.pop()
                if last_opening != self.bracket_map[char]:
                    return "mismatched_bracket_type"
        
        if stack:
            return "unmatched_opening_bracket"
        
        return None

# --- Example Usage ---
def run_tests():
    """Run test cases for both code validation and AI data validation scenarios."""
    
    validator = BracketValidator()
    
    print("\nBusiness Problem: Code Quality & AI Data Validation")
    print("-" * 55)
    
    # Test Case 1: Basic bracket validation
    print("\n1. Basic Syntax Validation:")
    test_cases = [
        ("()", "Simple function call"),
        ("()[]{}", "Mixed bracket types"),
        ("(]", "Mismatched brackets"),
        ("([)]", "Incorrect nesting"),
        ("((()))", "Nested parentheses"),
        ("", "Empty string")
    ]
    
    for brackets, description in test_cases:
        result = validator.is_valid(brackets)
        status = "✅ VALID" if result else "❌ INVALID"
        print(f"   {status} {description}: '{brackets}'")
    
    # Test Case 2: Code file validation for CI/CD
    print("\n2. CI/CD Pipeline Code Validation:")
    code_samples = [
        'function validate() { return array[index]; }',
        'if (condition) { process(); )',  # Invalid
        'const obj = { key: "value", nested: [1, 2, 3] };',
        'for (let i = 0; i < array.length; i++) { console.log(array[i]); }'
    ]
    
    for i, code in enumerate(code_samples):
        result = validator.validate_code_file(code)
        status = "✅ PASS" if result['is_valid'] else "❌ FAIL"
        print(f"   {status} Code Sample {i+1}: {result['total_brackets']} brackets")
        if not result['is_valid']:
            print(f"        Error: {result['error_type']}")
    
    # Test Case 3: JSON configuration validation
    print("\n3. Configuration File Validation:")
    json_configs = [
        '{"api": {"version": "v1", "endpoints": ["/users", "/orders"]}}',
        '{"config": {"debug": true, "port": 8080}',  # Invalid - missing closing brace
        '[]',  # Valid but empty
        '{"nested": {"deep": {"structure": {"value": 42}}}}'
    ]
    
    for i, config in enumerate(json_configs):
        result = validator.validate_json_config(config)
        status = "✅ SAFE" if result['deployment_safe'] else "❌ UNSAFE"
        print(f"   {status} Config {i+1}: Complexity {result['complexity_score']}")
        print(f"        Brackets: {result['bracket_counts']}")
    
    # Test Case 4: Batch validation for enterprise deployment
    print("\n4. Enterprise Batch Validation:")
    file_batch = [
        'function a() { return {}; }',
        'const arr = [1, 2, 3];',
        'if (true) { console.log("valid"); }',
        'broken function() { return ; )',  # Invalid
        '{"valid": "json", "config": true}'
    ]
    
    batch_result = validator.batch_validate(file_batch)
    summary = batch_result['summary']
    
    print(f"   📊 Batch Results: {summary['valid_files']}/{summary['total_files']} files valid")
    print(f"   📊 Success Rate: {summary['success_rate']}%")
    print(f"   🚀 Deployment Ready: {summary['deployment_ready']}")
    
    # Test Case 5: Performance analysis for large-scale validation
    print("\n5. Performance Analysis:")
    
    # Generate test data
    large_valid = "(" * 1000 + ")" * 1000
    large_invalid = "(" * 1000 + ")" * 999
    
    import time
    
    # Test large valid string
    start_time = time.time()
    result1 = validator.is_valid(large_valid)
    time1 = time.time() - start_time
    
    # Test large invalid string
    start_time = time.time()
    result2 = validator.is_valid(large_invalid)
    time2 = time.time() - start_time
    
    print(f"   ⚡ Large Valid (2000 chars): {result1} - Time: {time1:.6f}s")
    print(f"   ⚡ Large Invalid (1999 chars): {result2} - Time: {time2:.6f}s")
    print(f"   📈 Processing Rate: ~{2000/max(time1, 0.000001):.0f} chars/second")
    
    print("\n" + "="*55)
    print("BUSINESS IMPACT SUMMARY:")
    print("• Code Quality: Automated syntax validation in CI/CD pipelines")
    print("• Risk Reduction: Prevention of deployment failures due to syntax errors")
    print("• AI Enhancement: Structured data validation for machine learning systems")
    print("• Enterprise Scale: Batch processing for large codebases and configurations")
    print("="*55)

if __name__ == "__main__":
    run_tests()