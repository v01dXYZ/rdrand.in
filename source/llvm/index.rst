LLVM
====

Quality Assurance Basics
------------------------

To be implemented with ``buildbot``

1. ``llvm-lit``
2. ``clang`` with double stage
3. ``llvm-test-suite`` with regression reports
4. ``dtcxzyw/llvm-opt``

Issues/PRs
----------

Active
~~~~~~

* :llvm-pr:`96956` Branch Folding callbr infinite loop
* :llvm-pr:`102877` Count Leading Ones: ``DAGCombine`` to use shift.
* :llvm-issue:`106118` ``InstCombine`` for subo_carry

Stalled
~~~~~~~

* :llvm-issue:`107124` ld COFF: relocation overflows
* :llvm-pr:`106153` ``FABS``/``FSIGN``/``FCOPYSIGN`` legalize for i16 with ``Expand``.

Completed
~~~~~~~~~

* :llvm-pr:`105775` ``FPOWI`` promote f16

Canceled
~~~~~~~~

* :llvm-pr:`106076` Legalise ``FABS`` at ``LegalizeDAG``.
