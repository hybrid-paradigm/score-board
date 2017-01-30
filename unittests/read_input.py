'''
Created on 26 Jan 2017

@author: cian
'''
import os
import sys

def read_input_file(input_file):
	students_dict = {}
	with open(input_file, "r") as input:
		contents = input.readlines()
		for line in contents:
			student = line.split(', ')
			name = student[0] + '_' + student[1]
			students_dict[name] = student
		input.close()
	return students_dict
	
def sort_students(student_dict):
	student_ordered = []
	for key in student_dict.keys():
#		for place in range(0, len(student_ordered)):
		if len(student_ordered) == 0:
			student_ordered.append(student_dict[key])
			ordered_num = len(student_ordered)
		for place in range(0, ordered_num):
			if (student_dict[key][2] < student_ordered[place][2]):
				print "%s scored is less than %s scored" % (key, student_ordered[place][0])
				if (student_dict[key][2] >= student_ordered[place][2]):
					print "%s scored more than %s scored" % (key, student_ordered[place][0])				
					student_ordered.insert(place+1, student_dict[key])
				if (student_dict[key][2] <= student_ordered[place][2]):
#					student_ordered.insert(0, student_dict[key])
					print "Equality %s scored more than %s scored" % (key, student_ordered[place][0])
				if (student_dict[key][2] < student_ordered[ordered_num-1][2]): 
					student_ordered.append(student_dict[key])
					print "%s scored is less than everyone scored" % (key)
#			if (student_dict[key][2] > student_ordered[0][2]):
#				if student_dict[key][1] == student_ordered[0][1]:
#					student_ordered.insert(0, student_dict[key])
#					print "Equality %s" % student_ordered
#		else:
#				student_ordered.append(student_dict[key])
		print key
		print student_ordered
	return student_ordered
	
def generate_output_file(student_dict):
	with open('students-graded.txt', 'w') as output:
		for row in student_dict:
			output.write("%s, %s, %s" % (str(row[1]), str(row[0]), str(row[2])))
			output.write("\n")
		output.close()