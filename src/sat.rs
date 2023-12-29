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
    type Input; //= Vec<Variable>;
    type Output; // = Vec<Variable>;

    /**
     * Optimise Equation so solving it becomes easier.
     */
    fn optimise(&mut self) {
        
    }

    /**
     * Guess if the equation is satisfyable without finding a result
     */
    fn verify(&self, verifee: Self::Input) -> bool {
        if let Some(_) = self.solve() {
            true
        } else {
            false
        }
    }

    /**
     * Find any satisfyable solution
     */
    fn solve(&self) -> Option<Self::Output>;

    /**
     * Find all satisfyable solutions
     */
    fn solve_all(&self) -> Vec<Self::Output>;
}
