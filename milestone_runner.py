#!/usr/bin/env python3
"""
Milestone Runner - Executes all tasks for the milestone
"""

from task1_small_task import small_task
from task2_another_task import another_task

def run_milestone():
    """Run all tasks in the milestone."""
    print("=" * 50)
    print("🏁 MILESTONE EXECUTION STARTED")
    print("=" * 50)
    
    try:
        # Execute the milestone workflow
        final_result = another_task()
        
        print("\n" + "=" * 50)
        print("🎊 MILESTONE COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        print(f"Tasks completed: {len(final_result['completed_tasks'])}")
        for i, task in enumerate(final_result['completed_tasks'], 1):
            print(f"  {i}. {task}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Milestone failed with error: {e}")
        return False

if __name__ == "__main__":
    success = run_milestone()
    exit(0 if success else 1)