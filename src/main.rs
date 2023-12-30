mod algs;
mod parse;
mod sat;
#[cfg(test)]
mod test;

use sat::{KnfSat, SatSolver};
use std::{env, str::FromStr};

fn main() {
    let mut args = env::args().into_iter();
    let argc = args.next().unwrap();
    let mut knf_sat: Result<KnfSat, String> = Err("SAT Equation not specified".to_owned());
    let mut version: u8 = 0;

    while let Some(arg) = args.next() {
        match arg.as_str() {
            "--" => {
                if let Some(source) = args.next() {
                    knf_sat = KnfSat::from_str(&source);
                } else {
                    panic!("Expected a problem statement after `--` but got end of args")
                }
            }
            "-v" => {
                if let Some(v) = args.next() {
                    if let Ok(int) = v.parse::<u8>() {
                        version = int;
                        continue;
                    }
                    panic!(
                        "Expected a version number after `-v` but got `{}`",
                        v.as_str()
                    )
                }
                panic!("Expected a version number after `-v` but got end of args")
            }
            "-h" => {
                print_help(argc);
                return;
            }
            _ => {}
        }
    }

    if let Ok(mut sat) = knf_sat {
        sat.flatten();
        let mut algorithm = algs::get_algorithm(sat, version);
        algorithm.optimise();
        let solutions = algorithm.solve();

        if let Some(solution) = solutions {
            for a in solution {
                print!("{:?} ", a);
            }
            println!();
        } else {
            println!("\nNo Solutions");
        }
    } else if let Err(err) = knf_sat {
        panic!("{}", err);
    }
}

fn print_help(argc: String) {
    println!("======== SAT SOLVER ========
Usage: {} -- \"\x1b[36mS\x1b[0m\" [OPTIONS]
======= SAT Grammar ========
    \x1b[36mS\x1b[0m →\t\x1b[36mA\x1b[0m \x1b[33m| \t\x1b[36mS\x1b[0m \x1b[31m\" | \" \x1b[36mS\x1b[0m\t\t\x1b[30m% Example Sat: 1 2 -3 | 3 4 -5 | -5 -6\x1b[0m
    \x1b[36mA\x1b[0m →\t\x1b[36mN\x1b[0m \x1b[33m| \t\x1b[36mA\x1b[0m \x1b[31m\" \" \x1b[36mA\x1b[0m
    \x1b[36mN\x1b[0m →\t\x1b[31m\"-\"\x1b[0m \x1b[33m? \x1b[36mI\x1b[0m   \t\t\x1b[30m% Negativity represents Negation
    \x1b[36mI\x1b[0m →\t\x1b[33m[\x1b[31m1-9\x1b[33m] [\x1b[31m0-9\x1b[33m]*\t\t\x1b[30m% Integers represent variable identifiers\x1b[0m
========= Options ==========
    -v : Run specific algorithm
        0 : Brute Force
    -h : Print this help message
============================",
        argc
    );
}
