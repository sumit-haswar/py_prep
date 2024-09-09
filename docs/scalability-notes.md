
scalability Harvard web development (https://www.youtube.com/watch?v=-W9F__D3oY4)
somehow distribute our inbound request over multiple web-servers
servers - ip address
     load balance has its own ip address
     key distinction between public and private ip addresses: rest of the world can't see private ip addresses
     resource based routing of requests to servers (image server, misc. files server, db server)
     DNS servers (host names to IPs and vice versa)

session recalls tend to be for specific machine, so load-balance breaks the session based architecture since they are per server

session based server can be used (but they introduce a single point of failure issue)

RAID0: stripping data across 2 hard-drives
RAID1: mirroring data
RAID10: both 1 and 0, so we get best of both ( 4 drives)
RAID5: multiple drives but only one used for redundancy
RAID6: any two drives can die

Sticky Sessions
     Shared Storage ?
          FC, iSCML, MySQL, NFC, etc.
     Cookies ?


Load Balancers
     software
          ELB, HAproxy, LVS
     hardware
          barracuda, cisco, citrix, f5

Caching
     .html
     MySQL Query Cache
     memcache is a memory cache (might or might not need cache refresh or LRU cache)
          connect to memcache
          get X from memcache
               if found:
                     return X
               if not found: 
                    connect to db, set X in memcache
                    return X

replication: master-slave (good topology for a website which is more read-heavy than write-heavy)
                master
          /          |          \
     slave     slave     slave

replication: master-master (better topology for both read-heavy and write-heavy)
          master <--> master
              |                   |
          slave            slave

sample web app topology (phase 1)
     
                                        {client network}
                                                  ||
                                        [load balancer]
          /                         |                         |                              \
[web servers]      [web servers]      [web servers]      [web servers] 
             \             |             /                                              ||
               \           |           / (read queries)                       || (write queries)
               [load balancer]                                        [db - MASTER]
          /                    |                    \                                   / (replication)
[db slave 1]     [db slave 2]     [db slave 3]


(phase 2) two load balancers through partitioning

               A-M cluster                                                            N-Z Cluster
              [load balancer]                                                    [load balancer]
          /                    |                    \ (read queries)             /                    |                         \ (read queries)
[db slave 1]     [db slave 2]     [db slave 3]               [db slave 1]     [db slave 2]     [db slave 3]

                                                     \                      |               / (replication)
                                                                     [db Master]

high availability 
                                   [load balancer]
                      /                                                \
              [master 1]  <---replication--->    [master 2]


problem statement: 1 or more web-servers, 1 or more databases, maybe some load-balancers 


				                                       {internet}
				                                              |
---------------------------only tcp 80, 443 traffic allowed, maybe other ports for VPN--------------------------------------------------------

                                   [load balancer] (inserts some kind of cookie to map user to server to have sticky sessions)
                              /                                   \     (tcp 80)
                    [web server 1]               [web server 2]
                                            \          /
                                      [load balancer 2] - - - (replication if required)
                         /      \                                      /      \     (tcp 3306)
                 [db server 1]  <--replication--> [db server 2]


perform load balancing at DNS Server level for geographical replication of data-centers 



