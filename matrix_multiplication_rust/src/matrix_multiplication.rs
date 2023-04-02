use std::fs::File;
use std::io::{BufRead, BufReader, Result, Write};

pub fn read_arr(file_name: &str, arr: &mut Vec<Vec<i64>>) -> Result<()> {
    let file = File::open(file_name)?;
    let reader = BufReader::new(file);

    for (_i, line) in reader.lines().enumerate() {
        let mut row = Vec::new();
        for num in line?.split(',') {
            row.push(num.trim().parse().unwrap());
        }
        arr.push(row);
    }
    Ok(())
}

pub fn matrix_multiplication(
    first_matrix: &Vec<Vec<i64>>,
    second_matrix: &Vec<Vec<i64>>,
    result_matrix: &mut Vec<Vec<i64>>,
    matrix_size: usize,
) {
    for i in 0..matrix_size {
        for j in 0..matrix_size {
            result_matrix[i][j] = 0;
            for k in 0..matrix_size {
                result_matrix[i][j] += first_matrix[i][k] * second_matrix[k][j];
            }
        }
    }
}

pub fn write_result(file_name: &str, result_array: &Vec<Vec<i64>>) -> Result<()> {
    let mut file = File::create(file_name)?;
    for row in result_array {
        let row_string = row
            .iter()
            .map(|num| num.to_string())
            .collect::<Vec<String>>()
            .join(",");
        file.write_all(row_string.as_bytes())?;
        file.write_all(b"\n")?;
    }
    Ok(())
}