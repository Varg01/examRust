use rand::Rng;
use std::env;
use std::fs::File;
use std::io::Write;


fn write_to_file(filename: &str, numbers: &[i32], buffer_size: usize) -> Result<(), std::io::Error> {
    let mut file = match File::create(filename) {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    for chunk in numbers.chunks(buffer_size) {
        let number_string = chunk.iter()
            .map(|n| n.to_string())
            .collect::<Vec<String>>()
            .join("");
        match file.write_all(number_string.as_bytes()) {
            Ok(()) => (),
            Err(e) => return Err(e),
        }
    }

    Ok(())
}


fn main() -> Result<(), std::io::Error> {
    let mut rng = rand::thread_rng();
    let mut numbers: Vec<i32> = Vec::new();

    // 100 million
    let args: Vec<String> = env::args().collect();
    if args.len() > 1 {
        let number_size = args[1].parse::<usize>().unwrap();
        let buffer_size = 1_000_000;

        for _i in 0..number_size {
            numbers.push(rng.gen_range(0..9))
        }

        match write_to_file(&args[2], &numbers, buffer_size) {
            Ok(()) => Ok(()),
            Err(e) => Err(e),
        }
    } else {
        println!("Parameter missing");
        return Ok(());
    }
}