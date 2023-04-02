#ifndef READWRITE_HPP
#define READWRITE_HPP

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>


using namespace std;



void readArr(string fileName, string &fileData);

void writeResult(string &fileData, int size);

#endif // matrixMultiplication