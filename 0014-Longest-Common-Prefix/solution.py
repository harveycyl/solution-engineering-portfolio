class CommonPrefixAnalyzer:
    """A class that handles common prefix analysis for both API optimization and AI model alignment."""
    
    def longest_common_prefix(self, strs):
        """
        API Optimization Use Case: Find common prefixes in API endpoints to optimize
        routing rules, reduce gateway configuration complexity, and improve performance.

        AI Model Alignment Use Case: Identify shared patterns in multiple AI model responses
        to validate consensus, align outputs, and optimize multi-model reasoning chains.

        This solution uses vertical scanning to compare characters across all strings
        simultaneously, providing optimal performance for prefix detection.

        Args:
            strs (list[str]): Array of strings (e.g., API endpoints or AI responses)

        Returns:
            str: The longest common prefix string, or empty string if none exists

        Examples:
            ["flower","flow","flight"] -> "fl" (API path optimization)
            ["dog","racecar","car"] -> "" (no common pattern)
            ["/api/v1/users/profile", "/api/v1/users/settings"] -> "/api/v1/users/"
        """
        if not strs or len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        # Find the minimum length to avoid index out of bounds
        min_length = min(len(s) for s in strs)
        
        # Compare characters vertically across all strings
        for i in range(min_length):
            current_char = strs[0][i]
            
            # Check if this character is common across all strings
            for j in range(1, len(strs)):
                if strs[j][i] != current_char:
                    return strs[0][:i]
        
        # If we've checked all characters in the shortest string
        return strs[0][:min_length]
    
    def longest_common_prefix_binary_search(self, strs):
        """
        Optimized version using binary search for large datasets.
        Useful for enterprise-scale API endpoint analysis.
        """
        if not strs:
            return ""
        
        min_length = min(len(s) for s in strs)
        low, high = 0, min_length
        
        while low < high:
            mid = (low + high + 1) // 2
            if self._is_common_prefix(strs, mid):
                low = mid
            else:
                high = mid - 1
        
        return strs[0][:low]
    
    def _is_common_prefix(self, strs, length):
        """Helper method to check if prefix of given length is common to all strings."""
        prefix = strs[0][:length]
        return all(s.startswith(prefix) for s in strs)
    
    def analyze_api_endpoints(self, endpoints):
        """
        Analyze API endpoints to find optimization opportunities.
        
        Args:
            endpoints (list[str]): List of API endpoint paths
            
        Returns:
            dict: Analysis results with optimization recommendations
        """
        if not endpoints:
            return {"common_prefix": "", "optimization_potential": "low", "recommendations": []}
        
        common_prefix = self.longest_common_prefix(endpoints)
        
        # Calculate optimization metrics
        total_chars = sum(len(endpoint) for endpoint in endpoints)
        saved_chars = len(common_prefix) * len(endpoints) if common_prefix else 0
        optimization_percentage = (saved_chars / total_chars * 100) if total_chars > 0 else 0
        
        # Generate recommendations
        recommendations = []
        if len(common_prefix) > 10:
            recommendations.append("High optimization potential: Configure base routing rule")
        if len(common_prefix) > 5:
            recommendations.append("Consider API gateway prefix-based load balancing")
        if not common_prefix:
            recommendations.append("Endpoints are diverse - consider service grouping")
        
        optimization_level = "high" if optimization_percentage > 20 else "medium" if optimization_percentage > 10 else "low"
        
        return {
            "common_prefix": common_prefix,
            "optimization_potential": optimization_level,
            "savings_percentage": round(optimization_percentage, 2),
            "affected_endpoints": len(endpoints),
            "recommendations": recommendations
        }
    
    def analyze_ai_responses(self, responses):
        """
        Analyze AI model responses to identify consensus patterns.
        
        Args:
            responses (list[str]): List of AI model responses
            
        Returns:
            dict: Analysis of response alignment and consensus
        """
        if not responses:
            return {"consensus_prefix": "", "alignment_score": 0, "consensus_strength": "none"}
        
        consensus_prefix = self.longest_common_prefix(responses)
        
        # Calculate alignment metrics
        avg_response_length = sum(len(response) for response in responses) / len(responses)
        alignment_score = (len(consensus_prefix) / avg_response_length * 100) if avg_response_length > 0 else 0
        
        # Determine consensus strength
        if alignment_score > 30:
            consensus_strength = "strong"
        elif alignment_score > 15:
            consensus_strength = "moderate"
        elif alignment_score > 5:
            consensus_strength = "weak"
        else:
            consensus_strength = "none"
        
        return {
            "consensus_prefix": consensus_prefix,
            "alignment_score": round(alignment_score, 2),
            "consensus_strength": consensus_strength,
            "model_count": len(responses),
            "prefix_length": len(consensus_prefix)
        }

