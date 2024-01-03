use crate::sat::{KnfSat, Variable};

/**
 * Convert Human Readable Equation String to CNF Sat
 */
pub fn human_sat_to_struct(s: &str) -> Result<KnfSat, String> {
    let mut knf_sat = KnfSat::new();

    for exp in s.split_ascii_whitespace() {
        match exp {
            "|" => {
                knf_sat.eq.push(Vec::new());
            }
            _ => {
                if let Ok(num) = exp.parse::<Variable>() {
                    if let Some(block) = knf_sat.eq.last_mut() {
                        block.push(num);
                        continue;
                    }
                    return Err(format!("Unexpected character `{}`", exp));
                }
                return Err(format!("Unexpected character `{}`", exp));
            }
        }
    }

    Ok(knf_sat)
}
