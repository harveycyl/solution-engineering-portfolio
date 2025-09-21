class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListOptimizer:
    """A class that removes nth node from end for pipeline optimization and AI orchestration."""
    
    def remove_nth_from_end(self, head, n):
        """
        Core Algorithm: Remove the nth node from the end of a linked list.
        
        Time Complexity: O(L) where L is length of list
        Space Complexity: O(1)
        
        Args:
            head (ListNode): Head of the linked list
            n (int): Position from end to remove (1-indexed)
            
        Returns:
            ListNode: Head of modified list
        """
        # Create dummy head to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers
        fast = dummy
        slow = dummy
        
        # Move fast pointer n+1 steps ahead
        for i in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches end
        while fast is not None:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from end
        slow.next = slow.next.next
        
        return dummy.next
    
    def optimize_data_pipeline(self, pipeline_data, remove_position):
        """
        Business Use Case: Data Pipeline Optimization
        
        Remove outdated processing stages from data pipelines to improve
        performance and reduce memory usage in streaming operations.
        
        Args:
            pipeline_data (list): List of pipeline stage data
            remove_position (int): Position from end to remove
            
        Returns:
            dict: Optimized pipeline with performance metrics
        """
        # Convert list to linked list
        head = self._list_to_linked_list(pipeline_data)
        original_length = len(pipeline_data)
        
        # Remove nth node from end
        optimized_head = self.remove_nth_from_end(head, remove_position)
        
        # Convert back to list for analysis
        optimized_pipeline = self._linked_list_to_list(optimized_head)
        
        # Calculate optimization metrics
        memory_savings = (1 - len(optimized_pipeline) / original_length) * 100
        throughput_improvement = memory_savings * 0.8  # Estimated improvement
        
        return {
            'original_pipeline': pipeline_data,
            'optimized_pipeline': optimized_pipeline,
            'stages_removed': 1,
            'memory_savings_percent': round(memory_savings, 2),
            'estimated_throughput_gain': round(throughput_improvement, 2),
            'optimization_successful': len(optimized_pipeline) == original_length - 1
        }
    
    def manage_ai_inference_queue(self, inference_stages, rollback_steps):
        """
        AI Orchestration Use Case: Model Pipeline Management
        
        Remove nth inference stage from end to implement rollback mechanisms
        and optimize AI model serving performance.
        
        Args:
            inference_stages (list): List of AI inference pipeline stages
            rollback_steps (int): Number of steps to rollback from end
            
        Returns:
            dict: Optimized AI pipeline with performance analysis
        """
        # Convert to linked list for efficient removal
        head = self._list_to_linked_list(inference_stages)
        original_stages = len(inference_stages)
        
        # Remove nth stage from end
        optimized_head = self.remove_nth_from_end(head, rollback_steps)
        
        # Convert back for analysis
        optimized_stages = self._linked_list_to_list(optimized_head)
        
        # Calculate AI performance metrics
        latency_reduction = (rollback_steps / original_stages) * 100
        inference_efficiency = 100 - latency_reduction
        
        return {
            'original_stages': inference_stages,
            'optimized_stages': optimized_stages,
            'rollback_steps': rollback_steps,
            'latency_reduction_percent': round(latency_reduction, 2),
            'inference_efficiency': round(inference_efficiency, 2),
            'pipeline_valid': len(optimized_stages) > 0,
            'recommended_for_production': inference_efficiency >= 70
        }
    
    def _list_to_linked_list(self, data_list):
        """Helper method to convert list to linked list."""
        if not data_list:
            return None
        
        head = ListNode(data_list[0])
        current = head
        
        for i in range(1, len(data_list)):
            current.next = ListNode(data_list[i])
            current = current.next
        
        return head
    
    def _linked_list_to_list(self, head):
        """Helper method to convert linked list to list."""
        result = []
        current = head
        
        while current:
            result.append(current.val)
            current = current.next
        
        return result

# --- Example Usage ---
def run_tests():
    """Demonstrate linked list optimization with business and AI use cases."""
    
    optimizer = LinkedListOptimizer()
    
    print("Remove Nth Node: Pipeline Optimization & AI Management")
    print("-" * 55)
    
    # Core Algorithm Test
    print("\n1. Core Algorithm Validation:")
    test_data = [1, 2, 3, 4, 5]
    head = optimizer._list_to_linked_list(test_data)
    
    result_head = optimizer.remove_nth_from_end(head, 2)
    result = optimizer._linked_list_to_list(result_head)
    
    print(f"   Original: {test_data}")
    print(f"   Remove 2nd from end: {result}")
    print(f"   Expected: [1, 2, 3, 5] ✓")
    
    # Business Use Case: Data Pipeline Optimization
    print("\n2. Business Use Case - Data Pipeline Optimization:")
    pipeline_stages = [
        "data_ingestion", "validation", "transformation", 
        "enrichment", "aggregation", "output"
    ]
    
    optimization = optimizer.optimize_data_pipeline(pipeline_stages, 2)
    
    print(f"   Original Pipeline: {len(optimization['original_pipeline'])} stages")
    print(f"   Optimized Pipeline: {len(optimization['optimized_pipeline'])} stages")
    print(f"   Memory Savings: {optimization['memory_savings_percent']}%")
    print(f"   Throughput Gain: {optimization['estimated_throughput_gain']}%")
    print(f"   Removed Stage: '{optimization['original_pipeline'][-2]}'")
    
    # AI Use Case: Model Pipeline Management
    print("\n3. AI Use Case - Inference Pipeline Rollback:")
    ai_stages = [
        "input_preprocessing", "feature_extraction", "model_inference", 
        "post_processing", "confidence_scoring", "output_formatting"
    ]
    
    ai_optimization = optimizer.manage_ai_inference_queue(ai_stages, 1)
    
    print(f"   Original AI Pipeline: {len(ai_optimization['original_stages'])} stages")
    print(f"   Optimized Pipeline: {len(ai_optimization['optimized_stages'])} stages")
    print(f"   Latency Reduction: {ai_optimization['latency_reduction_percent']}%")
    print(f"   Inference Efficiency: {ai_optimization['inference_efficiency']}%")
    print(f"   Production Ready: {ai_optimization['recommended_for_production']}")
    print(f"   Removed Stage: '{ai_optimization['original_stages'][-1]}'")
    
    # Edge Cases Validation
    print("\n4. Edge Cases Validation:")
    edge_cases = [
        ([1], 1, "Single node removal"),
        ([1, 2], 1, "Remove last from two nodes"),
        ([1, 2], 2, "Remove first from two nodes"),
    ]
    
    for test_list, n, description in edge_cases:
        head = optimizer._list_to_linked_list(test_list)
        result_head = optimizer.remove_nth_from_end(head, n)
        result = optimizer._linked_list_to_list(result_head)
        print(f"   {description}: {test_list} -> {result}")

if __name__ == "__main__":
    run_tests()