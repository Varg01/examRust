#include "readWrite.hpp"



void readArr(const std::string& fileName, std::string& fileData)
{
    std::ifstream file(fileName, std::ios::binary);

    if (file) {
        file.seekg(0, std::ios::end);
        fileData.resize(file.tellg());
        file.seekg(0, std::ios::beg);
        file.read(&fileData[0], fileData.size());
        file.close();
    } else {
        std::cout << "Unable to open file.\n";
    }
}

void writeResult(const std::string& fileData)
{
    std::ofstream outFile("result.txt", std::ios::binary);

    if (outFile) {
        outFile.write(fileData.data(), fileData.size());
        outFile.close();
    } else {
        std::cout << "Unable to open file.\n";
    }
}
