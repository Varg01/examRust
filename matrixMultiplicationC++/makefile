CXX = g++
CXXFLAGS = -O3

SRCS = main.cpp matrixMultiplication.cpp
OBJS = $(SRCS:.c++=.o)
EXEC = matrixMultiplication_cpp

$(EXEC): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(EXEC)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(EXEC)
