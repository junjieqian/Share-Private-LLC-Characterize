cc = g++
DEBUG = -g
OBJS = cache.o main.o
CFLAGS = -c -Wall $(DEBUG) -I../include
LDFLAGS = -pthread

LRU_Statics:$(OBJS)
	$(CC) $(LDFLAGS) $(OBJS) -o LRU_Statics

cache.o:cache.cc
	$(CC) $(LDFLAGS) cache.cc

main.o:main.cc
	$(CC) $(LDFLAGS) main.cc

.PHONY:clean

clean:
	rm -f *.o LRU_Statics
