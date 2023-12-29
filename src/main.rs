mod parse;
mod sat;

use std::env;
use sat::KnfSat;
use parse::str_to_sat;

fn main() {
    let mut args = env::args().skip(1).into_iter();
    let mut knf_sat: Option<KnfSat> = None;

    while let Some(arg) = args.next() {
        match arg.as_str() {
            "--" => {
                if let Some(source) = args.next() {
                    knf_sat = Some(str_to_sat(&source));
                } else {
                    panic!("Expected a problem statement after `--` but got end of args")
                }
            }
            _ => {}
        }
    }

    dbg!(knf_sat);
}
