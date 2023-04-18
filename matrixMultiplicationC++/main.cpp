#include "matrixMultiplication.hpp"
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
    string fileName1 = argv[2];
    string fileName2 = argv[3];

    int** firstArray = new int*[size];
    for (int i = 0; i < size; i++) {
        firstArray[i] = new int[size];
    }

    int** secondArray = new int*[size];
    for (int i = 0; i < size; i++) {
        secondArray[i] = new int[size];
    }

    long** resultArray = new long*[size];
    for (int i = 0; i < size; i++) {
        resultArray[i] = new long[size];
    }

    int iterations = 10;
    long long totalDuration = 0;

    readArr(fileName1, firstArray);
    readArr(fileName2, secondArray);
    std::ofstream outputFile("timeResult_" + to_string(size));
    for (int i = 0; i < iterations; i++) {

        auto start = chrono::high_resolution_clock::now();
        matrixMultiplication(firstArray, secondArray, resultArray, size);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<std::chrono::microseconds>(end - start).count();
        totalDuration += duration;
        outputFile << "Duration for Iteration " << i + 1 << ": " << duration << " microseconds" << std::endl;
        outputFile << "Duration for Iteration " << i + 1 << ": " << duration/1000000 << " seconds" << std::endl;
    }
    outputFile << "Average Execution time: " << totalDuration / iterations << " microseconds" << std::endl;
    outputFile << "Average Execution time: " << totalDuration / (iterations * 1000000) << " seconds" << std::endl;


    writeResult(resultArray, size);

    for (int i = 0; i < size; i++) {
        delete[] firstArray[i];
    }
    delete[] firstArray;

    for (int i = 0; i < size; i++) {
        delete[] secondArray[i];
    }
    delete[] secondArray;

    for (int i = 0; i < size; i++) {
        delete[] resultArray[i];
    }
    delete[] resultArray;

    return 0;
}
/** @} */
