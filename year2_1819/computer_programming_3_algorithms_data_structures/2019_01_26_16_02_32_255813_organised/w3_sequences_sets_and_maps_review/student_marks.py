
def make_map():
	student_marks = {}
	name_mark = input()
	while 0 < len(name_mark):
		student_marks[name_mark.split()[0]] = name_mark.split()[1]
		name_mark = input()
	return student_marks