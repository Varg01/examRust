#include "mergeSort.hpp"
#include <string>

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
    std::string fileName = argv[2];


    std::ifstream file(fileName);
    int *arr = new int[size];
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

    mergeSort(arr, 0, size - 1);
    std::cout << "Sorted array : ";
    show(arr, size);
    delete[] arr;
    return 0;
}
/** @} */