# --- Example Usage ---
def run_tests():
    """Run test cases for both API optimization and AI model alignment scenarios."""
    
    analyzer = CommonPrefixAnalyzer()
    
    print("\nBusiness Problem: API Optimization & AI Model Alignment")
    print("-" * 60)
    
    # Test Case 1: API Endpoint Optimization
    print("\n1. API Gateway Routing Optimization:")
    api_endpoints = [
        "/api/v1/users/profile",
        "/api/v1/users/settings",
        "/api/v1/users/preferences",
        "/api/v1/users/notifications"
    ]
    
    prefix = analyzer.longest_common_prefix(api_endpoints)
    api_analysis = analyzer.analyze_api_endpoints(api_endpoints)
    
    print(f"   Common Prefix: '{prefix}'")
    print(f"   Optimization Potential: {api_analysis['optimization_potential']}")
    print(f"   Potential Savings: {api_analysis['savings_percentage']}%")
    for rec in api_analysis['recommendations']:
        print(f"   💡 {rec}")
    
    # Test Case 2: AI Model Response Alignment
    print("\n2. AI Model Consensus Analysis:")
    ai_responses = [
        "The solution requires careful analysis of the data patterns",
        "The solution requires careful consideration of user needs", 
        "The solution requires careful implementation planning"
    ]
    
    consensus = analyzer.longest_common_prefix(ai_responses)
    ai_analysis = analyzer.analyze_ai_responses(ai_responses)
    
    print(f"   Consensus Prefix: '{consensus}'")
    print(f"   Alignment Score: {ai_analysis['alignment_score']}%")
    print(f"   Consensus Strength: {ai_analysis['consensus_strength']}")
    print(f"   Models in Agreement: {ai_analysis['model_count']}")
    
    # Test Case 3: No Common Prefix Scenario
    print("\n3. Diverse Endpoint Analysis:")
    diverse_endpoints = ["/users/profile", "/orders/history", "/products/catalog"]
    diverse_analysis = analyzer.analyze_api_endpoints(diverse_endpoints)
    
    prefix_result = analyzer.longest_common_prefix(diverse_endpoints)
    print(f"   Common Prefix: '{prefix_result}' (empty - no commonality)")
    print(f"   Optimization Potential: {diverse_analysis['optimization_potential']}")
    for rec in diverse_analysis['recommendations']:
        print(f"   💡 {rec}")
    
    # Test Case 4: Performance Comparison
    print("\n4. Algorithm Performance Comparison:")
    large_dataset = [f"/api/v2/service_{i}/endpoint" for i in range(100)]
    
    import time
    
    # Standard approach
    start_time = time.time()
    result1 = analyzer.longest_common_prefix(large_dataset)
    time1 = time.time() - start_time
    
    # Binary search approach
    start_time = time.time()
    result2 = analyzer.longest_common_prefix_binary_search(large_dataset)
    time2 = time.time() - start_time
    
    print(f"   Standard Algorithm: '{result1}' (Time: {time1:.6f}s)")
    print(f"   Binary Search: '{result2}' (Time: {time2:.6f}s)")
    print(f"   Results Match: {result1 == result2}")
    
    # Test Case 5: Edge Cases for Robust Enterprise Systems
    print("\n5. Edge Case Validation:")
    edge_cases = [
        ([], "Empty array"),
        (["single"], "Single string"),
        (["", "test"], "Empty string in array"),
        (["abc", "abc", "abc"], "Identical strings")
    ]
    
    for test_input, description in edge_cases:
        try:
            result = analyzer.longest_common_prefix(test_input)
            print(f"   ✅ {description}: '{result}'")
        except Exception as e:
            print(f"   ❌ {description}: ERROR - {str(e)}")
    
    print("\n" + "="*60)
    print("BUSINESS IMPACT SUMMARY:")
    print("• API Optimization: Reduced routing complexity and improved performance")
    print("• AI Alignment: Enhanced multi-model consensus validation")
    print("• Enterprise Scale: Robust handling of large datasets and edge cases")
    print("• Cost Reduction: Optimized resource utilization through pattern recognition")
    print("="*60)

if __name__ == "__main__":
    run_tests()