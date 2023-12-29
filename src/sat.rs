/**
 * A Variable is denoted as a non-zero number with negatives implying negations of the variable.
 */
pub type Variable = isize;

/**
 * Satisfyability in Knf
 */
#[derive(Debug)]
pub struct KnfSat(Vec<Vec<Variable>>);

/**
 * Implementations
 */
impl KnfSat {
    pub fn new() -> Self {
        Self(Vec::new())
    }

    pub fn is_solution(verify: Vec<Variable>) -> bool {
        todo!()
    }
}
