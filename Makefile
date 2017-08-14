
all: cfunc.so gofunc.so

cfunc.o:
	gcc -c -Wall -Werror -fpic cfunc.c

gofunc.so:
	go build -buildmode=c-shared -o gofunc.so gofunc.go

cfunc.so: cfunc.o
	gcc -shared -o cfunc.so cfunc.o 

.PHONE: clean

clean:
	rm cfunc.o cfunc.so gofunc.h gofunc.so
