#ifndef MATRIXMULTIPLICATION_HPP
#define MATRIXMULTIPLICATION_HPP

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>


using namespace std;


void matrixMultiplication(int **firstMatrix, int **secondMatrix, long **resultMatrix, int matrixSize);

void readArr(string fileName, int **arr);

void writeResult(long ** resultArr, int size);

#endif // matrixMultiplication