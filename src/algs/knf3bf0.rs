// use crate::sat::{SatSolver, Variable, KnfSat};

// /**
//  * Algorithm: 3-KNF-SAT Brute Force
//  * Complexity: Exponential
//  */
// pub struct Sat3KnfBruteForce {
//     sat: KnfSat
// }

// impl SatSolver for Sat3KnfBruteForce {
//     fn new(sat: KnfSat) -> Self {
//         Sat3KnfBruteForce {
//             sat
//         }
//     }

//     fn optimise(&mut self) {
    
//     }

//     fn solve(&self) -> Option<Vec<Variable>> {
//         let variables = self.sat.varsize();

        

//         None
//     }

//     fn solve_all(&self) -> Vec<Vec<Variable>> {
//         todo!()
//     }
// }