#!/bin/sh
# Waits for the MAT-01 chain, backs up pre-boundary-fix outputs, then reruns NL-05, N1, NL-02, MS-02.
cd "$(dirname "$0")"
while kill -0 3804 2>/dev/null; do sleep 60; done
for d in n1_paper n1 nl02 nl05 ms02; do
  mkdir -p $d/pre_bcfix; cp $d/*.json $d/*.log $d/pre_bcfix/ 2>/dev/null
done
for s in rerun_nl05.sh rerun_n1.sh rerun_nl02.sh rerun_ms02.sh; do
  echo "start $s $(date)" >> queue_bcfix.log
  nice -n 5 sh $s >> queue_bcfix.log 2>&1 || echo "FAILED $s" >> queue_bcfix.log
  echo "end $s $(date)" >> queue_bcfix.log
done
echo QUEUE-DONE >> queue_bcfix.log
