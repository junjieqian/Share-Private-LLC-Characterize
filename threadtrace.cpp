/* BEGIN_LEGAL
 * ... REFER TO OTHER FILE FOR LICENSE
 */

#include <stdio.h>
#include "pin.H"

FILE * trace;

VOID MemRef(int tid, VOID * addr) {
//    cout << tid << ',' << addr << endl;
    fprintf(trace, "%d,%p\n", tid, addr);
}

VOID Instruction(INS ins, VOID *v) 
{
  if( INS_IsMemoryRead(ins) )
    INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR) MemRef,
       IARG_THREAD_ID, IARG_MEMORYREAD_EA, IARG_END);
  if( INS_IsMemoryWrite(ins) )
    INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR) MemRef,
       IARG_THREAD_ID, IARG_MEMORYWRITE_EA, IARG_END);
}

VOID Fini(INT32 code, VOID *v)
{
    fprintf(trace, "#eof\n");
    fclose(trace);
}

INT32 Usage()
{
    PIN_ERROR( "This Pintool prints a trace of memory addresses\n" 
              + KNOB_BASE::StringKnobSummary() + "\n");
    return -1;
}

int main(int argc, char *argv[]) {
  if (PIN_Init(argc, argv)) return Usage();

  trace = fopen("pinatrace.out", "w");

  INS_AddInstrumentFunction(Instruction, 0);
  PIN_AddFiniFunction(Fini, 0);

  PIN_StartProgram();
  return 0;
}

