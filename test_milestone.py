#!/usr/bin/env python3
"""
Tests for the milestone tasks
"""

import unittest
from task1_small_task import small_task
from task2_another_task import another_task
from milestone_runner import run_milestone

class TestMilestoneTasks(unittest.TestCase):
    
    def test_small_task(self):
        """Test that the small task returns the correct result."""
        result = small_task()
        self.assertEqual(result, 15, "Small task should return sum of [1,2,3,4,5] = 15")
    
    def test_another_task(self):
        """Test that another task builds upon the small task correctly."""
        result = another_task()
        
        # Verify the structure
        self.assertIn('task1_result', result)
        self.assertIn('task2_result', result)
        self.assertIn('completed_tasks', result)
        
        # Verify the values
        self.assertEqual(result['task1_result'], 15)
        self.assertEqual(result['task2_result'], 30)
        self.assertEqual(len(result['completed_tasks']), 2)
        
        # Verify task names
        self.assertIn('Small Task Inside The Milestone', result['completed_tasks'])
        self.assertIn('Another Task For That Milestone', result['completed_tasks'])
    
    def test_milestone_runner(self):
        """Test that the milestone runner executes successfully."""
        success = run_milestone()
        self.assertTrue(success, "Milestone should complete successfully")

if __name__ == '__main__':
    print("Running tests for milestone tasks...")
    unittest.main(verbosity=2)