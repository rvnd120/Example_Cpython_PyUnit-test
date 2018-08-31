# Declaration of variables
CC = gcc
CC_FLAGS = -shared -fPIC -I/usr/include/python2.7 -Wall -Wextra -Wno-unused-parameter -O2 -g

# Main target:
all: fibonacci.so

# Object files:
%.so: %.c
	$(CC) $(CC_FLAGS) $< -o $@

# Remove *ALL* build artifacts:
clean:
	rm -f *.so

.PHONY: all run clean
