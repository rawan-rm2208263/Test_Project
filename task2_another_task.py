#!/usr/bin/env python3
"""
Task 2: Another Task For That Milestone
An additional task that complements the first task with extended functionality.
"""

def another_task():
    """Execute another task for the milestone."""
    print("🎯 Executing Task 2: Another Task For That Milestone")
    
    # Extended operations for the additional task
    from task1_small_task import small_task
    
    # Get result from the small task
    previous_result = small_task()
    
    print("\n   - Building upon Task 1 results...")
    
    # Additional processing
    multiplier = 2
    enhanced_result = previous_result * multiplier
    
    # Create a simple report
    tasks_completed = ["Small Task Inside The Milestone", "Another Task For That Milestone"]
    
    print(f"   - Enhanced result: {previous_result} × {multiplier} = {enhanced_result}")
    print(f"   - Milestone tasks completed: {len(tasks_completed)}")
    print("   - All milestone tasks executed successfully! 🎉")
    
    return {
        "task1_result": previous_result,
        "task2_result": enhanced_result,
        "completed_tasks": tasks_completed
    }

if __name__ == "__main__":
    result = another_task()
    print(f"\nFinal milestone summary: {result}")