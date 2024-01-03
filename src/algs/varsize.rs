use crate::sat::KnfSat;

impl KnfSat {
    /**
     * **Algorithm**: Count Variables in Equation
     * **Complexity**: Polynomial
     */
    pub fn varsize(sat: &KnfSat) -> usize {
        let mut reference = vec![];
    
        for clausel in &sat.eq {
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