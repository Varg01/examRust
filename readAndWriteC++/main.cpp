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


    auto start = std::chrono::high_resolution_clock::now();
    readArr(fileName, fileData);
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    std::cout << "Execution time: " << duration << " microseconds" << std::endl;
    std::cout << "Execution time: " << duration/1000000 << " seconds" << std::endl;

    auto start = std::chrono::high_resolution_clock::now();
    writeResult(fileData, size);
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    std::cout << "Execution time: " << duration << " microseconds" << std::endl;
    std::cout << "Execution time: " << duration/1000000 << " seconds" << std::endl;

    // for (int i = 0; i < size; i++) {
    //     delete[] firstArray[i];
    // }
    // delete[] firstArray;


    return 0;
}
/** @} */
