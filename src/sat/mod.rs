/**
 * A Variable is denoted as a non-zero number with negatives implying negations of the variable.
 */
pub type Variable = isize;

/**
 * Satisfyability in Knf
 */
#[derive(Debug)]
pub struct KnfSat {
    pub eq: Vec<Vec<Variable>>,
}

/**
 * Transformation
 */
// TODO pub type TransformSat = dyn Fn(KnfSat) -> KnfSat;

/**
 * SatSolver satisfyability
 */
pub type CanSolveSat = dyn Fn(KnfSat) -> bool;

/**
 * SatSolver
 */
pub type SolveSat = dyn Fn(KnfSat) -> Vec<Variable>;

/**
 * SatSolver
 */
pub type SolveAllSat = dyn Fn(KnfSat) -> Vec<Vec<Variable>>;

/**
 * Implementations
 */
impl KnfSat {
    pub fn new() -> Self {
        Self { eq: vec![vec![]] }
    }
}
