make:
	@cp src/*.py .
	@mv radiator.py 306radiator
	@chmod +x 306radiator


clean:
	@rm -f 306radiator
	@rm -f *.py


fclean: clean
	@rm -rf __pycache__


re: fclean make


test: re
	./306radiator -h # help
	./306radiator 4 1 1 # matrices
	./306radiator 4 1 1 2 2 # temperature at a point
	./306radiator 5 1 2 3 2
	./306radiator 8 4 6 3 6
# 	./306radiator 12 3 9 1 6  # FIXME: big performance decrease with bigger room
# 	./306radiator 12 3 9  # see output of: python3 -m cProfile -s cumulative 306radiator 12 3 9

	./306radiator ; echo "$$?" # no arguments
	./306radiator 12 3 ; echo "$$?" # too few arguments
	./306radiator 4 2 3 3 ; echo "$$?" # too few arguments
	./306radiator 1 2 3 4 5 6 ; echo "$$?" # too many arguments

	./306radiator -b ; echo "$$?" # incorrect "flag" argument

	./306radiator 4 1 ababa ; echo "$$?" # incorrect argument type
	./306radiator 4 3 2 0 -1 ; echo "$$?" # negative coordinate value
	./306radiator 0 1 2 ; echo "$$?" # incorrect room size
	./306radiator -1 1 2 ; echo "$$?" # incorrect room size
	./306radiator 1 1 1 ; echo "$$?" # room too small
	./306radiator 2 1 1 ; echo "$$?" # room too small
	./306radiator 4 3 3 ; echo "$$?" # radiator inside walls
	./306radiator 4 2 2 3 2 ; echo "$$?" # point inside walls
	./306radiator 4 2.1 2 ; echo "$$?" # coordinate must be int

	./306radiator 3 1 1 # size 3 matrix
	./306radiator 4 1 1 # radiator and point are same coordinate
	./306radiator 4 1 1 1 1

# 	./306radiator 100 50 50 # very big room
# no gauss solution
