use crate::sat::{SatSolver, KnfSat};
mod bf0;

pub fn get_algorithm<'a>(sat: KnfSat, alg: u8) -> impl SatSolver {
    match alg {
        0 => bf0::BruteForce::new(sat),
        _ => panic!("Version {} does not exist. Use `-h` option to see which do.", alg)
    }
}