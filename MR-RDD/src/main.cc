/* main.cc
 * jqian.unl@gmail.com
 */

#include <fstream>    // std::ifstream, std::ofstream
#include <boost/algorithm/string.hpp>
#include <vector>
#include <stdlib.h> // exit

using namespace boost;

int setsize    = 16;      // 16-way set associative
int setnum     = 8192;    // total 8192 sets on the cache
string infile  = "";      // trace file name
string outfile = "";      // output file name

// process the command line options
void doargs(int argc, char ** argv) {
  int i = 0;
  int blocksize = 0;
  for (;i<argc;++i) {
    if ( argv[i] == "-set" )
      setsize = atoi(argv[++i].c_str());
    else if ( argv[i] == "-block" ) {
      blocksize = atoi(argv[++i].c_str());
      setnum = cachesize/(setsize*blocksize);
    }
    else if ( argv[i] == "-infile" )
      infile = argv[++i];
    else if ( argv[i] == "-outfile" )
      outfile = argv[++i];
    else {
      helper();
      exit(0);
    }
  } // end for loop, parser the args
}

// helper function
int helper() {
  cout << "USAGE of this tool: simulator -set [integer, set associative] -block [integer in byte] -infile [path to the trace file] -outfile [path to output file]\n";
  cout << "\t default values, -set is 16, -block is 64B, -infile and -outfile are NULL\n"
  return 0;
}

// everything starts from here
int main(int argc, char ** argv) {
  if (argc<2) return helper();

  doargs(argc, argv);
  cache lruCache = new cache(cachesize, setsize, setnum);
  ifstream tracefile (filename);
  string line;
  vector<string> tokens;
  int setid = 0;
  string address = "";
  int threadid = -1;

  if (tracefile.is_open()) {
    while (getline (tracefile, line)) {
      tokens.clear();
      split(tokens, line, is_any_of(' '));
	  // TODO
    } // end getline while
  } // end tracefile open if

}
