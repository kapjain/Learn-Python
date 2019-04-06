#http://www.pydev.org/manual_adv_remote_debugger.html
import pydevd
# epdb1.py -- experiment with the Python debugger, pdb
# go to C:\Users\Kapil Jain\git\kapil\TestPython\python_debug_pdb and run python pdbEx.py
a = "aaa"
#pydevd.settrace(host, stdoutToServer, stderrToServer, port, suspend, trace_only_current_thread, overwrite_prev_trace, patch_multiprocessing)
#pydevd.settrace()
pydevd.settrace(stdoutToServer=True, stderrToServer=True) #Debug Server at port: 5678
b = "bbb"
c = "ccc"
final = a + b + c
print (final)