use crate::sat::{SatSolver, KnfSat};
mod bf0;

pub fn solve(sat: KnfSat, alg: u8) {
    match alg {
        0 => {
            println!("we land here")
        }
        _ => panic!("Version {} does not exist. Use `-h` option to see which do.", alg)
    }
}