class IntervalMerger:
    """A class that merges overlapping intervals for scheduling and workload optimization."""
    
    def merge_intervals(self, intervals):
        """
        Core Algorithm: Merge overlapping intervals into non-overlapping intervals.
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(n) for the result array
        
        Args:
            intervals (List[List[int]]): Array of intervals [start, end]
            
        Returns:
            List[List[int]]: Merged non-overlapping intervals
        """
        if not intervals:
            return []
        
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            # Get the last merged interval
            last_merged = merged[-1]
            
            # If current interval overlaps with last merged interval
            if current[0] <= last_merged[1]:
                # Merge by updating the end time
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, add current interval to result
                merged.append(current)
        
        return merged
    
    def optimize_meeting_schedule(self, meeting_requests):
        """
        Business Use Case: Meeting and Resource Scheduling
        
        Optimize conference room bookings by merging overlapping meeting
        requests to identify actual usage patterns and prevent conflicts.
        
        Args:
            meeting_requests (List[List[int]]): Meeting time slots [start_hour, end_hour]
            
        Returns:
            dict: Schedule optimization analysis
        """
        original_meetings = len(meeting_requests)
        if original_meetings == 0:
            return self._empty_schedule_analysis()
        
        # Merge overlapping meeting slots
        optimized_schedule = self.merge_intervals(meeting_requests)
        optimized_meetings = len(optimized_schedule)
        
        # Calculate schedule efficiency metrics
        total_original_hours = sum(end - start for start, end in meeting_requests)
        total_optimized_hours = sum(end - start for start, end in optimized_schedule)
        
        # Calculate conflict resolution metrics
        conflicts_resolved = original_meetings - optimized_meetings
        conflict_reduction_rate = (conflicts_resolved / original_meetings) * 100
        
        # Calculate room utilization efficiency
        time_savings = total_original_hours - total_optimized_hours
        utilization_improvement = (time_savings / total_original_hours) * 100 if total_original_hours > 0 else 0
        
        # Calculate availability gaps
        availability_gaps = self._calculate_gaps(optimized_schedule)
        
        # Estimate business value
        room_cost_per_hour = 50  # Estimated cost
        cost_savings = time_savings * room_cost_per_hour
        productivity_gain = conflicts_resolved * 0.5  # Hours saved per conflict
        
        return {
            'original_meeting_requests': original_meetings,
            'optimized_meeting_blocks': optimized_meetings,
            'conflicts_resolved': conflicts_resolved,
            'conflict_reduction_rate': round(conflict_reduction_rate, 2),
            'total_hours_saved': time_savings,
            'utilization_improvement_percent': round(utilization_improvement, 2),
            'availability_gaps': availability_gaps,
            'estimated_cost_savings': round(cost_savings, 2),
            'productivity_hours_gained': round(productivity_gain, 2),
            'optimized_schedule': optimized_schedule,
            'schedule_efficiency_good': conflict_reduction_rate >= 20,
            'high_utilization_achieved': utilization_improvement >= 15
        }
    
    def optimize_ai_workload_schedule(self, processing_jobs):
        """
        AI Orchestration Use Case: Computational Workload Optimization
        
        Merge overlapping AI processing jobs to optimize GPU utilization
        and prevent resource contention in distributed AI systems.
        
        Args:
            processing_jobs (List[List[int]]): AI job time windows [start_time, end_time]
            
        Returns:
            dict: AI workload optimization analysis
        """
        original_jobs = len(processing_jobs)
        if original_jobs == 0:
            return self._empty_workload_analysis()
        
        # Merge overlapping processing windows
        optimized_workload = self.merge_intervals(processing_jobs)
        optimized_jobs = len(optimized_workload)
        
        # Calculate computational efficiency metrics
        total_original_compute_time = sum(end - start for start, end in processing_jobs)
        total_optimized_compute_time = sum(end - start for start, end in optimized_workload)
        
        # Calculate resource contention reduction
        contention_eliminated = original_jobs - optimized_jobs
        contention_reduction_rate = (contention_eliminated / original_jobs) * 100
        
        # Calculate GPU utilization optimization
        compute_time_saved = total_original_compute_time - total_optimized_compute_time
        gpu_efficiency_gain = (compute_time_saved / total_original_compute_time) * 100 if total_original_compute_time > 0 else 0
        
        # Calculate processing gaps for scaling decisions
        processing_gaps = self._calculate_gaps(optimized_workload)
        
        # Estimate performance improvements
        throughput_increase = min(50, contention_reduction_rate * 1.2)  # Cap at 50%
        memory_efficiency = (1 - (contention_eliminated / original_jobs)) * 100 if original_jobs > 0 else 100
        
        # Calculate cost efficiency
        gpu_hour_cost = 2.50  # Estimated GPU cost per hour
        infrastructure_savings = compute_time_saved * gpu_hour_cost
        
        return {
            'original_job_requests': original_jobs,
            'optimized_job_blocks': optimized_jobs,
            'contention_eliminated': contention_eliminated,
            'contention_reduction_rate': round(contention_reduction_rate, 2),
            'compute_hours_saved': compute_time_saved,
            'gpu_efficiency_gain_percent': round(gpu_efficiency_gain, 2),
            'processing_gaps': processing_gaps,
            'estimated_throughput_increase': round(throughput_increase, 2),
            'memory_efficiency_percent': round(memory_efficiency, 2),
            'infrastructure_cost_savings': round(infrastructure_savings, 2),
            'optimized_schedule': optimized_workload,
            'workload_optimization_effective': contention_reduction_rate >= 25,
            'high_gpu_efficiency': gpu_efficiency_gain >= 20
        }
    
    def _calculate_gaps(self, merged_intervals):
        """Calculate gaps between merged intervals for availability analysis."""
        if len(merged_intervals) <= 1:
            return []
        
        gaps = []
        for i in range(len(merged_intervals) - 1):
            gap_start = merged_intervals[i][1]
            gap_end = merged_intervals[i + 1][0]
            if gap_end > gap_start:
                gaps.append([gap_start, gap_end])
        
        return gaps
    
    def _empty_schedule_analysis(self):
        """Return empty analysis for no meeting requests."""
        return {
            'original_meeting_requests': 0,
            'optimized_meeting_blocks': 0,
            'conflicts_resolved': 0,
            'conflict_reduction_rate': 0,
            'total_hours_saved': 0,
            'utilization_improvement_percent': 0,
            'availability_gaps': [],
            'estimated_cost_savings': 0,
            'productivity_hours_gained': 0,
            'optimized_schedule': [],
            'schedule_efficiency_good': True,
            'high_utilization_achieved': False
        }
    
    def _empty_workload_analysis(self):
        """Return empty analysis for no processing jobs."""
        return {
            'original_job_requests': 0,
            'optimized_job_blocks': 0,
            'contention_eliminated': 0,
            'contention_reduction_rate': 0,
            'compute_hours_saved': 0,
            'gpu_efficiency_gain_percent': 0,
            'processing_gaps': [],
            'estimated_throughput_increase': 0,
            'memory_efficiency_percent': 100,
            'infrastructure_cost_savings': 0,
            'optimized_schedule': [],
            'workload_optimization_effective': True,
            'high_gpu_efficiency': False
        }

