#include "matrixMultiplication.hpp"



void readArr(string fileName, int **arr)
{
    std::ifstream file(fileName);

    int count;
    int lineCount = 0;

    if (file.is_open()) {
        std::string line;
        while (getline(file, line)) {
            std::stringstream ss(line);
            int num;
            count = 0;
            while (ss >> num) {
                arr[lineCount][count] = num;
                count++;
                if (ss.peek() == ',') {
                    ss.ignore();
                }
            }
            lineCount++;
        }
        file.close();
    } else {
        std::cout << "Unable to open file.\n";
    }


}

void matrixMultiplication(int **firstMatrix, int **secondMatrix, long **resultMatrix, int matrixSize)
{
    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < matrixSize; j++) {
            resultMatrix[i][j] = 0;
            for (int k = 0; k < matrixSize; k++) {
                resultMatrix[i][j] += firstMatrix[i][k] * secondMatrix[k][j];
            }
        }
    }
}


void writeResult(long **resultArray, int size){
    std::ofstream outFile("result.txt");

    if (outFile.is_open()) {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                outFile << resultArray[i][j];
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