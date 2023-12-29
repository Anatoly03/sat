use crate::sat::{SatSolver, Variable, KnfSat};

/**
 * Algorithm: Brute Force
 * Complexity: Exponential
 */
pub type BruteForce = KnfSat;

impl SatSolver for BruteForce {
    type Input = Vec<Variable>;
    type Output = Vec<Variable>;

    fn solve(&self) -> Option<Self::Output> {
        todo!()
    }

    fn solve_all(&self) -> Vec<Self::Output> {
        todo!()
    }
}