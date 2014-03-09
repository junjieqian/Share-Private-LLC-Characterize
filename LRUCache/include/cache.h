/* cache.h
 * this is not one LLC implementation, but one tool to analyze the Reuse Distance Distribution tool
 * Information wantted: whether this one is supposed to be in cache
 */

#ifndef _CACHE_H_
#define _CACHE_H_

#include <iostream>   // std::cout
#include <list>       // std::list
#include <string.h>   // std::string
#include <map>        // std::map

typedef long long line_stamp;


class cache {
private:
  map<line_stamp, string> LineStampAddress;
  map<int, long long> ReuseDistanceDistribution;
public:
  cache ();
  void ClearCache ();
  int Get (string address);
  int Put (string address, int data);
  void IncrementLRU(int set, int block);
  ~cache ();

}

#endif
// CACHE.H
