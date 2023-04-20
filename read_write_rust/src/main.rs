mod read_write_file;

use std::fs::File;
use std::io::{Write};
use std::time::{Duration, Instant};



// Do this and sort with O3 optimization.
fn main() {

    let size = std::env::args()
        .nth(1)
        .and_then(|arg| arg.parse::<usize>().ok())
        .unwrap_or(0);
    let file_name = std::env::args().nth(2).unwrap_or_default();
    let iterations = std::env::args()
    .nth(3)
    .and_then(|arg| arg.parse::<usize>().ok())
    .unwrap_or(0);


    let mut output_file_name = std::env::args().nth(4).unwrap_or_default();
    output_file_name.push_str(&size.to_string());
    let mut output_file = File::create(&output_file_name).expect("Failed to create output file");

    let mut total_duration_read = Duration::default();
    let mut total_duration_write = Duration::default();
    for i in 0..iterations {
        let start = Instant::now();
        let file_data = read_write_file::read_file(&file_name).unwrap();
        let end = Instant::now();
        let duration = end.duration_since(start);
        total_duration_read += duration;
        writeln!(output_file, "Read duration for Iteration {}: {:.6} microseconds", i + 1, duration.as_micros() as f64).expect("Failed to create output file");
        writeln!(output_file, "Read duration for Iteration {}: {:.6} microseconds", i + 1, duration.as_secs_f64() as f64).expect("Failed to create output file");

        let start = Instant::now();
        read_write_file::write_file("result.txt", &file_data).unwrap();
        let end = Instant::now();
        let duration = end.duration_since(start);
        total_duration_write += duration;
        writeln!(output_file, "Write duration for Iteration {}: {:.6} microseconds", i + 1, duration.as_micros() as f64).expect("Failed to create output file");
        writeln!(output_file, "Write duration for Iteration {}: {:.6} microseconds", i + 1, duration.as_secs_f64() as f64).expect("Failed to create output file");
    }

    writeln!(output_file, "Average Execution time read: {:.6} microseconds", total_duration_read.as_micros() as f64 / iterations as f64).unwrap();
    writeln!(output_file, "Average Execution time read: {:.6} seconds", total_duration_read.as_secs_f64() / iterations as f64).unwrap();
    writeln!(output_file, "Average Execution time write: {:.6} microseconds", total_duration_write.as_micros() as f64 / iterations as f64).unwrap();
    writeln!(output_file, "Average Execution time write: {:.6} seconds", total_duration_write.as_secs_f64() / iterations as f64).unwrap();


}