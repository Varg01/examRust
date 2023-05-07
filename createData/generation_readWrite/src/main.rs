use rand::Rng;
use std::env;
use std::fs::File;
use std::io::{BufWriter, Write};


fn write_to_file(filename: &str, numbers: &[i32]) -> std::io::Result<()> {
    let file = File::create(filename)?;
    let mut writer = BufWriter::new(file);

    let mut buffer = String::new();
    for number in numbers {
        buffer.push_str(&number.to_string());
        if buffer.len() >= 1_000_000 {
            writer.write_all(buffer.as_bytes())?;
            buffer.clear();
        }
    }

    if !buffer.is_empty() {
        writer.write_all(buffer.as_bytes())?;
    }

    writer.flush()?;
    Ok(())
}

fn main() -> Result<(), std::io::Error> {
    let mut rng = rand::thread_rng();
    let mut numbers: Vec<i32> = Vec::new();

    // 100 000 1 000 000 and 10 000 000
    let args: Vec<String> = env::args().collect();
    if args.len() > 1 {
        let number_size = args[1].parse::<i64>().unwrap();

        for _i in 0..number_size {
            numbers.push(rng.gen_range(1..9))
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