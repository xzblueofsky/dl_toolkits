#pragma once
#include <time.h>

//-----------------------------------------------------------------------------
// latency_timer is a timer to simulate a latency. 
// when timer is set (with a delay in milliseconds), 
// everytime you check it, it will tell you whether it has passed the latency.

class latency_timer {

  public:
    latency_timer();
    ~latency_timer();
    
    // calibrate floor coordinate system from at least 3 points on a same plane which is parrallel to floor plane
    bool setTimer(int milliseconds);
    bool checkTimer(void);

private:
    int timer_length; // in milliseconds
    unsigned long long starting_time_in_millisecond;
    unsigned long long cur_time_in_millisecond;
    bool activated;

};