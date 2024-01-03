use crate::sat::{KnfSat, Variable};

/**
 * **Algorithm**: Rename Variables to fill [0..n]
 * **Complexity**: Polynomial `O(n^2)`
 */
pub fn flatten(mut sat: KnfSat) -> KnfSat {
    let mut reference = vec![];

    for clausel in &mut sat.eq {
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
    
    sat
}
