use std::path::PathBuf;

use docopt::Docopt;
use serde::Deserialize;
use egg::*;

use rewrite_eqsat::analysis::TensorAnalysis;
use rewrite_eqsat::rules::*;
use rewrite_eqsat::language::TensorLang;

use rewrite_eqsat::tvm::from_relay;

const USAGE: &'static str = "
Equality Saturation based prototype for graph rewriting

Usage:
    eqsat (-h | --help)
    eqsat [-s | --stats] [--node-limit <N>] [--explain] [--svg] <expression>
    eqsat [-s | --stats] [--node-limit <N>] [--explain] [--svg] -f <file>

Options:
  -h --help     Show this screen.
  --explain     Show list of transformations for this exception.
  --svg         Create svg files for equality saturation graphs.
  -s --stats    Print statistics considering the size of the used egraph, 
                and the runtime of equality saturation
  -f --file     relay file to run optimization over
  --node-limit  maximum number of nodes in the e-graph
";

#[derive(Debug, Deserialize)]
struct Args {
    flag_explain: bool,
    flag_stats: bool, 
    flag_svg: bool,
    arg_expression: String,
    arg_file: PathBuf,
    flag_node_limit: usize,
}

fn main() {
    let args: Args = Docopt::new(USAGE)
        .and_then(|d| d.deserialize())
        .unwrap_or_else(|e| e.exit());
    
    let mut runner: Runner<TensorLang, TensorAnalysis> = Runner::default();
    if args.flag_explain{
        runner = runner.with_explanations_enabled();
    }

    if args.flag_node_limit != 0 {
      runner = runner.with_node_limit(args.flag_node_limit);
    }

    let mut start = "nil".parse().unwrap();
    if args.arg_expression != "" {
        start = args.arg_expression.parse().unwrap();
        runner = runner.with_expr(&start);
    }else if args.arg_file.exists() {
        println!("Opening file {}", args.arg_file.to_string_lossy());
        start = from_relay(args.arg_file).unwrap();
        runner = runner.with_expr(&start);
    }else{
        panic!("Either file or expression must be given");
    }

    if args.flag_svg {
        runner.egraph.dot().to_svg("egraph_start.svg").unwrap()
    }


    let rules = all_rules();
    runner = runner.run(&rules);
    
    let extractor = Extractor::new(&runner.egraph, AstSize);

    let (best_cost, best_expr) = extractor.find_best(runner.roots[0]);


    if args.flag_stats {
        runner.print_report();
    }

    if args.flag_svg {
        runner.egraph.dot().to_svg("egraph_end.svg").unwrap();
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