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

    fn optimise(&mut self) {
    
    }

    fn solve(&self) -> Option<Vec<Variable>> {
        let variables = self.sat.varsize();

        

        None
    }

    fn solve_all(&self) -> Vec<Vec<Variable>> {
        todo!()
    }
}