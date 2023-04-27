#include "matrixMultiplication.hpp"



void readArr(string fileName, int *arr)
{
    std::ifstream file(fileName);

    int count = 0;

    if (file.is_open()) {
        std::string line;
        while (getline(file, line)) {
            std::stringstream ss(line);
            int num;
            while (ss >> num) {
                arr[count] = num;
                count++;
                if (ss.peek() == ',') {
                    ss.ignore();
                }
            }
        }
        file.close();
    } else {
        std::cout << "Unable to open file.\n";
    }
}

void matrixMultiplication(int *firstMatrix, int *secondMatrix, long *resultMatrix, int matrixSize)
{
    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < matrixSize; j++) {
            long sum = 0;
            for (int k = 0; k < matrixSize; k++) {
                sum += firstMatrix[i * matrixSize + k] * secondMatrix[k * matrixSize + j];
            }
            resultMatrix[i * matrixSize + j] = sum;
        }
    }
}


void writeResult(long *resultArray, int size){
    std::ofstream outFile("result.txt");

    if (outFile.is_open()) {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                outFile << resultArray[i * size + j];
                if (j < size - 1) {
                    outFile << ",";
                }
            }
            outFile << "\n";
        }
        outFile.close();
    } else {
        std::cout << "Unable to open file.\n";
    }
}

