https://www.youtube.com/watch?v=tQ2V9QSv48M

first check out: 
     https://developer.yahoo.com/performance/rules.html


while (not fixed){
     propose an architecture
     identify failures and bottlenecks
     identify downtime
     apply a better solution
}


concepts:
     scalability: number of users/sessions/trx/ operations the entire system can handel
     performance: optimal utilization of resources
     responsiveness: time taken per operation
     availability: probability of the app being available at any given point in time
     downtime impact: the impart of a downtime of a server/service/resource - number of users, type of impact etc.

Section 1
CAP Theorem: Consistency, Availability and Partition Tolerance (Cost, Quality and Time Triangle)

fallacies of distributed computing:
     network is reliable, latency is zero, bandwidth is infinite, network is secure, topology doesn't change, there is one administrator, transport cost is zero, network is homogenous, 


Section 2: Failed Architecture

App-server & DBServer

[                                                            ]
[                                                            ]
[  (App Server)      (Database Server) ]
[                                                            ]
[                                                            ]

throw more RAM and CPU - vertical scaling

Horizontal Scaling
                              load balance
[app server 1]     [app server 2] [app server 3]

                              [db server]

Unfortunate Solution
IE  ----------> [load balancer]
                    [web] [web] [web]
                                   ||
                                   V
                         [services][services][services]
                                                  ||
                                                  V
                                         [database]

Section 3: Less Scalable Solution
Sticky Sessions
               [user 1]
               [load balancer]
               
               [iis] [iis] [iis]

central session store
               [load balancer]        [
             [iis]     [iis]     [iis]      [ App Server
               [session store]         [

clustered session management (not bad for few requests)
               [load balancer]
          [iis]<-->[iis]<-->[iis]


Load Balanced App Server Cluster
                         [users]
     [load balancer]     [load balancer]          (active-passive or active-active)


Vertical Partitioning (Hardware)               Vertical == scaling up & horizontal == scaling out
          [load balancer] [load balancer]
         [iis] [iis] [iis]
               \|/
          [db server]          <-----> [SAN] (storage area network)


Horizontal Scaling (DB)        
          [load balancer] [load balancer]
         [iis] [iis] [iis]
               \|/
          [db server][db server][db server]  (db replica)        <-----> [SAN] (storage area network)

partitioning out becomes a huge problem when it comes to RDBMS (you loose ACID)


Vertical / Horizontal Scaling (DB) 
     [load balancer] [load balancer]
         [iis] [iis] [iis]
               \|/                              (db cluster)
          {[db server][db server][db server]}

Vertical / Horizontal Scaling (DB) 
          [App Cluster]
               /\
(db cluster 1) 0-1M users        (db cluster 2) 1-2M users
{twtr table, fb table}          {twtr table, fb table}


Step 7 - Vertical / Horizontal Partitioning (DB)

Separating Sets Diagram (35:00)


Caching

Add caches within App Server
     object cache
     session cache
     API cache
     page cache

Software
     Memcached
     Redis
     Azure Cache (App Fabric)

its important to have a policy regarding what not to cache

HTTP Accelerator
a good http accelerator / revers proxy performs the following - 
     - redirect static content request to a lighter HTTP server (lighttpd)

