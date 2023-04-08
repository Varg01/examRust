#include "mergeSort.hpp"
#include <string>
#include <chrono>

/**
 * Utility function used to print the array after
 * sorting
 */
void show(int *arr, int size) {
    for (int i = 0; i < size; i++) cout << arr[i] << " ";
    cout << "\n";
}



/** Main function */
int main(int argc, char **argv) {

    if (argc != 3) {
        cout << "Usage: " << argv[0] << " <size> <filename>" << std::endl;
        return 1;
    }

    // Extract command-line arguments
    int size = 0;
    try {
        size = stoi(argv[1]);
    } catch (const std::invalid_argument& e) {
        cout << "Error: Invalid size argument. Please provide an integer." << std::endl;
        return 1;
    }
    string fileName = argv[2];

    ifstream file(fileName);
    int *arr = new int[size];
    int count = 0;

    int iterations = 10;
    long long totalDuration = 0;
    for (int i = 0; i < iterations; i++) {
        count = 0;
        file.open(fileName);
        if (file.is_open()) {
            string line;
            while (getline(file, line)) {
                stringstream ss(line);
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
            cout << "Unable to open file.\n";
        }

        auto start = chrono::high_resolution_clock::now();
        mergeSort(arr, 0, size - 1);
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<std::chrono::microseconds>(end - start).count();
        totalDuration += duration;

    }

    std::cout << "Average Execution time: " << totalDuration / iterations << " microseconds" << std::endl;
    std::cout << "Average Execution time: " << totalDuration / (iterations * 1000000) << " seconds" << std::endl;


    // cout << "Sorted array : ";
    // show(arr, size);
    delete[] arr;
    return 0;
}
/** @} */
