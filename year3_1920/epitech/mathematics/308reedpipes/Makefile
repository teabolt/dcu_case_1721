BINARY=308reedpipes


make:
	@cp src/*.py .
	@mv 308reedpipes.py $(BINARY)
	@chmod +x $(BINARY)


clean:
	@rm -f $(BINARY)
	@rm -f *.py
	@rm -f *.log


fclean: clean
	@rm -rf __pycache__
	@rm -rf tests/__pycache__
	@rm -rf src/__pycache__


re: fclean make

test: re
	# given tests
	./$(BINARY) 1.5 2 2 2 5 11
	./$(BINARY) 2 3 2 4 5 13
	
	# help
	./$(BINARY) -h

	# arguments
	./$(BINARY) ; echo "$$?" # no arguments

	# argument semantics
	./$(BINARY) 1 2 3 4 5 4; echo "$$?" # not enough display points
	./$(BINARY) 1 2 3 4 5 0; echo "$$?" # zero display points
	./$(BINARY) 1 2 0 4 5 7; echo "$$?" # zero radius
