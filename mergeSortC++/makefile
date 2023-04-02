CXX = g++
CXXFLAGS = -O3

SRCS = main.c++ mergeSort.c++
OBJS = $(SRCS:.c++=.o)
EXEC = mergeSort_c++

$(EXEC): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(EXEC)

%.o: %.c++
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(EXEC)
