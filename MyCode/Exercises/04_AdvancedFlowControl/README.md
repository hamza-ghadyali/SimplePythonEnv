AdvancedFlowControl README

Core Python: Advanced Flow Control

order:

stack-demo: WHILE ELSE BLOCKS
THINK OF "ELSE" AS "NOBREAK" instead
    evaluator_200.py:
        step through with a breakpoint to understand flow
        good example with program stack (see loop-else-clauses-slides.pdf slide 5)
        this is a search-failure handling example for while-else
        very common use of while-else is search-failure handling

for-else-demo: FOR-ELSE BLOCKS
    divisor_010.py and divisor_020.py:
        step through with breakpoint to understand flow
        good example of for-else
        again think of "else" as "nobreak"
        
Both for-else and while-else are uncommon and widely misunderstood.
REFACTOR these LOOP-ELSE BLOCKS by EXTRACTING THE METHOD:
    divisor_100_REFACTOR.py shows how to do this:
        define a function and return at different points
        which acts like conditionals and breaks


try-else-clauses-slides.pdf 
    --> see slide 2 LEFT SIDE
    --> see slide 4 combining try-except-else-finally
    --> try-else-demo-concept:
            count-lines.py

context managers using `with` blocks are usually preferred over try-else-finally

emulating-switch-adventure-demo:
    since python doesn't have a switch/case blocks,
    the alternative is to use functional programming paradigm
    use dictionaries to create mappings from each option to a callable function
    interesting checkpoints refactoring:
        _090 good use of lambadas (anonymous function with zero inputs)
        _100 
        _130
        _170
        _200 final result


dispatching-on-type:
    revisit later
    see also `from functools import singledispatch` documentation
    most examples here were showing poor implementations that are fragile to refactoring
    some examples here are showing a preferred approach

final section: see short-circuit-evaluation-slides.pdf
    coalescing nulls - interesting concept! see slide 10

    see search-demo:
        search_050.py and search_060.py
        simple but effective examples, see notes contained in script


    


    







    


