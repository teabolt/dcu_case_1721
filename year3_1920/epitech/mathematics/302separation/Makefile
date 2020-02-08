JCC = javac
JFLAGS = -d .


make:
	@$(JCC) $(JFLAGS) src/*.java
	@touch 302separation
	@echo 'java Separation "$$@"' > 302separation
	@chmod +x 302separation


clean:
	@rm -f *.class


fclean: clean
	@rm -f 302separation


re: fclean make


test: re
# 	pass '-i' flag to continue even in case of non-zero exit status
	@echo "[MAKE] testing matrix implementation"
	java Tests

	@echo "[MAKE] testing submission program"
	./302separation -h
	./302separation tests/example 3
	./302separation tests/example "Yvette Horner" "Barack Obama"
	./302separation tests/example "Yvette Horner" "Yvette Horner"
	./302separation tests/example "Yvette Horner" "Mike Tyson"

	@echo "[MAKE] difference between output and expected"
	./302separation tests/example 3 > tests/output
	diff tests/output tests/expected

	@echo "[MAKE] testing edge cases / stress testing"
	./302separation tests/example 100
	./302separation tests/example 0
	./302separation tests/example "spiderman" "snowman"
	./302separation tests/example2 3 # empty file
	./302separation tests/example3 3 # file with whitespaces
	./302separation tests/example4 3 # well-formatted file with unnecessary whitespace
	./302separation tests/example5 3 # not well-formatted file (misspellings)
	./302separation tests/example6 3 # two people  # FIXME
	./302separation tests/example7 3 # one person

	@echo "[MAKE] testing error handling"
	./302separation
	./302separation -a
	./302separation -a bababab
	./302separation -a -b -c
	./302separation nonexistantfile 10
	./302separation tests/example -100 # throw error or ignore ???
