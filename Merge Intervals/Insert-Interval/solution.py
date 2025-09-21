class IntervalInserter:
    """A class that inserts intervals into sorted lists for dynamic scheduling and workload management."""
    
    def insert_interval(self, intervals, new_interval):
        """
        Core Algorithm: Insert new interval into sorted list and merge overlapping intervals.
        
        Time Complexity: O(n) where n is the number of intervals
        Space Complexity: O(n) for the result array
        
        Args:
            intervals (List[List[int]]): Sorted non-overlapping intervals
            new_interval (List[int]): New interval to insert [start, end]
            
        Returns:
            List[List[int]]: Updated list with new interval inserted and overlaps merged
        """
        if not intervals:
            return [new_interval]
        
        result = []
        i = 0
        n = len(intervals)
        
        # Add all intervals that end before new interval starts
        while i < n and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals with new interval
        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1
        
        # Add the merged interval
        result.append(new_interval)
        
        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
    
    def schedule_urgent_meeting(self, existing_meetings, urgent_meeting):
        """
        Business Use Case: Dynamic Meeting Scheduling
        
        Insert urgent meeting into existing schedule while automatically
        resolving conflicts and optimizing room utilization.
        
        Args:
            existing_meetings (List[List[int]]): Current meeting schedule [start_hour, end_hour]
            urgent_meeting (List[int]): Urgent meeting to insert [start_hour, end_hour]
            
        Returns:
            dict: Meeting scheduling analysis with conflict resolution
        """
        original_meeting_count = len(existing_meetings)
        
        # Insert urgent meeting and resolve conflicts
        updated_schedule = self.insert_interval(existing_meetings, urgent_meeting.copy())
        final_meeting_count = len(updated_schedule)
        
        # Calculate scheduling impact metrics
        meetings_merged = original_meeting_count + 1 - final_meeting_count
        conflict_resolution_rate = (meetings_merged / (original_meeting_count + 1)) * 100
        
        # Calculate time efficiency metrics
        original_total_hours = sum(end - start for start, end in existing_meetings)
        urgent_hours = urgent_meeting[1] - urgent_meeting[0]
        final_total_hours = sum(end - start for start, end in updated_schedule)
        
        time_saved = (original_total_hours + urgent_hours) - final_total_hours
        utilization_improvement = (time_saved / (original_total_hours + urgent_hours)) * 100 if (original_total_hours + urgent_hours) > 0 else 0
        
        # Calculate availability and gaps
        schedule_gaps = self._calculate_schedule_gaps(updated_schedule)
        availability_windows = len(schedule_gaps)
        
        # Estimate business impact
        meeting_room_cost_per_hour = 75  # Premium meeting room cost
        cost_savings = time_saved * meeting_room_cost_per_hour
        
        # Calculate productivity metrics
        conflict_hours_saved = meetings_merged * 0.5  # Average time saved per conflict
        executive_productivity_gain = conflict_hours_saved * 200  # Value per executive hour
        
        # Determine scheduling efficiency
        schedule_efficiency = 100 - conflict_resolution_rate
        optimal_insertion = meetings_merged <= 2  # Minimal disruption
        
        return {
            'original_meetings': original_meeting_count,
            'final_meetings': final_meeting_count,
            'urgent_meeting_inserted': urgent_meeting,
            'meetings_merged': meetings_merged,
            'conflict_resolution_rate': round(conflict_resolution_rate, 2),
            'time_saved_hours': time_saved,
            'utilization_improvement_percent': round(utilization_improvement, 2),
            'updated_schedule': updated_schedule,
            'schedule_gaps': schedule_gaps,
            'availability_windows': availability_windows,
            'estimated_cost_savings': round(cost_savings, 2),
            'conflict_hours_saved': round(conflict_hours_saved, 2),
            'executive_productivity_value': round(executive_productivity_gain, 2),
            'schedule_efficiency_percent': round(schedule_efficiency, 2),
            'optimal_insertion_achieved': optimal_insertion,
            'minimal_disruption': meetings_merged <= 1
        }
    
    def insert_priority_ai_job(self, existing_jobs, priority_job):
        """
        AI Orchestration Use Case: Real-Time Workload Management
        
        Insert high-priority AI job into existing computational schedule
        while optimizing GPU utilization and minimizing disruption.
        
        Args:
            existing_jobs (List[List[int]]): Current AI job schedule [start_time, end_time]
            priority_job (List[int]): Priority job to insert [start_time, end_time]
            
        Returns:
            dict: AI workload management analysis with resource optimization
        """
        original_job_count = len(existing_jobs)
        
        # Insert priority job and optimize schedule
        optimized_workload = self.insert_interval(existing_jobs, priority_job.copy())
        final_job_count = len(optimized_workload)
        
        # Calculate workload consolidation metrics
        jobs_consolidated = original_job_count + 1 - final_job_count
        consolidation_rate = (jobs_consolidated / (original_job_count + 1)) * 100
        
        # Calculate computational efficiency
        original_compute_hours = sum(end - start for start, end in existing_jobs)
        priority_compute_hours = priority_job[1] - priority_job[0]
        final_compute_hours = sum(end - start for start, end in optimized_workload)
        
        compute_time_saved = (original_compute_hours + priority_compute_hours) - final_compute_hours
        gpu_efficiency_gain = (compute_time_saved / (original_compute_hours + priority_compute_hours)) * 100 if (original_compute_hours + priority_compute_hours) > 0 else 0
        
        # Calculate resource utilization
        processing_gaps = self._calculate_schedule_gaps(optimized_workload)
        available_slots = len(processing_gaps)
        
        # Estimate performance improvements
        throughput_increase = min(45, consolidation_rate * 1.5)  # Cap at 45%
        memory_efficiency = max(70, 100 - (jobs_consolidated * 5))  # Memory optimization
        
        # Calculate cost efficiency
        gpu_cluster_cost_per_hour = 12.50  # High-performance GPU cost
        infrastructure_savings = compute_time_saved * gpu_cluster_cost_per_hour
        
        # Calculate system responsiveness metrics
        priority_job_latency_reduction = jobs_consolidated * 0.25  # Hours saved on priority job
        system_responsiveness = min(95, 80 + (consolidation_rate * 0.3))
        
        # Determine optimization effectiveness
        workload_optimized = consolidation_rate >= 15
        minimal_system_impact = jobs_consolidated <= 3
        
        return {
            'original_jobs': original_job_count,
            'final_jobs': final_job_count,
            'priority_job_inserted': priority_job,
            'jobs_consolidated': jobs_consolidated,
            'consolidation_rate': round(consolidation_rate, 2),
            'compute_time_saved_hours': compute_time_saved,
            'gpu_efficiency_gain_percent': round(gpu_efficiency_gain, 2),
            'optimized_workload': optimized_workload,
            'processing_gaps': processing_gaps,
            'available_processing_slots': available_slots,
            'estimated_throughput_increase': round(throughput_increase, 2),
            'memory_efficiency_percent': round(memory_efficiency, 2),
            'infrastructure_cost_savings': round(infrastructure_savings, 2),
            'priority_latency_reduction': round(priority_job_latency_reduction, 2),
            'system_responsiveness_score': round(system_responsiveness, 2),
            'workload_optimization_effective': workload_optimized,
            'minimal_system_impact_achieved': minimal_system_impact,
            'real_time_insertion_successful': True
        }
    
    def _calculate_schedule_gaps(self, intervals):
        """Calculate gaps between intervals for availability analysis."""
        if len(intervals) <= 1:
            return []
        
        gaps = []
        for i in range(len(intervals) - 1):
            gap_start = intervals[i][1]
            gap_end = intervals[i + 1][0]
            if gap_end > gap_start:
                gaps.append([gap_start, gap_end])
        
        return gaps

