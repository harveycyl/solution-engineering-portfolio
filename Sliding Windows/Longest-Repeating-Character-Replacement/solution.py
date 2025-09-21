class SlidingWindowOptimizer:
    """A class that optimizes windows for quality control and AI model tuning."""
    
    def character_replacement(self, s, k):
        """
        Core Algorithm: Find longest substring with identical characters using ≤k replacements.
        
        Time Complexity: O(n)
        Space Complexity: O(1) for fixed alphabet size
        
        Args:
            s (str): Input string of uppercase English characters
            k (int): Maximum number of character replacements allowed
            
        Returns:
            int: Length of longest valid substring
        """
        if not s:
            return 0
        
        left = 0
        max_frequency = 0
        max_length = 0
        char_count = {}
        
        for right in range(len(s)):
            # Add current character to window
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, char_count[s[right]])
            
            # Check if current window is valid
            window_size = right - left + 1
            replacements_needed = window_size - max_frequency
            
            # Shrink window if too many replacements needed
            if replacements_needed > k:
                char_count[s[left]] -= 1
                left += 1
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    def optimize_production_quality(self, quality_sequence, max_corrections):
        """
        Business Use Case: Manufacturing Quality Control
        
        Find the longest production run that maintains quality standards
        with at most k quality corrections/interventions.
        
        Args:
            quality_sequence (str): Sequence of quality states (A=good, B=defect, etc.)
            max_corrections (int): Maximum corrections allowed in production window
            
        Returns:
            dict: Production optimization analysis
        """
        optimal_length = self.character_replacement(quality_sequence, max_corrections)
        
        # Calculate production metrics
        total_production = len(quality_sequence)
        efficiency_gain = (optimal_length / total_production) * 100
        
        # Analyze quality distribution
        quality_distribution = {}
        for state in quality_sequence:
            quality_distribution[state] = quality_distribution.get(state, 0) + 1
        
        # Calculate waste reduction
        baseline_defects = sum(count for state, count in quality_distribution.items() if state != 'A')
        optimized_waste = max(0, optimal_length - quality_distribution.get('A', 0))
        waste_reduction = max(0, baseline_defects - optimized_waste)
        
        return {
            'optimal_run_length': optimal_length,
            'total_production_units': total_production,
            'efficiency_improvement_percent': round(efficiency_gain, 2),
            'max_corrections_allowed': max_corrections,
            'quality_distribution': quality_distribution,
            'estimated_waste_reduction': waste_reduction,
            'production_optimization_score': min(100, efficiency_gain + (waste_reduction / total_production * 100)),
            'quality_control_effective': optimal_length > total_production * 0.6
        }
    
    def optimize_ai_training_stability(self, performance_states, max_adjustments):
        """
        AI Orchestration Use Case: Model Training Optimization
        
        Find the longest stable training period with at most k hyperparameter
        adjustments to maximize model consistency and training efficiency.
        
        Args:
            performance_states (str): Training performance state sequence
            max_adjustments (int): Maximum hyperparameter adjustments allowed
            
        Returns:
            dict: AI training optimization analysis
        """
        optimal_stability = self.character_replacement(performance_states, max_adjustments)
        
        # Calculate training efficiency metrics
        total_epochs = len(performance_states)
        stability_ratio = optimal_stability / total_epochs
        training_efficiency = stability_ratio * 100
        
        # Analyze performance state distribution
        state_distribution = {}
        for state in performance_states:
            state_distribution[state] = state_distribution.get(state, 0) + 1
        
        # Determine dominant performance state
        dominant_state = max(state_distribution.items(), key=lambda x: x[1])[0]
        consistency_score = (state_distribution[dominant_state] / total_epochs) * 100
        
        # Calculate intervention efficiency
        intervention_efficiency = (optimal_stability / max(1, max_adjustments)) if max_adjustments > 0 else optimal_stability
        
        return {
            'optimal_stability_window': optimal_stability,
            'total_training_epochs': total_epochs,
            'training_efficiency_percent': round(training_efficiency, 2),
            'max_adjustments_budget': max_adjustments,
            'performance_state_distribution': state_distribution,
            'dominant_performance_state': dominant_state,
            'model_consistency_score': round(consistency_score, 2),
            'intervention_efficiency': round(intervention_efficiency, 2),
            'training_optimization_recommended': stability_ratio < 0.7,
            'model_training_stable': stability_ratio >= 0.8
        }

# --- Example Usage ---
def run_tests():
    """Demonstrate sliding window optimization with business and AI use cases."""
    
    optimizer = SlidingWindowOptimizer()
    
    print("Longest Repeating Character Replacement: Quality Control & AI Optimization")
    print("-" * 70)
    
    # Core Algorithm Test
    print("\n1. Core Algorithm Validation:")
    test_cases = [
        ("ABAB", 2, "Basic replacement"),
        ("AABABBA", 1, "Single replacement"),
        ("ABCDE", 4, "Maximum replacements"),
        ("AAAA", 0, "No replacements needed")
    ]
    
    for string, k, description in test_cases:
        result = optimizer.character_replacement(string, k)
        print(f"   {description}: '{string}' with k={k} -> Length: {result}")
    
    # Business Use Case: Manufacturing Quality Control
    print("\n2. Business Use Case - Production Quality Optimization:")
    production_data = "AAABBACCCA"  # A=good quality, B=defect, C=minor issue
    max_corrections = 2
    
    quality_analysis = optimizer.optimize_production_quality(production_data, max_corrections)
    
    print(f"   Production Sequence: '{production_data}'")
    print(f"   Max Corrections Allowed: {max_corrections}")
    print(f"   Optimal Run Length: {quality_analysis['optimal_run_length']} units")
    print(f"   Efficiency Improvement: {quality_analysis['efficiency_improvement_percent']}%")
    print(f"   Quality Distribution: {quality_analysis['quality_distribution']}")
    print(f"   Waste Reduction: {quality_analysis['estimated_waste_reduction']} units")
    print(f"   Optimization Score: {quality_analysis['production_optimization_score']:.1f}/100")
    
    # AI Use Case: Training Stability Optimization
    print("\n3. AI Use Case - Model Training Stability:")
    training_states = "AAABBACCCA"  # A=stable, B=unstable, C=marginal
    max_adjustments = 2
    
    training_analysis = optimizer.optimize_ai_training_stability(training_states, max_adjustments)
    
    print(f"   Training States: '{training_states}'")
    print(f"   Max Adjustments Budget: {max_adjustments}")
    print(f"   Optimal Stability Window: {training_analysis['optimal_stability_window']} epochs")
    print(f"   Training Efficiency: {training_analysis['training_efficiency_percent']}%")
    print(f"   Dominant State: '{training_analysis['dominant_performance_state']}'")
    print(f"   Model Consistency: {training_analysis['model_consistency_score']}%")
    print(f"   Intervention Efficiency: {training_analysis['intervention_efficiency']:.1f}")
    print(f"   Training Stable: {training_analysis['model_training_stable']}")
    
    # Edge Cases Validation
    print("\n4. Edge Cases Validation:")
    edge_cases = [
        ("A", 0, "Single character"),
        ("AB", 1, "Two different characters"),
        ("AAA", 5, "Replacements > needed"),
    ]
    
    for string, k, description in edge_cases:
        result = optimizer.character_replacement(string, k)
        print(f"   {description}: '{string}' with k={k} -> Length: {result}")

if __name__ == "__main__":
    run_tests()