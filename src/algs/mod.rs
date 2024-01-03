pub mod bf0;
pub mod flatten;
pub mod knf3;
pub mod varsize;

// pub fn get_algorithm<T: SatSolver>(sat: KnfSat, alg: u8) -> T {
//     match alg {
//         0 => return bf0::BruteForce::new(sat),
//         // 1 => return knf3bf0::Sat3KnfBruteForce::new(sat),
//         _ => panic!("Version {} does not exist. Use `-h` option to see which do.", alg)
//     }
// }