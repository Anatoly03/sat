mod parse;
mod sat;
#[cfg(test)]
mod test;

use sat::KnfSat;
use std::{env, str::FromStr};

fn main() {
    let mut args = env::args().into_iter();
    let argc = args.next().unwrap();
    let mut knf_sat: Result<KnfSat, String> = Err("SAT Equation not specified".to_owned());
    let mut version: i8 = 0;

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
                    if let Ok(int) = v.parse::<i8>() {
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

    // TODO execute algorithm VERSION
    // TODO with parameter KNF_SAT

    dbg!(knf_sat);
}

fn print_help(argc: String) {
    println!("======== SAT SOLVER ========
Usage: {} -- \"SAT\" [OPTIONS]
Sat Grammar:
    \x1b[36mS\x1b[0m →\t\x1b[36mA\x1b[0m \x1b[33m| \t\x1b[36mS\x1b[0m \x1b[31m\"|\" \x1b[36mS\x1b[0m\t\t\x1b[30m% Example Sat: 1 2 -3 | 3 4 -5 | -5 -6\x1b[0m
    \x1b[36mA\x1b[0m →\t\x1b[36mN\x1b[0m \x1b[33m| \t\x1b[36mA\x1b[0m \x1b[31m\"|\" \x1b[36mA\x1b[0m
    \x1b[36mN\x1b[0m →\t\x1b[31m\"-\"\x1b[0m \x1b[33m? \x1b[36mI\x1b[0m   \t\t\x1b[30m% Negativity represents Negation
    \x1b[36mI\x1b[0m →\t\x1b[33m[\x1b[31m1-9\x1b[33m] [\x1b[31m0-9\x1b[33m]*\t\t\x1b[30m% Integers represent variable identifiers\x1b[0m
Options: 
    -v : Run specific algorithm
        0 : Brute Force
    -h : Print this help message
============================",
        argc
    );
}
