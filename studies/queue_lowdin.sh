#!/bin/sh
# Full regeneration after the buffered-Loewdin fix (qwkit 0.6.1). MS-02 timings first, on the idle machine.
cd "$(dirname "$0")"
export PYTHONPATH=$(cd .. && pwd)
date; echo "== MS-02 validate2 (timings)"
(cd ms02 && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 validate2.py > validate2_t1.log 2>&1 && \
 OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 TIMING_ONLY=1 python3 validate2.py > validate2_t2.log 2>&1) || echo "validate2 FAILED"
date; echo "== N1"; sh rerun_n1.sh > rerun_n1.log 2>&1 || echo "N1 FAILED"
date; echo "== NL-02"; sh rerun_nl02.sh > rerun_nl02.log 2>&1 || echo "NL02 FAILED"
date; echo "== NL-05"; sh rerun_nl05.sh > rerun_nl05.log 2>&1 || echo "NL05 FAILED"
date; echo "== TPV-05"; sh rerun_tpv05.sh > rerun_tpv05.log 2>&1 || echo "TPV05 FAILED"
date; echo "== MS-02 rest"
sed '/validate2.py/d' rerun_ms02.sh > rerun_ms02_rest.sh && sh rerun_ms02_rest.sh > rerun_ms02.log 2>&1 || echo "MS02 FAILED"
date; echo QUEUE-DONE
