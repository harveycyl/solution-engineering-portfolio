class DuplicateDetector:
    """A class that finds duplicates for data deduplication and anomaly detection."""
    
    def find_duplicate(self, nums):
        """
        Core Algorithm: Find the duplicate number using Floyd's Cycle Detection.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums (list[int]): Array of n+1 integers in range [1,n]
            
        Returns:
            int: The duplicate number
        """
        # Phase 1: Detect cycle using fast and slow pointers
        slow = nums[0]
        fast = nums[0]
        
        # Move pointers until they meet (cycle detection)
        while True:
            slow = nums[slow]           # Move slow pointer one step
            fast = nums[nums[fast]]     # Move fast pointer two steps
            
            if slow == fast:
                break
        
        # Phase 2: Find the entrance of the cycle (duplicate number)
        slow = nums[0]  # Reset slow pointer to start
        
        # Move both pointers one step until they meet at cycle entrance
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow  # The duplicate number
    
    def detect_duplicate_records(self, record_ids):
        """
        Business Use Case: Enterprise Data Deduplication
        
        Identify duplicate records in data warehouse systems to maintain
        data integrity and optimize storage costs.
        
        Args:
            record_ids (list[int]): Array of record IDs with one duplicate
            
        Returns:
            dict: Deduplication analysis with cost impact
        """
        duplicate_id = self.find_duplicate(record_ids)
        
        # Calculate business metrics
        total_records = len(record_ids)
        unique_records = total_records - 1
        duplicate_count = record_ids.count(duplicate_id)
        
        # Estimate storage savings (assuming 1KB per record)
        storage_saved_kb = (duplicate_count - 1) * 1  # Keep one copy
        storage_savings_percent = ((duplicate_count - 1) / total_records) * 100
        
        # Estimate cost savings (assuming $0.023 per GB per month for cloud storage)
        monthly_cost_savings = (storage_saved_kb / (1024 * 1024)) * 0.023
        
        return {
            'duplicate_record_id': duplicate_id,
            'total_records': total_records,
            'unique_records': unique_records,
            'duplicate_occurrences': duplicate_count,
            'storage_saved_kb': storage_saved_kb,
            'storage_savings_percent': round(storage_savings_percent, 2),
            'estimated_monthly_savings_usd': round(monthly_cost_savings, 6),
            'data_quality_score': round((unique_records / total_records) * 100, 2),
            'deduplication_required': duplicate_count > 1
        }
    
    def monitor_ai_anomalies(self, prediction_sequence):
        """
        AI Orchestration Use Case: Anomaly Pattern Detection
        
        Detect recurring anomaly patterns in AI model predictions to
        identify system issues and model validation problems.
        
        Args:
            prediction_sequence (list[int]): Sequence of prediction pattern IDs
            
        Returns:
            dict: Anomaly analysis with system health metrics
        """
        anomaly_pattern = self.find_duplicate(prediction_sequence)
        
        # Calculate AI system health metrics
        total_predictions = len(prediction_sequence)
        pattern_occurrences = prediction_sequence.count(anomaly_pattern)
        anomaly_frequency = (pattern_occurrences / total_predictions) * 100
        
        # Determine system health status
        if anomaly_frequency > 50:
            health_status = "CRITICAL"
            intervention_priority = "HIGH"
        elif anomaly_frequency > 20:
            health_status = "WARNING"
            intervention_priority = "MEDIUM"
        else:
            health_status = "STABLE"
            intervention_priority = "LOW"
        
        # Calculate model reliability score
        reliability_score = max(0, 100 - (anomaly_frequency * 2))
        
        return {
            'recurring_anomaly_pattern': anomaly_pattern,
            'total_predictions': total_predictions,
            'anomaly_occurrences': pattern_occurrences,
            'anomaly_frequency_percent': round(anomaly_frequency, 2),
            'system_health_status': health_status,
            'model_reliability_score': round(reliability_score, 2),
            'intervention_priority': intervention_priority,
            'model_retraining_recommended': anomaly_frequency > 30,
            'system_stable': health_status == "STABLE"
        }

# --- Example Usage ---
def run_tests():
    """Demonstrate duplicate detection with business and AI use cases."""
    
    detector = DuplicateDetector()
    
    print("Find Duplicate Number: Data Deduplication & AI Anomaly Detection")
    print("-" * 65)
    
    # Core Algorithm Test
    print("\n1. Core Algorithm Validation:")
    test_cases = [
        ([1, 3, 4, 2, 2], "Basic duplicate"),
        ([3, 1, 3, 4, 2], "Duplicate at start"),
        ([1, 1], "Simple case"),
        ([2, 5, 9, 6, 9, 3, 8, 9, 7, 1], "Complex array")
    ]
    
    for nums, description in test_cases:
        result = detector.find_duplicate(nums)
        print(f"   {description}: {nums} -> Duplicate: {result}")
    
    # Business Use Case: Data Warehouse Deduplication
    print("\n2. Business Use Case - Data Warehouse Deduplication:")
    customer_records = [1, 3, 4, 2, 5, 2]  # Customer ID array with duplicate
    
    dedup_analysis = detector.detect_duplicate_records(customer_records)
    
    print(f"   Customer Records: {customer_records}")
    print(f"   Duplicate Customer ID: {dedup_analysis['duplicate_record_id']}")
    print(f"   Total Records: {dedup_analysis['total_records']}")
    print(f"   Duplicate Occurrences: {dedup_analysis['duplicate_occurrences']}")
    print(f"   Storage Savings: {dedup_analysis['storage_savings_percent']}%")
    print(f"   Data Quality Score: {dedup_analysis['data_quality_score']}%")
    print(f"   Monthly Cost Savings: ${dedup_analysis['estimated_monthly_savings_usd']}")
    
    # AI Use Case: Anomaly Pattern Detection
    print("\n3. AI Use Case - Model Anomaly Monitoring:")
    ai_predictions = [1, 3, 4, 2, 5, 2, 6]  # AI prediction pattern sequence
    
    anomaly_analysis = detector.monitor_ai_anomalies(ai_predictions)
    
    print(f"   Prediction Sequence: {ai_predictions}")
    print(f"   Recurring Anomaly Pattern: {anomaly_analysis['recurring_anomaly_pattern']}")
    print(f"   System Health: {anomaly_analysis['system_health_status']}")
    print(f"   Anomaly Frequency: {anomaly_analysis['anomaly_frequency_percent']}%")
    print(f"   Model Reliability: {anomaly_analysis['model_reliability_score']}%")
    print(f"   Intervention Priority: {anomaly_analysis['intervention_priority']}")
    print(f"   Retraining Recommended: {anomaly_analysis['model_retraining_recommended']}")
    
    # Edge Cases Validation
    print("\n4. Edge Cases Validation:")
    edge_cases = [
        ([1, 1], "Minimum case"),
        ([2, 1, 2], "Three elements"),
        ([1, 2, 3, 4, 4], "Duplicate at end")
    ]
    
    for test_array, description in edge_cases:
        result = detector.find_duplicate(test_array)
        print(f"   {description}: {test_array} -> Duplicate: {result}")

if __name__ == "__main__":
    run_tests()