'''
Created on 26 Jan 2017

@author: cian
'''
import unittest
import os
from read_input import *

class Unittests(unittest.TestCase):

    def test_source_file_exists(self):
        self.assertEqual(os.path.exists('unittests\students.txt'), True)

    def test_output_file_exists(self):
        self.assertEqual(os.path.exists('unittests\students-graded.txt'), True)
		
    def test_generate_sample_output_file(self):
		student_dict = { 'TED': ['TED', 'BUNDY', '88'], 'ALLAN': ['ALLAN', 'SMITH', '85'], 'FRANCIS': ['FRANCIS', 'SMITH', '85'], 'MADISON': ['MADISON', 'KING', '83']}
		generate_output_file(student_dict)
		file_exist = os.path.exists('unittests\students-graded.txt')
		self.assertEqual(os.path.exists('unittests\students-graded.txt'), True)
		
    def test_read_input_file(self):
		students = read_input_file('unittests\students.txt')
		students_exist = bool(len(students)!=0)
		self.assertEqual(students_exist, True)

if __name__ == '__main__':
    unittest.main()