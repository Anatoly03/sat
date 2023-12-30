use crate::sat::{SatSolver, Variable, KnfSat};

/**
 * Algorithm: Brute Force
 * Complexity: Exponential
 */
pub struct BruteForce {
    sat: KnfSat
}

impl SatSolver for BruteForce {
    fn new(sat: KnfSat) -> Self {
        BruteForce {
            sat
        }
    }

    fn solve(&self) -> Option<Vec<Variable>> {
        todo!()
    }

    fn solve_all(&self) -> Vec<Vec<Variable>> {
        todo!()
    }
}