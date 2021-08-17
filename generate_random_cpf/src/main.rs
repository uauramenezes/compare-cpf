// Programa para gerar CPF aleatório

use rand::{thread_rng, Rng};
use std::fs::File;
use std::io::{Error, Write};

fn main() -> Result<(), Error> {
	let path = "cpf.txt";
	let mut output = File::create(path)?;
	for _ in 0..300000 {
		let cpf = generate_random_cpf();
		write!(output, "{}\n", cpf)?;
	}

	Ok(())
}

fn generate_random_number() -> u32 {
	let mut rng = thread_rng();

	let n = rng.gen_range(0..10);
	n
}

fn generate_random_cpf() -> String {
	let mut cpf = String::new();
	for _ in 0..11 {
		let number = generate_random_number().to_string();
		cpf.push_str(&number);
	}

	cpf
}
