'''
Created on 26 Jan 2017

@author: cian
'''
import unittest
from read_input import *
import argparse

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
		
	def test_source_file_exists(self):
        self.assertEqual('foo'.upper(), 'FOO')

'''
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
'''

if __name__ == "__main__":
	unittest.test_source_file_exists()
	input = raw_input("Enter your input file? ")
	print "Input file is: %s." % input
	if os.path.exists(input):
		print "input file exists"
		students = read_input_file(input)
		sorted = sort_students(students)
		generate_output_file(sorted)
		exit = raw_input("This program will now exit... press any key to exit")
	elif not os.path.exists(input):
		print "input file not in specified diretory ... please check ... exiting program now"
		exit = raw_input("This program will now exit... press any key to exit")
		sys.exit()