# --- Example Usage ---
def run_tests():
    """Demonstrate interval merging with business and AI use cases."""
    
    merger = IntervalMerger()
    
    print("Merge Intervals: Scheduling & Workload Optimization")
    print("-" * 55)
    
    # Core Algorithm Test
    print("\n1. Core Algorithm Validation:")
    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]], "Standard overlapping intervals"),
        ([[1,4],[4,5]], "Adjacent intervals"),
        ([[1,4],[2,3]], "Contained intervals"),
        ([[1,4],[0,2],[3,5]], "Multiple overlaps"),
        ([[1,1]], "Single point interval")
    ]
    
    for intervals, description in test_cases:
        result = merger.merge_intervals(intervals)
        print(f"   {description}: {intervals} -> {result}")
    
    # Business Use Case: Meeting Schedule Optimization
    print("\n2. Business Use Case - Meeting Schedule Optimization:")
    meeting_requests = [[9,10],[10,12],[11,13],[14,16],[15,17]]  # Conference room bookings
    
    schedule_analysis = merger.optimize_meeting_schedule(meeting_requests)
    
    print(f"   Original Meeting Requests: {meeting_requests}")
    print(f"   Optimized Schedule: {schedule_analysis['optimized_schedule']}")
    print(f"   Meetings: {schedule_analysis['original_meeting_requests']} -> {schedule_analysis['optimized_meeting_blocks']}")
    print(f"   Conflicts Resolved: {schedule_analysis['conflicts_resolved']}")
    print(f"   Conflict Reduction: {schedule_analysis['conflict_reduction_rate']}%")
    print(f"   Hours Saved: {schedule_analysis['total_hours_saved']}")
    print(f"   Utilization Improvement: {schedule_analysis['utilization_improvement_percent']}%")
    print(f"   Cost Savings: ${schedule_analysis['estimated_cost_savings']}")
    print(f"   Productivity Gained: {schedule_analysis['productivity_hours_gained']} hours")
    print(f"   Schedule Efficiency: {'Good' if schedule_analysis['schedule_efficiency_good'] else 'Needs Improvement'}")
    
    # AI Use Case: Workload Optimization
    print("\n3. AI Use Case - Computational Workload Optimization:")
    ai_jobs = [[1,3],[2,6],[8,10],[15,18],[16,20]]  # AI processing jobs
    
    workload_analysis = merger.optimize_ai_workload_schedule(ai_jobs)
    
    print(f"   Original AI Jobs: {ai_jobs}")
    print(f"   Optimized Workload: {workload_analysis['optimized_schedule']}")
    print(f"   Jobs: {workload_analysis['original_job_requests']} -> {workload_analysis['optimized_job_blocks']}")
    print(f"   Contention Eliminated: {workload_analysis['contention_eliminated']}")
    print(f"   Contention Reduction: {workload_analysis['contention_reduction_rate']}%")
    print(f"   Compute Hours Saved: {workload_analysis['compute_hours_saved']}")
    print(f"   GPU Efficiency Gain: {workload_analysis['gpu_efficiency_gain_percent']}%")
    print(f"   Throughput Increase: {workload_analysis['estimated_throughput_increase']}%")
    print(f"   Memory Efficiency: {workload_analysis['memory_efficiency_percent']}%")
    print(f"   Infrastructure Savings: ${workload_analysis['infrastructure_cost_savings']}")
    print(f"   Workload Optimization: {'Effective' if workload_analysis['workload_optimization_effective'] else 'Minimal Impact'}")
    
    # Edge Cases Validation
    print("\n4. Edge Cases Validation:")
    edge_cases = [
        ([], "Empty intervals"),
        ([[1,1]], "Single point"),
        ([[1,2],[3,4]], "No overlaps"),
        ([[1,10],[2,3],[4,5]], "Multiple contained")
    ]
    
    for intervals, description in edge_cases:
        result = merger.merge_intervals(intervals)
        print(f"   {description}: {intervals} -> {result}")

if __name__ == "__main__":
    run_tests()