#!/bin/bash
# Phase 2 job queue (14 Oct 2026): METH-01 scan, then N2 tuning, after the MAT-03 queue.
export PYTHONPATH=/home/claude/qwkit OMP_NUM_THREADS=1 NPROC=2
while [ ! -f /home/claude/qwkit/studies/mat03/queue2.done ]; do sleep 15; done
cd /home/claude/qwkit/studies/meth01 && python3 -W ignore scan.py > scan.log 2>&1 && echo done > scan.done
cd /home/claude/qwkit/studies/n2 && python3 -W ignore tuning.py > tuning.log 2>&1 && echo done > tuning.done
