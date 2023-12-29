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

    pub fn is_solution(verify: Vec<Variable>) -> bool {
        todo!()
    }
}
