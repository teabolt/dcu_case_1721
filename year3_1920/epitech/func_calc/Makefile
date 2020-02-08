EXECUTABLE_PATH=$(shell stack path --local-install-root)
EXECUTABLE_NAME=funEvalExpr


make:
	@stack install
	@cp $(EXECUTABLE_PATH)/bin/$(EXECUTABLE_NAME) .


clean:
	@rm -f $(EXECUTABLE_NAME)
	@stack clean


fclean: clean
	@stack purge


re: fclean make


run: make
	# execute as "make run ARGS=args_for_executable"
	@$(EXECUTABLE_NAME) $(ARGS)


test:
	@stack test
