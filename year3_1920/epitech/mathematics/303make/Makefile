# Go parameters
GO=go
GOINSTALL=$(GO) install
GOBUILD=$(GO) build
GORUN=$(GO) run

# Local file paths
MAIN=./src/303make


make:
	# @$(GOINSTALL) $(MAIN)	# TODO: use go install (but don't move program to $GOPATH)
	@$(GOBUILD) $(MAIN)


run:
	@$(GORUN) $(MAIN) tests/MakefileTest


clean:
	@rm -f 303make


fclean: clean


re: fclean make


test:
	# TODO: empty file
	# TODO: make with bad targets
	# TODO: make with cycles
	# TODO: check with this makefile for index errors