#!/bin/bash

matrixMultipicationCpp="matrixMultiplicationC++/matrixMultiplication_cpp"
matrixMultipicationRust="matrix_multiplication_rust/target/release/matrix_multiplication"
mergeSortCpp="mergeSortC++/mergeSort_c++"
mergeSortRust="merge_sort_rust/target/release/merge_sort_rust"
readAndWriteCpp="readAndWriteC++/readWrite_cpp"
readAndWriteRust="read_write_rust/target/release/read_write_rust"

iterations="100"

$matrixMultipicationCpp "250" "data/matrixMultData/firstMatrix250.txt" "data/matrixMultData/secondMatrix250.txt" $iterations "resultFiles/c++Matrix/timeResult_"
$matrixMultipicationCpp "500" "data/matrixMultData/firstMatrix500.txt" "data/matrixMultData/secondMatrix500.txt" $iterations "resultFiles/c++Matrix/timeResult_"
$matrixMultipicationCpp "1000" "data/matrixMultData/firstMatrix1000.txt" "data/matrixMultData/secondMatrix1000.txt" $iterations "resultFiles/c++Matrix/timeResult_"
$matrixMultipicationCpp "2000" "data/matrixMultData/firstMatrix2000.txt" "data/matrixMultData/secondMatrix2000.txt" $iterations "resultFiles/c++Matrix/timeResult_"

$matrixMultipicationRust "250" "data/matrixMultData/firstMatrix250.txt" "data/matrixMultData/secondMatrix250.txt" $iterations "resultFiles/rustMatrix/timeResult_"
$matrixMultipicationRust "500" "data/matrixMultData/firstMatrix500.txt" "data/matrixMultData/secondMatrix500.txt" $iterations "resultFiles/rustMatrix/timeResult_"
$matrixMultipicationRust "1000" "data/matrixMultData/firstMatrix1000.txt" "data/matrixMultData/secondMatrix1000.txt" $iterations "resultFiles/rustMatrix/timeResult_"
$matrixMultipicationRust "2000" "data/matrixMultData/firstMatrix2000.txt" "data/matrixMultData/secondMatrix2000.txt" $iterations "resultFiles/rustMatrix/timeResult_"

# $mergeSortCpp "100000" "data/sortData/sort10⁵.txt" $iterations "resultFiles/c++Sort/timeResult_"
# $mergeSortCpp "1000000" "data/sortData/sort10⁶.txt" $iterations "resultFiles/c++Sort/timeResult_"
# $mergeSortCpp "10000000" "data/sortData/sort10⁷.txt" $iterations "resultFiles/c++Sort/timeResult_"
# $mergeSortCpp "100000000" "data/sortData/sort10⁸.txt" $iterations "resultFiles/c++Sort/timeResult_"

# $mergeSortRust "100000" "data/sortData/sort10⁵.txt" $iterations "resultFiles/rustSort/timeResult_"
# $mergeSortRust "1000000" "data/sortData/sort10⁶.txt" $iterations "resultFiles/rustSort/timeResult_"
# $mergeSortRust "10000000" "data/sortData/sort10⁷.txt" $iterations "resultFiles/rustSort/timeResult_"
# $mergeSortRust "100000000" "data/sortData/sort10⁸.txt" $iterations "resultFiles/rustSort/timeResult_"

# $readAndWriteCpp "10000" "data/readWriteData/readWrite10⁴.txt" $iterations "resultFiles/c++ReadWrite/timeResult_"
# rm "result.txt"
# $readAndWriteCpp "1000000" "data/readWriteData/readWrite10⁶.txt" $iterations "resultFiles/c++ReadWrite/timeResult_"
# rm "result.txt"
# $readAndWriteCpp "100000000" "data/readWriteData/readWrite10⁸.txt" $iterations "resultFiles/c++ReadWrite/timeResult_"
# rm "result.txt"
# $readAndWriteCpp "1000000000" "data/readWriteData/readWrite10⁹.txt" $iterations "resultFiles/c++ReadWrite/timeResult_"
# rm "result.txt"

# $readAndWriteRust "10000" "data/readWriteData/readWrite10⁴.txt" $iterations "resultFiles/rustReadWrite/timeResult_"
# rm "result.txt"
# $readAndWriteRust "1000000" "data/readWriteData/readWrite10⁶.txt" $iterations "resultFiles/rustReadWrite/timeResult_"
# rm "result.txt"
# $readAndWriteRust "100000000" "data/readWriteData/readWrite10⁸.txt" $iterations "resultFiles/rustReadWrite/timeResult_"
# rm "result.txt"
# $readAndWriteRust "1000000000" "data/readWriteData/readWrite10⁹.txt" $iterations "resultFiles/rustReadWrite/timeResult_"
# rm "result.txt"

