pub mod solver;

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
 * Implementations
 */
impl KnfSat {
    pub fn new() -> Self {
        Self {
            eq: vec![vec![]]
        }
    }

    /**
     * Rename variables to tightly cover [1 .. output]
     */
    pub fn flatten(&mut self) -> usize {
        let mut reference = vec![];

        for clausel in &mut self.eq {
            for literal in clausel {
                let pos = reference.iter().position(|&r| r == literal.abs());

                let new_val: Variable = if let Some(p) = pos {
                    p as Variable + 1
                } else {
                    reference.push((literal).abs());
                    reference.len() as Variable
                };

                if literal > &mut 0 {
                    *literal = new_val;
                } else {
                    *literal = -new_val;
                }
            }
        }

        reference.len()
    }

    /**
     * Counter of Variables in the equation
     */
    pub fn varsize(&self) -> usize {
        let mut reference = vec![];

        for clausel in &self.eq {
            for literal in clausel {
                let pos = reference.iter().position(|&r| r == literal.abs());

                if let None = pos {
                    reference.push((literal).abs());
                };
            }
        }

        reference.len()
    }
}