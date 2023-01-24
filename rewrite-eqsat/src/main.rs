use std::path::PathBuf;

use docopt::Docopt;
use serde::Deserialize;
use egg::*;

use rewrite_eqsat::analysis::TensorAnalysis;
use rewrite_eqsat::rules::*;
use rewrite_eqsat::language::TensorLang;

#[cfg(feature = "tvm")]
use rewrite_eqsat::tvm::from_relay;

const USAGE: &'static str = "
Equality Saturation based prototype for graph rewriting

Usage:
    eqsat (-h | --help)
    eqsat [-s | --stats] [--explain] <expression>
    eqsat [-s | --stats] [--explain] -f <file>

Options:
  -h --help     Show this screen.
  --explain     Show list of transformations for this exception.
  -s --stats    Print statistics considering the size of the used egraph, 
                and the runtime of equality saturation
  -f --file     relay file to run optimization over
";

#[derive(Debug, Deserialize)]
struct Args {
    flag_explain: bool,
    flag_stats: bool, 
    arg_expression: String,
    arg_file: PathBuf,
}

fn main() {
    let args: Args = Docopt::new(USAGE)
        .and_then(|d| d.deserialize())
        .unwrap_or_else(|e| e.exit());
    
    let mut start = "a".parse().unwrap();
    if args.arg_expression != "" {
        start = args.arg_expression.parse().unwrap();
    }

    let rules = all_rules();

    let mut runner: Runner<TensorLang, TensorAnalysis> = Runner::default();
    
    if args.flag_explain{
        runner = runner.with_explanations_enabled();
    }

    runner = runner.with_expr(&start).run(&rules);
    
    let extractor = Extractor::new(&runner.egraph, AstSize);

    let (best_cost, best_expr) = extractor.find_best(runner.roots[0]);


    if args.flag_stats {
        runner.print_report();
    }

    if args.flag_explain {
        let mut explanation = runner.explain_equivalence(&start, &best_expr);
        
        
        println!("The following transformations produce the minimal cost function:");
        println!("");
        println!("{}", explanation.get_flat_string());
        println!("");
    }

    println!("Best Expr: {best_expr}");
    println!("Best Cost: {best_cost}");
}