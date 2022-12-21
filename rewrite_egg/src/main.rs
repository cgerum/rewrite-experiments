use docopt::Docopt;
use serde::Deserialize;
use egg::*;

use rewrite_egg::analysis::TensorAnalysis;
use rewrite_egg::rules::*;
use rewrite_egg::language::TensorLang;

const USAGE: &'static str = "
Equality Saturation based prototype for graph rewriting

Usage:
    eqsat (-h | --help)
    eqsat [--explain] <EXPRESSION>

Options:
  -h --help     Show this screen.
  --explain     Show list of transformations for this exception.
";

#[derive(Debug, Deserialize)]
struct Args {
    flag_explain: bool,
    arg_EXPRESSION: String, 
}

fn main() {
    let args: Args = Docopt::new(USAGE)
        .and_then(|d| d.deserialize())
        .unwrap_or_else(|e| e.exit());
    

    let start: RecExpr<TensorLang> = args.arg_EXPRESSION.parse().unwrap();

    let rules = all_rules();

    let runner: Runner<TensorLang, TensorAnalysis> = Runner::default().with_expr(&start).run(&rules);
    
    let extractor = Extractor::new(&runner.egraph, AstSize);

    let (best_cost, best_expr) = extractor.find_best(runner.roots[0]);

    println!("Best Expr: {best_expr}");
    println!("Best Cost: {best_cost}");
}