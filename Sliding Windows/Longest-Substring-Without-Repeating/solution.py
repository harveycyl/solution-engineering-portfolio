class UniqueWindowOptimizer:
    """A class that finds longest unique windows for session management and AI optimization."""
    
    def longest_substring_without_repeating(self, input_str):
        """
        Core Algorithm: Find length of longest substring without repeating characters.
        
        Time Complexity: O(n)
        Space Complexity: O(min(m,n)) where m is character set size
        
        Args:
            input_str (str): Input string of letters, digits, and spaces
            
        Returns:
            int: Length of longest substring without repeating characters
        """
        if not input_str:
            return 0
        
        char_index_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(input_str)):
            current_char = input_str[right]
            
            # If character already seen in current window, move left pointer
            if current_char in char_index_map and char_index_map[current_char] >= left:
                left = char_index_map[current_char] + 1
            
            # Update character's latest position
            char_index_map[current_char] = right
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    def optimize_user_sessions(self, activity_sequence):
        """
        Business Use Case: User Session Management
        
        Optimize user session lengths by finding longest periods without
        duplicate activities to improve user experience and system efficiency.
        
        Args:
            activity_sequence (str): Sequence of user activities
            
        Returns:
            dict: Session optimization analysis
        """
        optimal_session_length = self.longest_substring_without_repeating(activity_sequence)
        
        # Calculate session metrics
        total_activities = len(activity_sequence)
        session_efficiency = (optimal_session_length / total_activities) * 100
        
        # Analyze activity distribution
        unique_activities = len(set(activity_sequence))
        activity_diversity = unique_activities / total_activities if total_activities > 0 else 0
        
        # Calculate duplicate reduction potential
        duplicates_count = total_activities - unique_activities
        duplicate_reduction = (duplicates_count / total_activities) * 100 if total_activities > 0 else 0
        
        # Estimate system efficiency gains
        cache_hit_improvement = min(50, session_efficiency * 0.8)  # Cap at 50%
        memory_savings = duplicate_reduction * 0.6  # Estimated memory savings
        
        return {
            'optimal_session_length': optimal_session_length,
            'total_activities': total_activities,
            'session_efficiency_percent': round(session_efficiency, 2),
            'unique_activities_count': unique_activities,
            'activity_diversity_score': round(activity_diversity, 3),
            'duplicate_reduction_percent': round(duplicate_reduction, 2),
            'estimated_cache_improvement': round(cache_hit_improvement, 2),
            'estimated_memory_savings': round(memory_savings, 2),
            'session_optimization_recommended': session_efficiency < 70,
            'system_efficiency_good': session_efficiency >= 60
        }
    
    def optimize_ai_context_window(self, token_sequence):
        """
        AI Orchestration Use Case: Context Window Optimization
        
        Find optimal AI context window with unique tokens to maximize
        information density and improve inference efficiency.
        
        Args:
            token_sequence (str): Sequence of AI context tokens
            
        Returns:
            dict: AI context optimization analysis
        """
        optimal_context_length = self.longest_substring_without_repeating(token_sequence)
        
        # Calculate AI efficiency metrics
        total_tokens = len(token_sequence)
        context_utilization = (optimal_context_length / total_tokens) * 100
        
        # Analyze token diversity
        unique_tokens = len(set(token_sequence))
        token_diversity = unique_tokens / total_tokens if total_tokens > 0 else 0
        
        # Calculate information density
        information_density = (optimal_context_length / max(1, unique_tokens)) * 100
        redundancy_ratio = (total_tokens - unique_tokens) / total_tokens if total_tokens > 0 else 0
        
        # Estimate performance improvements
        inference_speedup = min(40, context_utilization * 0.5)  # Cap at 40%
        token_efficiency = (1 - redundancy_ratio) * 100
        
        return {
            'optimal_context_length': optimal_context_length,
            'total_tokens': total_tokens,
            'context_utilization_percent': round(context_utilization, 2),
            'unique_tokens_count': unique_tokens,
            'token_diversity_score': round(token_diversity, 3),
            'information_density_score': round(information_density, 2),
            'redundancy_ratio': round(redundancy_ratio, 3),
            'estimated_inference_speedup': round(inference_speedup, 2),
            'token_efficiency_percent': round(token_efficiency, 2),
            'context_optimization_needed': context_utilization < 80,
            'ai_performance_optimal': context_utilization >= 75
        }

# --- Example Usage ---
def run_tests():
    """Demonstrate unique window optimization with business and AI use cases."""
    
    optimizer = UniqueWindowOptimizer()
    
    print("Longest Substring Without Repeating: Session & AI Context Optimization")
    print("-" * 70)
    
    # Core Algorithm Test
    print("\n1. Core Algorithm Validation:")
    test_cases = [
        ("abcabcbb", "Classic example"),
        ("bbbbb", "All same characters"),
        ("pwwkew", "Mixed pattern"),
        ("abcdef", "All unique"),
        ("", "Empty string")
    ]
    
    for string, description in test_cases:
        result = optimizer.longest_substring_without_repeating(string)
        print(f"   {description}: '{string}' -> Length: {result}")
    
    # Business Use Case: User Session Management
    print("\n2. Business Use Case - User Session Optimization:")
    user_activities = "abcabcbb"  # User activity sequence
    
    session_analysis = optimizer.optimize_user_sessions(user_activities)
    
    print(f"   Activity Sequence: '{user_activities}'")
    print(f"   Optimal Session Length: {session_analysis['optimal_session_length']} activities")
    print(f"   Session Efficiency: {session_analysis['session_efficiency_percent']}%")
    print(f"   Unique Activities: {session_analysis['unique_activities_count']}")
    print(f"   Activity Diversity: {session_analysis['activity_diversity_score']}")
    print(f"   Cache Improvement: {session_analysis['estimated_cache_improvement']}%")
    print(f"   Memory Savings: {session_analysis['estimated_memory_savings']}%")
    print(f"   System Efficiency: {'Good' if session_analysis['system_efficiency_good'] else 'Needs Optimization'}")
    
    # AI Use Case: Context Window Optimization
    print("\n3. AI Use Case - Context Window Optimization:")
    ai_tokens = "pwwkew"  # AI context token sequence
    
    ai_analysis = optimizer.optimize_ai_context_window(ai_tokens)
    
    print(f"   Token Sequence: '{ai_tokens}'")
    print(f"   Optimal Context Length: {ai_analysis['optimal_context_length']} tokens")
    print(f"   Context Utilization: {ai_analysis['context_utilization_percent']}%")
    print(f"   Token Diversity: {ai_analysis['token_diversity_score']}")
    print(f"   Information Density: {ai_analysis['information_density_score']}")
    print(f"   Redundancy Ratio: {ai_analysis['redundancy_ratio']}")
    print(f"   Inference Speedup: {ai_analysis['estimated_inference_speedup']}%")
    print(f"   Token Efficiency: {ai_analysis['token_efficiency_percent']}%")
    print(f"   AI Performance: {'Optimal' if ai_analysis['ai_performance_optimal'] else 'Needs Optimization'}")
    
    # Edge Cases Validation
    print("\n4. Edge Cases Validation:")
    edge_cases = [
        ("a", "Single character"),
        ("ab", "Two unique characters"),
        ("aa", "Two same characters"),
        ("abc123", "Mixed letters and digits")
    ]
    
    for string, description in edge_cases:
        result = optimizer.longest_substring_without_repeating(string)
        print(f"   {description}: '{string}' -> Length: {result}")

if __name__ == "__main__":
    run_tests()