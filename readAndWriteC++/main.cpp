#include "readWrite.hpp"
#include <string>
#include <chrono>
#include <iomanip>

/**
 * Utility function used to print the array after
 * sorting
 */

/** Main function */
int main(int argc, char **argv) {

    if (argc != 5) {
        cout << "Usage: " << argv[0] << " <size> <filename> <iterations> <resultFile>" << std::endl;
        return 1;
    }

    int size = std::stoi(argv[1]);
    string fileName = argv[2];
    int iterations = std::stoi(argv[3]);
    string outputFileName = argv[4];
    

    string fileData = ""; 

    long long totaldurationRead = 0;
    long long totalDurationWrite = 0;
    std::ofstream outputFile(outputFileName + argv[1]);
    for (int i = 0; i < iterations; i++) {
        auto startRead = chrono::high_resolution_clock::now();
        readArr(fileName, fileData);
        auto endRead = chrono::high_resolution_clock::now();

        auto durationRead = chrono::duration_cast<std::chrono::microseconds>(endRead - startRead).count();
        outputFile << "Duration for Iteration read" << i + 1 << ": " << durationRead << "  microseconds" << std::endl;
        outputFile << "Duration for Iteration read" << i + 1 << ": " << durationRead/1000000 << " seconds" << std::endl;

        totaldurationRead += durationRead;

        auto startWrite = std::chrono::high_resolution_clock::now();
        writeResult(fileData);
        auto endWrite = chrono::high_resolution_clock::now();
        auto durationWrite = chrono::duration_cast<chrono::microseconds>(endWrite - startWrite).count();
        outputFile << "Duration for Iteration write" << i + 1 << ": " << durationWrite << " microseconds" << std::endl;
        outputFile << "Duration for Iteration write" << i + 1 << ": " << durationWrite/1000000.0 << " seconds" << std::endl;
        totalDurationWrite += durationWrite;
    }

    outputFile << "Average Execution time read: " << totaldurationRead / iterations << " microseconds" << std::endl;
    outputFile << "Average Execution time read: " << totaldurationRead / (iterations * 1000000.0) << " seconds" << std::endl;

    outputFile << "Average Execution time write: " << totalDurationWrite / iterations << " microseconds" << std::endl;
    outputFile << "Average Execution time write: " << totalDurationWrite / (iterations * 1000000.0) << " seconds" << std::endl;



    return 0;
}
/** @} */
