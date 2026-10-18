# Contributing to qwkit

Thank you for your interest. Bug reports, questions, validation cases and pull requests are welcome.

## Reporting problems and asking questions
Open an issue on the project repository with: what you ran (a minimal script), what you expected,
what you got, and your Python, numpy and scipy versions. Questions about the physics or the model
assumptions are welcome as issues too.

## Contributing code
1. Fork the repository and create a branch.
2. Install in editable mode: `pip install -e ".[test,plots]"`.
3. Every new physical quantity needs a test checked against an analytic limit or a published number,
   in `tests/` (plain `test_*` functions; run with `pytest` or `python tests/run_tests.py`).
4. Keep units consistent with the conventions in the user guide (Angstrom and eV inside the solvers;
   SI in the propagation module) and document any new parameters with their source.
5. Run the full test suite before opening a pull request, and describe the change and its validation.

## Material parameters
New material sets should cite their source for every parameter (offset, mass, gap, permittivities,
LO-phonon energy) and include at least one validation test.

## Conduct
Participation is governed by the Code of Conduct in `CODE_OF_CONDUCT.md`.
