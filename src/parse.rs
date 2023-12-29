use super::sat::KnfSat;
use std::str::FromStr;

impl FromStr for KnfSat {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut knf_sat = KnfSat::new();

        todo!();

        Ok(knf_sat)
    }
}
