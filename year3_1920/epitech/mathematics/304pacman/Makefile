pacman: 
	@cp src/304pacman.py 304pacman
	@chmod +x 304pacman


clean:
	@rm -f 304pacman


fclean: clean
	@rm -rf __pycache__
	@rm -rf src/__pycache__


re: fclean pacman


test: re
	./304pacman -h
	./304pacman input/map1 '+' ' '  # small map
	./304pacman input/map2 '@' ' '  # big map
	./304pacman input/map3 '+' ' ' ; echo "$$?"  # inconsistent line lengths
	./304pacman input/map4 '+' ' ' ; echo "$$?"  # invalid characters
	./304pacman input/map5 '@' ' ' ; echo "$$?"  # no ghost
	./304pacman input/map6 '@' ' ' ; echo "$$?"	 # multiple pacman
