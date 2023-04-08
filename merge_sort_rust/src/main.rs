mod merge_sort;
use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};
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
    
    let numbers_ref = &numbers;
    let num_elements = numbers_ref.len();
    println!("Number of elements in vector: {}", num_elements);
    
    let iterations = 10;
    let mut total_duration = Duration::default();
    for _ in 0..iterations {
        let mut arr = numbers.clone();
        let start = Instant::now();
        merge_sort::top_down_merge_sort(&mut arr);
        let end = Instant::now();
        let duration = end - start;
        total_duration += duration;
    }

    println!("Average Execution time: {:.6} microseconds", total_duration.as_micros() as f64 / iterations as f64);
    println!("Average Execution time: {:.6} seconds", total_duration.as_secs_f64() / iterations as f64);


}
