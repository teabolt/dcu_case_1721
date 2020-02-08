make:
	@cp src/hex_to_base64.py hex_to_base64.py
	@cp src/byte_xor_encryption.py byte_xor_encryption.py
	@cp src/repeating_xor_encryption.py repeating_xor_encryption.py
	@cp src/aes_encryption.py aes_encryption.py
	@cp src/utils.py utils.py


	@cp src/source01.py challenge01
	@chmod +x challenge01

	@cp src/source02.py challenge02
	@chmod +x challenge02

	@cp src/source03.py challenge03
	@chmod +x challenge03

	@cp src/source04.py challenge04
	@chmod +x challenge04

	@cp src/source05.py challenge05
	@chmod +x challenge05

	@cp src/source06.py challenge06
	@chmod +x challenge06

	@cp src/source07.py challenge07
	@chmod +x challenge07

	@cp src/source08.py challenge08
	@chmod +x challenge08

	@cp src/source09.py challenge09
	@chmod +x challenge09

	@cp src/source10.py challenge10
	@chmod +x challenge10

	@cp src/source11.py challenge11
	@chmod +x challenge11

	@cp src/source12.py challenge12
	@chmod +x challenge12

	@cp src/source13.py challenge13
	@chmod +x challenge13

	@cp src/source14.py challenge14
	@chmod +x challenge14

	@# TODO: use a loop/matching instead of repeating this


re: fclean make


clean:
	@rm -f challenge*
	@rm -f *.py
	@rm -rf __pycache__/


fclean: clean


test: make
	@# To ignore errors: make test -i
	./challenge01 input/input01.txt
	./challenge02 input/input02.txt
	./challenge03 input/input03.txt
	./challenge04 input/input04.txt
	./challenge05 input/input05.txt
	./challenge06 input/input06.txt
	./challenge07 input/input07.txt
	./challenge08 input/input08.txt
	./challenge09 input/input09.txt
	./challenge10 input/input10.txt
	./challenge11 input/input11.txt
	./challenge12 input/input12.txt
	./challenge13 input/input13.txt
	./challenge14 input/input14.txt