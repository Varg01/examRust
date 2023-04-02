mod read_write_file;

use std::time::Instant;


// Do this and sort with O3 optimization.
fn main() {
    let file_name = std::env::args().nth(1).unwrap_or_default();

     let file_data = read_write_file::read_file(&file_name).unwrap();

    let start = Instant::now();

    let end = Instant::now();

    let duration = end.duration_since(start);
    let elapsed_micros = duration.as_micros();

    println!("Execution time: {} microseconds", elapsed_micros);

    read_write_file::write_file("result.txt", &file_data).unwrap();

}