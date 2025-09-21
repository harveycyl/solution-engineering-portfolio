class CircularArrayAnalyzer:
    """A class that detects circular loops for system deadlock detection and AI training monitoring."""
    
    def circular_array_loop(self, nums):
        """
        Core Algorithm: Detect if circular array contains a valid cycle.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums (list[int]): Circular array of non-zero integers
            
        Returns:
            bool: True if valid cycle exists, False otherwise
        """
        if len(nums) < 2:
            return False
        
        for i in range(len(nums)):
            if nums[i] == 0:  # Already visited, skip
                continue
            
            # Use fast and slow pointers from current position
            slow = i
            fast = i
            
            # Check if we can form a valid cycle from this starting point
            while True:
                # Move slow pointer one step
                slow = self._get_next_index(nums, slow)
                
                # Move fast pointer two steps
                fast = self._get_next_index(nums, fast)
                if fast != -1:
                    fast = self._get_next_index(nums, fast)
                
                # Invalid cycle conditions
                if fast == -1 or slow == -1:
                    break
                
                # Cycle detected
                if slow == fast:
                    # Verify cycle length > 1
                    if slow == self._get_next_index(nums, slow):
                        break  # Self-loop, invalid
                    return True
            
            # Mark all visited nodes in this path as invalid
            self._mark_path_invalid(nums, i)
        
        return False
    
    def detect_system_deadlock(self, service_dependencies):
        """
        Business Use Case: Distributed System Deadlock Detection
        
        Analyze microservice dependencies to detect circular patterns
        that could cause system deadlocks and service unavailability.
        
        Args:
            service_dependencies (list[int]): Service dependency pattern
            
        Returns:
            dict: Deadlock analysis with system health metrics
        """
        has_deadlock = self.circular_array_loop(service_dependencies.copy())
        
        # Calculate system health metrics
        total_services = len(service_dependencies)
        positive_deps = sum(1 for dep in service_dependencies if dep > 0)
        negative_deps = total_services - positive_deps
        
        dependency_balance = abs(positive_deps - negative_deps) / total_services
        risk_level = "HIGH" if has_deadlock else "MEDIUM" if dependency_balance > 0.7 else "LOW"
        
        return {
            'has_deadlock': has_deadlock,
            'total_services': total_services,
            'forward_dependencies': positive_deps,
            'backward_dependencies': negative_deps,
            'dependency_balance': round(dependency_balance, 3),
            'risk_level': risk_level,
            'system_stable': not has_deadlock,
            'intervention_required': has_deadlock
        }
    
    def monitor_training_convergence(self, gradient_pattern):
        """
        AI Orchestration Use Case: Training Loop Detection
        
        Monitor AI model training gradients to detect oscillating patterns
        that indicate non-converging training loops requiring intervention.
        
        Args:
            gradient_pattern (list[float]): Sequence of gradient values
            
        Returns:
            dict: Training convergence analysis
        """
        # Convert gradients to integer pattern (multiply by 1000 for precision)
        int_pattern = [int(grad * 1000) for grad in gradient_pattern if grad != 0]
        
        if not int_pattern:
            return {'training_stable': True, 'convergence_issue': False}
        
        has_loop = self.circular_array_loop(int_pattern.copy())
        
        # Calculate training efficiency metrics
        gradient_variance = self._calculate_variance(gradient_pattern)
        oscillation_score = gradient_variance * 100  # Scale for interpretation
        
        training_efficiency = 100 - min(oscillation_score, 90)  # Cap at 90% reduction
        
        return {
            'has_training_loop': has_loop,
            'gradient_samples': len(gradient_pattern),
            'gradient_variance': round(gradient_variance, 6),
            'oscillation_score': round(oscillation_score, 2),
            'training_efficiency': round(training_efficiency, 2),
            'convergence_issue': has_loop,
            'intervention_recommended': has_loop or oscillation_score > 50,
            'training_stable': not has_loop and oscillation_score <= 30
        }
    
    def _get_next_index(self, nums, current):
        """Helper method to get next valid index maintaining direction."""
        direction = 1 if nums[current] > 0 else -1
        next_idx = (current + nums[current]) % len(nums)
        
        # Check if next step maintains same direction
        next_direction = 1 if nums[next_idx] > 0 else -1
        
        if direction != next_direction:
            return -1  # Direction change, invalid cycle
        
        return next_idx
    
    def _mark_path_invalid(self, nums, start):
        """Helper method to mark visited path as invalid."""
        current = start
        while nums[current] != 0:
            next_idx = (current + nums[current]) % len(nums)
            nums[current] = 0  # Mark as visited
            current = next_idx
    
    def _calculate_variance(self, values):
        """Helper method to calculate variance of gradient values."""
        if not values:
            return 0
        mean = sum(values) / len(values)
        return sum((v - mean) ** 2 for v in values) / len(values)

# --- Example Usage ---
def run_tests():
    """Demonstrate circular array loop detection with business and AI use cases."""
    
    analyzer = CircularArrayAnalyzer()
    
    print("Circular Array Loop: Deadlock Detection & AI Training Monitoring")
    print("-" * 65)
    
    # Core Algorithm Test
    print("\n1. Core Algorithm Validation:")
    test_cases = [
        ([2, -1, 1, 2, 2], "Has valid cycle"),
        ([1, 2], "No valid cycle"),
        ([2, 1, -1, -2], "Mixed directions"),
        ([-1, 2], "Short array")
    ]
    
    for nums, description in test_cases:
        result = analyzer.circular_array_loop(nums.copy())
        status = "✓ CYCLE FOUND" if result else "✗ NO CYCLE"
        print(f"   {status}: {description} - {nums}")
    
    # Business Use Case: System Deadlock Detection
    print("\n2. Business Use Case - Distributed System Health:")
    service_deps = [3, -2, 1, 2, -1]  # Service dependency pattern
    
    deadlock_analysis = analyzer.detect_system_deadlock(service_deps)
    
    print(f"   Service Dependencies: {service_deps}")
    print(f"   System Stable: {deadlock_analysis['system_stable']}")
    print(f"   Deadlock Detected: {deadlock_analysis['has_deadlock']}")
    print(f"   Risk Level: {deadlock_analysis['risk_level']}")
    print(f"   Forward Dependencies: {deadlock_analysis['forward_dependencies']}")
    print(f"   Intervention Required: {deadlock_analysis['intervention_required']}")
    
    # AI Use Case: Training Loop Detection
    print("\n3. AI Use Case - Training Convergence Monitoring:")
    gradients = [0.5, -0.3, 0.2, 0.5, -0.3, 0.1]  # Training gradient progression
    
    training_analysis = analyzer.monitor_training_convergence(gradients)
    
    print(f"   Gradient Pattern: {gradients}")
    print(f"   Training Stable: {training_analysis['training_stable']}")
    print(f"   Loop Detected: {training_analysis['has_training_loop']}")
    print(f"   Training Efficiency: {training_analysis['training_efficiency']}%")
    print(f"   Oscillation Score: {training_analysis['oscillation_score']}")
    print(f"   Intervention Recommended: {training_analysis['intervention_recommended']}")
    
    # Edge Cases Validation
    print("\n4. Edge Cases Validation:")
    edge_cases = [
        ([1], "Single element"),
        ([1, 1], "Self-loops only"),
        ([2, -2], "Alternating pattern"),
    ]
    
    for test_array, description in edge_cases:
        result = analyzer.circular_array_loop(test_array.copy())
        print(f"   {description}: {test_array} -> {'Cycle' if result else 'No Cycle'}")

if __name__ == "__main__":
    run_tests()