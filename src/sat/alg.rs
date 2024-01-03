use crate::sat::{CanSolveSat, SolveSat, SolveAllSat, KnfSat};

pub struct Algorithm {
    pub name: String,
    pub satisfiable: Option<Box<CanSolveSat>>,
    pub solve: Option<Box<SolveSat>>,
    pub solve_all: Option<Box<SolveAllSat>>,
}

pub fn get_algorithm(sat: KnfSat, alg: u8) -> Algorithm {
    match alg {
        0 => return Algorithm {
            name: "(Default) Brute Force".to_string(),
            satisfiable: None,
            solve: None,
            solve_all: None,
        },
        _ => panic!("Version {} does not exist. Use `-h` option to see which do.", alg)
    }
}