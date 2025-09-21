class PalindromeValidator:
    """A class that validates palindromes for data integrity and content moderation."""
    
    def is_palindrome(self, s):
        """
        Core Algorithm: Determine if a string is a palindrome after normalizing.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            s (str): Input string to validate
            
        Returns:
            bool: True if string is a palindrome, False otherwise
        """
        if not s:
            return True
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
    def validate_user_input(self, user_inputs):
        """
        Business Use Case: Data Integrity Validation
        
        Validate user inputs for e-commerce platforms to detect suspicious
        patterns and maintain data quality standards.
        
        Args:
            user_inputs (list[str]): List of user input strings
            
        Returns:
            dict: Validation results with quality metrics
        """
        results = []
        suspicious_count = 0
        
        for user_input in user_inputs:
            is_palindrome = self.is_palindrome(user_input)
            
            # Flag long palindromes as potentially suspicious
            is_suspicious = is_palindrome and len(user_input.replace(' ', '')) > 15
            if is_suspicious:
                suspicious_count += 1
            
            results.append({
                'input': user_input[:50] + '...' if len(user_input) > 50 else user_input,
                'is_palindrome': is_palindrome,
                'length': len(user_input),
                'status': 'SUSPICIOUS' if is_suspicious else 'NORMAL'
            })
        
        return {
            'results': results,
            'total_inputs': len(user_inputs),
            'suspicious_count': suspicious_count,
            'integrity_score': 1 - (suspicious_count / len(user_inputs)) if user_inputs else 1
        }
    
    def analyze_content_authenticity(self, content_list):
        """
        AI Orchestration Use Case: Content Moderation
        
        Analyze content patterns to detect potential bot-generated text
        through palindromic pattern recognition.
        
        Args:
            content_list (list[str]): List of content strings to analyze
            
        Returns:
            dict: Content authenticity analysis
        """
        total_content = len(content_list)
        palindrome_count = 0
        bot_likelihood_scores = []
        
        for content in content_list:
            is_palindrome = self.is_palindrome(content)
            if is_palindrome:
                palindrome_count += 1
            
            # Calculate bot likelihood (higher palindrome ratio = higher bot likelihood)
            alphanumeric_length = sum(1 for c in content if c.isalnum())
            bot_score = 0.8 if is_palindrome and alphanumeric_length > 20 else 0.1
            bot_likelihood_scores.append(bot_score)
        
        palindrome_ratio = palindrome_count / total_content if total_content > 0 else 0
        avg_bot_likelihood = sum(bot_likelihood_scores) / len(bot_likelihood_scores) if bot_likelihood_scores else 0
        
        return {
            'total_analyzed': total_content,
            'palindrome_count': palindrome_count,
            'palindrome_ratio': round(palindrome_ratio, 3),
            'avg_bot_likelihood': round(avg_bot_likelihood, 3),
            'authenticity_rating': 'HIGH' if palindrome_ratio > 0.3 else 'MEDIUM' if palindrome_ratio > 0.1 else 'LOW'
        }

# --- Example Usage ---
def run_tests():
    """Demonstrate palindrome validation with business and AI use cases."""
    
    validator = PalindromeValidator()
    
    print("Valid Palindrome: Data Integrity & Content Moderation")
    print("-" * 50)
    
    # Core Algorithm Test
    print("\n1. Core Palindrome Algorithm:")
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?"
    ]
    
    for text in test_cases:
        result = validator.is_palindrome(text)
        status = "✓ PALINDROME" if result else "✗ NOT PALINDROME"
        print(f"   {status}: '{text}'")
    
    # Business Use Case: Data Integrity
    print("\n2. Business Use Case - E-commerce Input Validation:")
    user_inputs = [
        "Great product quality!",
        "A Santa at NASA - best seller!",
        "Fast shipping, excellent service",
        "Step on no pets review"
    ]
    
    validation_result = validator.validate_user_input(user_inputs)
    print(f"   Total Inputs: {validation_result['total_inputs']}")
    print(f"   Suspicious Patterns: {validation_result['suspicious_count']}")
    print(f"   Data Integrity Score: {validation_result['integrity_score']:.2f}")
    
    for result in validation_result['results']:
        print(f"   {result['status']}: '{result['input']}'")
    
    # AI Use Case: Content Moderation
    print("\n3. AI Use Case - Bot Content Detection:")
    content_samples = [
        "This product is amazing for daily use",
        "A Toyota's a Toyota",
        "Really satisfied with my purchase",
        "Madam, I'm Adam and I love this!"
    ]
    
    analysis = validator.analyze_content_authenticity(content_samples)
    print(f"   Content Analyzed: {analysis['total_analyzed']}")
    print(f"   Palindrome Ratio: {analysis['palindrome_ratio']*100:.1f}%")
    print(f"   Bot Likelihood: {analysis['avg_bot_likelihood']:.2f}")
    print(f"   Authenticity Rating: {analysis['authenticity_rating']} risk")

if __name__ == "__main__":
    run_tests()