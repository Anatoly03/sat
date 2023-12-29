use super::sat::{KnfSat, Variable};
use std::str::FromStr;

impl FromStr for KnfSat {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut knf_sat = KnfSat::new();

        for exp in s.split_ascii_whitespace() {
            match exp {
                "|" => {
                    knf_sat.0.push(Vec::new());
                }
                _ => {
                    if let Ok(num) = exp.parse::<Variable>() {
                        if let Some(block) = knf_sat.0.last_mut() {
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
}
