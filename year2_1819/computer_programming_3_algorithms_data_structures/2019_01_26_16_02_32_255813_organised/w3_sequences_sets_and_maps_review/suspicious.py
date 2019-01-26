
import sys
students = sys.argv[1]
delinquents = sys.argv[2]
with open(students, 'r') as stud_f, open(delinquents, 'r') as dlinq_f:
	stud_set = set([s.strip() for s in stud_f])
	dlinq_set = set([d.strip() for d in dlinq_f])
	suspicious = sorted(list(stud_set & dlinq_set))

	for student in enumerate(suspicious):
		num, name = student
		print('{}. {}'.format(num+1,name))