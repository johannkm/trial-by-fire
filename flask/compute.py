from flask import jsonify
from typing import Callable

from sandbox import getRunnable, getCanonical, getMutants

import sys
from io import StringIO
import contextlib


def runSubmission(id: int, tests: [str]):

    results = {'status': 'good'}  # all mutations fail by default

    # NOTE: For each mutant, all test cases are run.
    # A test case kills a mutant if it makes it fail (but succeeds for the solution).
    # This is known as 'Mutation Testing'.

    # NOTE (unknown): Can test cases be written to only succeed for a specific algorithm?

    # The solution score is determined by how many mutants a user kills.

    # NOTE: using "sum a and b" as example

    # TODO: Get flawed solutions that correspond to a needed test case.

    ### CANONICAL SOLUTIONS
    canonical_runnable: str = getRunnable(id, tests, getCanonical(id))

    local = {}
    exec(canonical_runnable, {}, local)

    canonical_results = local['results']

    # a test case failed on canonical solution (one is False)
    if not all(canonical_results.values()):
        results['status'] = 'bad'
        for key, val in canonical_results.items():
            if not val:
                results['case'] = key  # return bad test case
                return results
    
    ### MUTATIONS
    mutants: [str] = getMutants(id)
    for mutant in mutants:
        mutant_algo, mutant_messages = mutant
        mutant_runnable: str = getRunnable(id, tests, mutant_algo)

        local = {}
        exec(mutant_runnable, {}, local)

        mutant_results = local['results']

        # missing test case for a mutation (all True for a mutation)
        if all(mutant_results.values()):
            results['status'] = 'missing'
            if 'messages' not in results:
                results['messages'] = []
            for mutant_message in mutant_messages:
                results['messages'].append(mutant_message)
        print("mutant results")
        print(mutant_results)

    return results

    # # Mutants alive by default
    # killed: {str: bool} = {}
    # for mutant in mutants:
    #     killed[mutant] = False

    # # Killing procedure
    # for name, mutant in mutants.items():
    #     if code(mutant) == False:  # if a test kills it
    #         killed[name] = True
    #         break  # mutant killed
                
    # return killed


        
