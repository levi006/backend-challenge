#NoRedInk Coding Challenge - Backend 

question_file = "./readme/questions.csv"

strands = {}
standards = {}
questions = {} 

for line in open(question_file):
	file_info = line.rstrip().split(",")
	strand_id, strand_name = file_info[0], file_info[1]
	strands[strand_id] = strand_name

	# standard_info = line.rstrip().split(",")
	standard_id, standard_name = file_info[2], file_info[3]
	standards[standard_id] = standard_name

	# question_info = line.rstrip().split(",")
	question_id, question_difficulty = file_info[4], file_info[5]
	questions[question_id] = question_difficulty	

print strands
print standards
print questions
	


# num_questions = float(raw_input("How many questions would you like to put in the quiz?"))

# if num_questions <= 0 or num_questions % 1 != 0:
# 	print "Sorry, please enter an integer greater than zero."




