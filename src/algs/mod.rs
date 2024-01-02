use crate::sat::{SatSolver, KnfSat};
mod bf0;
mod knf3bf0;

pub fn get_algorithm<T: SatSolver>(sat: KnfSat, alg: u8) -> T {
    match alg {
        0 => return bf0::BruteForce::new(sat),
        // 1 => return knf3bf0::Sat3KnfBruteForce::new(sat),
        _ => panic!("Version {} does not exist. Use `-h` option to see which do.", alg)
    }
}