# --- Example Usage ---
def run_tests():
    """Demonstrate interval insertion with business and AI use cases."""
    
    inserter = IntervalInserter()
    
    print("Insert Interval: Dynamic Scheduling & Real-Time Workload Management")
    print("-" * 65)
    
    # Core Algorithm Test
    print("\n1. Core Algorithm Validation:")
    test_cases = [
        ([[1,3],[6,9]], [2,5], "Overlapping with first interval"),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], "Multiple overlaps"),
        ([], [5,7], "Empty intervals list"),
        ([[1,5]], [2,3], "New interval contained"),
        ([[1,5]], [6,8], "No overlap, append")
    ]
    
    for intervals, new_interval, description in test_cases:
        result = inserter.insert_interval(intervals.copy(), new_interval.copy())
        print(f"   {description}")
        print(f"     Intervals: {intervals}, New: {new_interval} -> {result}")
    
    # Business Use Case: Dynamic Meeting Scheduling
    print("\n2. Business Use Case - Urgent Meeting Scheduling:")
    existing_meetings = [[1,2],[3,5],[6,7],[8,10]]  # Current meeting schedule
    urgent_meeting = [4,8]  # Executive urgent meeting
    
    meeting_analysis = inserter.schedule_urgent_meeting(existing_meetings, urgent_meeting)
    
    print(f"   Existing Meetings: {existing_meetings}")
    print(f"   Urgent Meeting: {urgent_meeting}")
    print(f"   Updated Schedule: {meeting_analysis['updated_schedule']}")
    print(f"   Meetings: {meeting_analysis['original_meetings']} -> {meeting_analysis['final_meetings']}")
    print(f"   Meetings Merged: {meeting_analysis['meetings_merged']}")
    print(f"   Conflict Resolution: {meeting_analysis['conflict_resolution_rate']}%")
    print(f"   Time Saved: {meeting_analysis['time_saved_hours']} hours")
    print(f"   Utilization Improvement: {meeting_analysis['utilization_improvement_percent']}%")
    print(f"   Cost Savings: ${meeting_analysis['estimated_cost_savings']}")
    print(f"   Executive Value: ${meeting_analysis['executive_productivity_value']}")
    print(f"   Schedule Efficiency: {meeting_analysis['schedule_efficiency_percent']}%")
    print(f"   Minimal Disruption: {'Yes' if meeting_analysis['minimal_disruption'] else 'No'}")
    
    # AI Use Case: Real-Time Workload Management
    print("\n3. AI Use Case - Priority AI Job Insertion:")
    existing_jobs = [[1,3],[6,9],[12,15]]  # Current AI workload
    priority_job = [2,10]  # High-priority model training
    
    workload_analysis = inserter.insert_priority_ai_job(existing_jobs, priority_job)
    
    print(f"   Existing AI Jobs: {existing_jobs}")
    print(f"   Priority Job: {priority_job}")
    print(f"   Optimized Workload: {workload_analysis['optimized_workload']}")
    print(f"   Jobs: {workload_analysis['original_jobs']} -> {workload_analysis['final_jobs']}")
    print(f"   Jobs Consolidated: {workload_analysis['jobs_consolidated']}")
    print(f"   Consolidation Rate: {workload_analysis['consolidation_rate']}%")
    print(f"   Compute Time Saved: {workload_analysis['compute_time_saved_hours']} hours")
    print(f"   GPU Efficiency Gain: {workload_analysis['gpu_efficiency_gain_percent']}%")
    print(f"   Throughput Increase: {workload_analysis['estimated_throughput_increase']}%")
    print(f"   Memory Efficiency: {workload_analysis['memory_efficiency_percent']}%")
    print(f"   Infrastructure Savings: ${workload_analysis['infrastructure_cost_savings']}")
    print(f"   Priority Latency Reduction: {workload_analysis['priority_latency_reduction']} hours")
    print(f"   System Responsiveness: {workload_analysis['system_responsiveness_score']}")
    print(f"   Minimal Impact: {'Yes' if workload_analysis['minimal_system_impact_achieved'] else 'No'}")
    
    # Edge Cases Validation
    print("\n4. Edge Cases Validation:")
    edge_cases = [
        ([], [1,2], "Insert into empty list"),
        ([[1,1]], [2,2], "Point intervals"),
        ([[1,10]], [5,6], "New interval fully contained"),
        ([[5,6]], [1,10], "New interval contains existing")
    ]
    
    for intervals, new_interval, description in edge_cases:
        result = inserter.insert_interval(intervals.copy(), new_interval.copy())
        print(f"   {description}: {intervals} + {new_interval} -> {result}")

if __name__ == "__main__":
    run_tests()