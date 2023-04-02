mod merge_sort;
use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

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

    let mut arr = numbers;

    merge_sort::top_down_merge_sort(&mut arr);
}
