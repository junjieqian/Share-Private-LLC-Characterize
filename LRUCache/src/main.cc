/* main.cc
 *
 */

#include "cache.h"

// process the command line options
void doargs(int argc, char ** argv) {

}

// helper function
int helper() {
  cout << "USAGE of this tool....\n";
  return 0;
}

// everything starts from here
int main(int argc, char ** argv) {
  if (argc<2) return helper();

  doargs(argc, argv);
}
