import signal
import sys


class ScaleneSignals:

    start_profiling_signal = signal.SIGILL
    if sys.platform != "win32":
        stop_profiling_signal = signal.SIGWINCH
        cpu_signal = signal.SIGVTALRM
        cpu_timer_signal = signal.ITIMER_REAL
        memcpy_signal = signal.SIGPROF
        # Malloc and free signals are generated by include/sampleheap.hpp.
        malloc_signal = signal.SIGXCPU
        free_signal = signal.SIGXFSZ
    else:
        cpu_signal = signal.SIGBREAK
        cpu_timer_signal = None
        stop_profiling_signal = signal.SIGTERM
        # TO DO - not yet activated for Windows
        mempcy_signal = None
        malloc_signal = None
        free_signal = None
