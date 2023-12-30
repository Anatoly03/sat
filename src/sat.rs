/**
 * A Variable is denoted as a non-zero number with negatives implying negations of the variable.
 */
pub type Variable = isize;

/**
 * Satisfyability in Knf
 */
#[derive(Debug)]
pub struct KnfSat(pub Vec<Vec<Variable>>);

/**
 * Implementations
 */
impl KnfSat {
    pub fn new() -> Self {
        Self(vec![vec![]])
    }
}

/**
 * Algorithmic Implementations
 */
pub trait SatSolver {
    /**
     * Create new instance
     */
    fn new(_s: KnfSat) -> Self;

    /**
     * Optimise Equation so solving it becomes easier.
     */
    fn optimise(&mut self) {
        
    }

    /**
     * Guess if the equation is satisfyable without finding a result
     */
    fn verify(&self, _verifee: Vec<Variable>) -> bool {
        if let Some(_) = self.solve() {
            true
        } else {
            false
        }
    }

    /**
     * Find any satisfyable solution
     */
    fn solve(&self) -> Option<Vec<Variable>>;

    /**
     * Find all satisfyable solutions
     */
    fn solve_all(&self) -> Vec<Vec<Variable>>;
}
