# hedera-ryu

Hedera experiment revamped to OpenFlow 1.3

The code of this experiment is based on 
https://github.com/strategist333/hedera

The description of the experiment can be found here
https://reproducingnetworkresearch.wordpress.com/2012/06/06/hedera/

## Running the experiment

There are two possibilities to run the experiment, using Mininet as in the original code or using

### Mininet

To run the experiment you need to install Mininet with Open vSwitch (OVS). This code was tested with version 2.3.0. It is recommended to use an OVS version that negotiates the OpenFlow version of the controller application (e.g 2.0.2).

    $ git clone https://github.com/mininet/mininet.git
    $ sudo ./mininet/util/install.sh -nV 2.0.2

To start the experiments run test.sh

    $ sudo ./test.sh <num_trials> <duration>
  
The number of trials defines how many times each experiment will be run and the duration specifies the amount of time for all cases. The total time to execute all experiments is machine dependant, so it is recommendable to run a short test to run only each experiment, only once, for 30 seconds.  

    $ sudo ./test.sh 1 30

### Horse
**TBD**


