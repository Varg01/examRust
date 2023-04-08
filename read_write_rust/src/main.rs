mod read_write_file;

use std::time::{Duration, Instant};


// Do this and sort with O3 optimization.
fn main() {
    let file_name = std::env::args().nth(1).unwrap_or_default();


    let iterations = 10;
    let mut total_duration_read = Duration::default();
    let mut total_duration_write = Duration::default();
    for _ in 0..iterations {
        let start = Instant::now();
        let file_data = read_write_file::read_file(&file_name).unwrap();
        let end = Instant::now();
        let duration = end.duration_since(start);
        total_duration_read += duration;

        let start = Instant::now();
        read_write_file::write_file("result.txt", &file_data).unwrap();
        let end = Instant::now();
        let duration = end.duration_since(start);
        total_duration_write += duration;
    }

    println!("Average Execution time: {:.6} microseconds", total_duration_read.as_micros() as f64 / iterations as f64);
    println!("Average Execution time: {:.6} seconds", total_duration_read.as_secs_f64() / iterations as f64);
    println!("Average Execution time: {:.6} microseconds", total_duration_write.as_micros() as f64 / iterations as f64);
    println!("Average Execution time: {:.6} seconds", total_duration_write.as_secs_f64() / iterations as f64);
    

}