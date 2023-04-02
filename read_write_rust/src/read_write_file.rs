use std::fs::{File, OpenOptions};
use std::io::{Result, Write, Read};


pub fn read_file(file_name: &str) -> Result<String> {
    let mut file = File::open(file_name)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}

pub fn write_file(file_name: &str, file_data: &str) -> Result<()> {
    let mut file = OpenOptions::new()
        .write(true)
        .create(true)
        .truncate(true)
        .open(file_name)?;
    file.write_all(file_data.as_bytes())?;
    Ok(())
}
