mod matrix_multiplication;

use std::time::{Duration, Instant};
use std::fs::File;
use std::io::{BufRead, BufReader, Write};


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

    let mut output_file = File::create("output.txt").expect("Failed to create output file"); 
    let iterations = 10;
    let mut total_duration = Duration::default();
    for i in 0..iterations {
        matrix_multiplication::read_arr(&file_name1, &mut first_array).unwrap();
        matrix_multiplication::read_arr(&file_name2, &mut second_array).unwrap();

        let start = Instant::now();
        matrix_multiplication::matrix_multiplication(&first_array, &second_array, &mut result_array, size);
        let end = Instant::now();
        let duration = end.duration_since(start);
        total_duration += duration;
        writeln!(output_file, "Duration for Iteration {}: {:.6} microseconds", i + 1, duration.as_micros() as f64).expect("Failed to create output file");
    }

    let average_micros = total_duration.as_micros() as f64 / iterations as f64;
    let average_secs = total_duration.as_secs_f64() / iterations as f64;

    writeln!(output_file, "Average Execution time: {:.6} microseconds", average_micros).unwrap(); // Write average duration to output file
    writeln!(output_file, "Average Execution time: {:.6} seconds", average_secs).unwrap(); // Write average duration to output file

    matrix_multiplication::write_result("result.txt", &result_array).unwrap();

}