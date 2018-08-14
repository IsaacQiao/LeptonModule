
TARGET = raspberrypi_capture
LIBS = -lm -L/usr/lib/python3.5/config-3.5m-arm-linux-gnueabihf -lpython3.5
CC = gcc
CFLAGS = -g -Wall -I/usr/include/python3.5

.PHONY: default all clean

default: $(TARGET)
all: default

OBJECTS = $(patsubst %.c, %.o, $(wildcard *.c))
HEADERS = $(wildcard *.h)

%.o: %.c $(HEADERS)
	$(CC) $(CFLAGS) -c $< -o $@

.PRECIOUS: $(TARGET) $(OBJECTS)

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -Wall $(LIBS) -o $@

clean:
	-rm -f *.o
	-rm -f $(TARGET)

