use rand::Rng;
use std::env;
use std::fs::File;
use std::io::Write;

fn write_to_file(filename: &str, numbers: &Vec<Vec<i32>>) -> Result<(), std::io::Error> {
    let mut file = match File::create(filename) {
        Ok(file) => file,
        Err(e) => return Err(e),
    };
    for row in numbers {
        let row_string = row
            .iter()
            .map(|n| n.to_string())
            .collect::<Vec<String>>()
            .join(",");
        writeln!(file, "{}", row_string)?;
    }

    Ok(())
}

fn main() -> Result<(), std::io::Error> {
    let mut rng = rand::thread_rng();
    let mut numbers: Vec<Vec<i32>> = Vec::new();

    // 100 000 1 000 000 and 10 000 000
    let args: Vec<String> = env::args().collect();
    if args.len() > 1 {
        let number_size = args[1].parse::<usize>().unwrap();

        numbers.resize(number_size, vec![0; number_size]);

        for i in 0..number_size {
            for j in 0..number_size {
                numbers[i][j] = rng.gen_range(1..10000);
            }
        }

        match write_to_file(&args[2], &numbers) {
            Ok(()) => Ok(()),
            Err(e) => Err(e),
        }
    } else {
        println!("Parameter missing");
        return Ok(());
    }

}