use crate::sat::{CanSolveSat, SolveAllSat, SolveSat};

pub struct Algorithm {
    pub name: String,
    pub satisfiable: Option<Box<CanSolveSat>>,
    pub solve: Option<Box<SolveSat>>,
    pub solve_all: Option<Box<SolveAllSat>>,
}

impl Algorithm {
    pub fn new() -> Self {
        Self {
            name: "(Default) Brute Force".to_string(),
            satisfiable: None,
            solve: None,
            solve_all: None,
        }
    }
}

pub fn get_algorithm(alg: u8) -> Option<Algorithm> {
    match alg {
        0 => Some(Algorithm {
            name: "(Default) Brute Force".to_string(),
            satisfiable: None,
            solve: None,
            solve_all: None,
        }),
        _ => None,
    }
}
