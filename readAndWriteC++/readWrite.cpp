#include "matrixMultiplication.hpp"



void readArr(string fileName, string& fileData)
{
    std::ifstream file(fileName);

    if (file.is_open()) {
        fileData.assign(std::istreambuf_iterator<char>(file), std::istreambuf_iterator<char>());
        file.close();
    } else {
        std::cout << "Unable to open file.\n";
    }
}

void writeResult(string fileName, const string& fileData)
{
    std::ofstream outFile(fileName);

    if (outFile.is_open()) {
        outFile << fileData;
        outFile.close();
    } else {
        std::cout << "Unable to open file.\n";
    }
}
