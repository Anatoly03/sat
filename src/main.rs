mod parse;
mod sat;
#[cfg(test)]
mod test;

use sat::KnfSat;
use std::{env, str::FromStr};

fn main() {
    let mut args = env::args().skip(1).into_iter();
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
                    panic!("Expected a version number after `-v` but got `{}`", v.as_str())
                }
                panic!("Expected a version number after `-v` but got end of args")
            }
            _ => {}
        }
    }

    // TODO execute algorithm VERSION
    // TODO with parameter KNF_SAT

    dbg!(knf_sat);
}
