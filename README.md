"# SAIL-to-CGEN-Coding-Challenge-" 

The attached python script () reads a structured YAML input file and converts it into a Lisp S-expression format. The transformation adheres to the semantics requested in the SAIL-to-CGEN coding challenge, handling dictionaries, lists, strings, booleans, numbers, and dates in a way that matches typical Lisp conventions.

Input: YAML file    
Output : S-expression (Lisp-like) tree

Executed script to convert a structured YAML file, specifically cmul.yaml from [riscv-unified-db/spec/std/isa/inst/B/clmul.yaml](https://github.com/riscv-software-src/riscv-unified-db/blob/main/spec/std/isa/inst/B/clmul.yaml), which contains the lower part of carry less multiplication instruction description  into a Lisp-style S-expression. 

