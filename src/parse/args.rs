use crate::sat::{
    alg::{get_algorithm, Algorithm},
    KnfSat,
};

use super::knf_sat::human_sat_to_struct;

pub struct Parameters {
    pub sat: Option<KnfSat>,
    pub alg: Algorithm,
}

/**
 * Convert Human Readable Equation String to CNF Sat
 */
pub fn args(mut arguments: std::env::Args) -> Result<Option<Parameters>, String> {
    let argc = arguments.next().unwrap();
    let mut params = Parameters {
        sat: None,
        alg: Algorithm::new(),
    };

    while let Some(arg) = arguments.next() {
        match arg.as_str() {
            "--" => {
                if let Some(source) = arguments.next() {
                    let opt_eq = human_sat_to_struct(&source);
                    if let Ok(sat) = opt_eq {
                        params.sat = Some(sat);
                    } else if let Err(s) = opt_eq {
                        return Err(s);
                    }
                } else {
                    return Err(
                        "Expected a problem statement after `--` but got end of args".to_owned(),
                    );
                }
            }
            "-v" => {
                if let Some(v) = arguments.next() {
                    if let Ok(int) = v.parse::<u8>() {
                        let a = get_algorithm(int);
                        if let Some(alg) = a {
                            params.alg = alg;
                            continue;
                        }
                        return Err(format!(
                            "Version {} does not exist. Use `-h` option to see which do.",
                            int
                        ));
                    }
                    return Err(format!(
                        "Expected a version number after `-v` but got `{}`",
                        v.as_str()
                    ));
                }
                return Err("Expected a version number after `-v` but got end of args".to_owned());
            }
            "-h" => {
                print_help(argc);
                return Ok(None);
            }
            _ => {}
        }
    }

    // if let Ok(mut sat) = knf_sat {
    //     let mut algorithm = sat::alg::get_algorithm(sat, version);
    //     // let solutions = algorithm.solve();

    //     // if let Some(solution) = solutions {
    //     //     for a in solution {
    //     //         print!("{:?} ", a);
    //     //     }
    //     //     println!();
    //     // } else {
    //     //     println!("\nNo Solutions");
    //     // }
    // } else if let Err(err) = knf_sat {
    //     panic!("{}", err);
    // }

    Ok(Some(params))
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
