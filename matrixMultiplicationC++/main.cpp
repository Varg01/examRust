#include "matrixMultiplication.hpp"
#include <string>
#include <chrono>
#include <iomanip>

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

    if (argc != 6) {
        cout << "Usage: " << argv[0] << " <size> <filename1> <filename2> <iterations> <resultFile>" << std::endl;
        return 1;
    }

    int size = std::stoi(argv[1]);
    string fileName1 = argv[2];
    string fileName2 = argv[3];
    int iterations = std::stoi(argv[4]);
    string outputFileName = argv[5];

    int* firstArray = new int[size * size];
    int* secondArray = new int[size * size];
    long* resultArray = new long[size * size];

    long long totalDuration = 0;

    readArr(fileName1, firstArray);
    readArr(fileName2, secondArray);
    std::ofstream outputFile(outputFileName + to_string(size));
    for (int i = 0; i < iterations; i++) {

        auto start = chrono::high_resolution_clock::now();
        matrixMultiplication(firstArray, secondArray, resultArray, size);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<std::chrono::microseconds>(end - start).count();
        totalDuration += duration;
        outputFile << "Duration for Iteration " << i + 1 << ": " << duration << " microseconds" << std::endl;
        outputFile << "Duration for Iteration " << i + 1 << ": " << duration/1000000.0 << " seconds" << std::endl;
    }
    outputFile << "Average Execution time: " << totalDuration / iterations << " microseconds" << std::endl;
    outputFile << "Average Execution time: " << totalDuration / (iterations * 1000000.0) << " seconds" << std::endl;

    // writeResult(resultArray, size);

    delete[] firstArray;
    delete[] secondArray;
    delete[] resultArray;

    return 0;
}
/** @} */
