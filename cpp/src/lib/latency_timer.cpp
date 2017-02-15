#include <stdio.h>
#include <math.h>
#include <sys/time.h>
#include <unistd.h>
#include "latency_timer.h"


using namespace std;

latency_timer::latency_timer()
{
  activated = false;
}

latency_timer::~latency_timer()
{
}

// set a timer with latency in milliseconds
bool latency_timer::setTimer(int milliseconds)
{
  if(activated)
  {
    printf("Error in latency_timer::setTimer: can not set latency timer when it is already activated!\n");
    return false;
  }

  timer_length = milliseconds;
  activated = true;

  struct timeval start;
  gettimeofday(&start, NULL);
  starting_time_in_millisecond = (start.tv_sec) * 1000 + start.tv_usec/1000.0;

  return true;
}


// check whether the time-out has occured. If yes true will be returned, otherwise a false will be returned.
// when true is returned, the timer is off and it has to be set again for future use.
bool latency_timer::checkTimer(void)
{
  if(!activated)
    return false;

  // get current time;
  struct timeval current;
  gettimeofday(&current, NULL);
  cur_time_in_millisecond = (current.tv_sec) * 1000 + current.tv_usec/1000.0;

  if((cur_time_in_millisecond - starting_time_in_millisecond) > (unsigned long long)timer_length)
  {
    activated = false;
    return true;
  }

  return false;
}

