BINARY=307multigrains


make:
	@cp src/*.py .
	@mv multigrains.py $(BINARY)
	@chmod +x $(BINARY)


clean:
	@rm -f $(BINARY)
	@rm -f *.py


fclean: clean
	@rm -rf __pycache__


re: fclean make


# TIP: run as following to see log output in stdout:
# DEBUG=TRUE make test
test: re
	./$(BINARY) 10 100 10 0 200 200 200 200 200
	./$(BINARY) 45 41 21 63 198 259 257 231 312

	./$(BINARY) -h # help
	./$(BINARY) ; echo "$$?" # no arguments
	./$(BINARY) 10 32 2 3 3 2 1 3 ; echo "$$?" # too few arguments
	./$(BINARY) 10 32 2 3 3 2 1 3 5 10 ; echo "$$?" # too many arguments
	./$(BINARY) -b ; echo "$$?" # incorrect "flag" argument

	./$(BINARY) 10 32 2 3 3 2 1 3 hi ; echo "$$?" # incorrect argument type - str
	./$(BINARY) 10 10.5 2 3 3 2 1 4 4 ; echo "$$?" # incorrect argument type - float
	./$(BINARY) 10 10 2 -3 3 2 1 4 4 ; echo "$$?" # negative tons amount
	./$(BINARY) 10 10 2 0 3 2 1 4 -5 ; echo "$$?" # negative price

	./$(BINARY) 0 0 0 0 0 0 0 0 0 # all zeroes
	./$(BINARY) 1000 4330 3240 3230 1000 5000 3000 6000 6666 # big numbers
	# TODO: small example solveable by hand
