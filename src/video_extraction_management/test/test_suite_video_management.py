"""
Project: Fruit Size Estimation
Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: February 2022
Description:
    Suit to test all classes video management, don't forget to add new tests HERE!

Use:
    python -m unittest video_extraction_management/test/test_suite_video_management.py
"""

import unittest
from src.video_extraction_management.test.test_frame_extraction_config import TestFramesManagerConfig
from src.video_extraction_management.test.test_frame_extraction import TestFramesManager

def video_management_suite():
    """
        Gather all the tests to process data from detected objects in all levels
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestFramesManagerConfig))
    test_suite.addTest(unittest.makeSuite(TestFramesManager))

    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(video_management_suite())