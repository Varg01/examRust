#include "readWrite.hpp"
#include <string>
#include <chrono>

/**
 * Utility function used to print the array after
 * sorting
 */
void show(int *arr, int size) {
    for (int i = 0; i < size; i++) std::cout << arr[i] << " ";
    std::cout << "\n";
}

/** Main function */
int main(int argc, char **argv) {

    int size = std::stoi(argv[1]);
    string fileName = argv[2];

    string fileData = ""; 

    // int** firstArray = new int*[size];
    // for (int i = 0; i < size; i++) {
    //     firstArray[i] = new int[size];
    // }

    int iterations = 10;
    long long totaldurationRead = 0;
    long long totalDurationWrite = 0;
    for (int i = 0; i < iterations; i++) {
        auto startRead = chrono::high_resolution_clock::now();
        readArr(fileName, fileData);
        auto endRead = chrono::high_resolution_clock::now();

        auto durationRead = chrono::duration_cast<std::chrono::microseconds>(endRead - startRead).count();
        cout << "Execution time: " << durationRead << " microseconds" << endl;
        cout << "Execution time: " << durationRead/1000000 << " seconds" << endl;

        totaldurationRead += durationRead;

        auto startWrite = std::chrono::high_resolution_clock::now();
        writeResult(fileData, size);
        auto endWrite = chrono::high_resolution_clock::now();
        auto durationWrite = chrono::duration_cast<chrono::microseconds>(endWrite - startWrite).count();
        cout << "Execution time: " << durationWrite << " microseconds" << endl;
        cout << "Execution time: " << durationWrite/1000000 << " seconds" << endl;
        totalDurationWrite += durationWrite;
    }

    std::cout << "Average Execution time: " << totaldurationRead / iterations << " microseconds" << std::endl;
    std::cout << "Average Execution time seconds: " << totaldurationRead / (iterations * 1000000) << " seconds" << std::endl;

    std::cout << "Average Execution time: " << totalDurationWrite / iterations << " microseconds" << std::endl;
    std::cout << "Average Execution time seconds: " << totalDurationWrite / (iterations * 1000000) << " seconds" << std::endl;

    
    

    // for (int i = 0; i < size; i++) {
    //     delete[] firstArray[i];
    // }
    // delete[] firstArray;


    return 0;
}
/** @} */
