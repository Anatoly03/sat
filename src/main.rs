mod parse;
mod sat;
#[cfg(test)]
mod test;

fn main() {
    let args = parse::args(std::env::args().into_iter());

    if let Ok(Some(params)) = args {
        // TODO
        println!("Success!");
        dbg!(params.sat);
    } else if let Err(err) = args {
        eprintln!("{}", err);
        std::process::exit(1);
    }
}
