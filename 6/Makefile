
all:
	@gcc -W -Wall -ansi -pedantic -O2 -g -o main main.c
	@./main

check:
	valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --verbose --log-file=valgrind-out.txt ./main
