use std::fs::File;
use std::io::{BufRead, BufReader, Result, Write};

pub fn read_arr(file_name: &str, arr: &mut [i64], matrix_size: usize) -> Result<()> {
    let file = File::open(file_name)?;
    let reader = BufReader::new(file);

    for (i, line) in reader.lines().enumerate() {
        for (j, num) in line?.split(',').enumerate() {
            let index = i * matrix_size + j;
            arr[index] = num.trim().parse().unwrap();
        }
    }
    Ok(())
}

pub unsafe fn matrix_multiplication(
    first_matrix: &[i64],
    second_matrix: &[i64],
    result_matrix: &mut [i64],
    matrix_size: usize,
) {
    for i in 0..matrix_size {
        for j in 0..matrix_size {
            let mut sum = 0;
            for k in 0..matrix_size {
                let a = *first_matrix.get_unchecked(i * matrix_size + k);
                let b = *second_matrix.get_unchecked(k * matrix_size + j);
                sum += a * b;
            }
            *result_matrix.get_unchecked_mut(i * matrix_size + j) = sum;
        }
    }
}

pub fn write_result(file_name: &str, result_array: &[i64], size: usize) -> Result<()> {
    let mut file = File::create(file_name)?;
    for i in 0..size {
        let mut row_string = String::new();
        for j in 0..size {
            row_string.push_str(&result_array[i * size + j].to_string());
            if j < size - 1 {
                row_string.push(',');
            }
        }
        file.write_all(row_string.as_bytes())?;
        file.write_all(b"\n")?;
    }
    Ok(())
}