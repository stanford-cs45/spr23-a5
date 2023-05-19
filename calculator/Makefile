calculator: main.o addition.o subtraction.o division.o multiplication.o
	cc -o calculator main.o addition.o subtraction.o division.o multiplication.o

addition.o: addition.c operations.h
	cc -c addition.c

subtraction.o: subtraction.c operations.h
	cc -c subtraction.c

division.o: division.c operations.h
	cc -c division.c

multiplication.o: multiplication.c operations.h
	cc -c multiplication.c

main.o: main.c operations.h
	cc -c main.c

clean:
	rm *.o calculator
