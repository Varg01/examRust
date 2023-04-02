mod matrix_multiplication;

use std::time::Instant;


// Do this and sort with O3 optimization.
fn main() {
    let size = std::env::args()
        .nth(1)
        .and_then(|arg| arg.parse::<usize>().ok())
        .unwrap_or(0);
    let file_name1 = std::env::args().nth(2).unwrap_or_default();
    let file_name2 = std::env::args().nth(3).unwrap_or_default();

    let mut first_array = Vec::with_capacity(size);
    let mut second_array = Vec::with_capacity(size);
    let mut result_array = vec![vec![0; size]; size];

    matrix_multiplication::read_arr(&file_name1, &mut first_array).unwrap();
    matrix_multiplication::read_arr(&file_name2, &mut second_array).unwrap();

    let start = Instant::now();
    
    matrix_multiplication::matrix_multiplication(&first_array, &second_array, &mut result_array, size);

    let end = Instant::now();

    let duration = end.duration_since(start);
    let elapsed_micros = duration.as_micros();

    println!("Execution time: {} microseconds", elapsed_micros);

    matrix_multiplication::write_result("result.txt", &result_array).unwrap();

}