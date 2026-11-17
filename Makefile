CC = cc
CFLAGS = -O2 -Wall -Wextra

.PHONY: all clean
all: build/tiny

build/tiny: dos/TINY.C Makefile
	mkdir -p build
	$(CC) $(CPPFLAGS) $(CFLAGS) -x c dos/TINY.C $(LDFLAGS) -lm -o $@

clean:
	rm -rf build
