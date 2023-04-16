mod merge_sort;
use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader, Write};
use std::time::{Duration, Instant};



fn main() {
    let args: Vec<String> = env::args().collect();

    let file = File::open(&args[1]).unwrap();
    let reader = BufReader::new(file);

    let mut numbers: Vec<i32> = Vec::new();

    for line in reader.lines() {
        let input = line.unwrap();

        numbers = input
            .split(',')
            .map(|s| s.trim().parse::<i32>().unwrap())
            .collect::<Vec<i32>>();
    }

    let mut output_file = File::create("output.txt").expect("Failed to create output file"); 
    let iterations = 10;
    let mut total_duration = Duration::default();
    for i in 0..iterations {
        let mut arr = numbers.clone();
        let start = Instant::now();
        merge_sort::top_down_merge_sort(&mut arr);
        let end = Instant::now();
        let duration = end - start;
        total_duration += duration;
        writeln!(output_file, "Duration for Iteration {}: {:.6} microseconds", i + 1, duration.as_micros() as f64).expect("Failed to create output file");
    }

    let average_micros = total_duration.as_micros() as f64 / iterations as f64;
    let average_secs = total_duration.as_secs_f64() / iterations as f64;

    writeln!(output_file, "Average Execution time: {:.6} microseconds", average_micros).unwrap(); // Write average duration to output file
    writeln!(output_file, "Average Execution time: {:.6} seconds", average_secs).unwrap(); // Write average duration to output file

    output_file.flush().expect("Failed to flush output file");


}
