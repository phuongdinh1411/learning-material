# Table of Contents

- [NETWORKING](#networking)
- [OPERATING SYSTEM](#operating-system)
- [DATABASE](#database)
- [SECURITY](#security)

## NETWORKING

1. Read the concept of TCP in [this wiki page](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) and try to understand all the concepts of it (deeply):
    - How TCP open a connection? what does it need to open a connection?
        + Why there are 3 way handshakes but not 2 way?
            Handshakes is process to exchange sequence number. And actuality though, the middle two events (#2 and #3) happen in the same packet. What makes a packet a SYN or ACK is simply a binary flag turned on or off inside each TCP header, so there is nothing preventing both of these flags from being enabled on the same packet. So the three-way handshake ends up being:
            Alice ---> Bob    SYNchronize with my Initial Sequence Number of X
            Alice <--- Bob    I received your syn, I ACKnowledge that I am ready for [X+1]
            Alice <--- Bob    SYNchronize with my Initial Sequence Number of Y
            Alice ---> Bob    I received your syn, I ACKnowledge that I am ready for [Y+1]
        + What is syn, ack mean?
        + Why they have to send 2 "random" sequence numbers? The purpose of this sequence number?
            The use of sequence and acknowledgment numbers allows both sides to detect missing or out-of-order segments
        + What if the 3rd handshake fail? How the server can detect it and what does it do in this case?
    - How TCP handles the connection?
        + What happens if some bits are wrong due to connection errors? How to detect them and fix them?
        + How the timeout is handled? what if the timeout is expired?
        + What will happen if some "packet" is missing on the way?
        + How to detect the appropriate number of packets to send (speed of sending packet)?
    - How TCP close the connection?
        The connection termination phase uses a four-way handshake, with each side of the connection terminating independently. 
        It is also possible to terminate the connection by a 3-way handshake, when host A sends a FIN and host B replies with a FIN & ACK (combining two steps into one) and host A replies with an ACK
        + What if the internet is dropped in the middle of the connection? Or in case one peer is crash?
    - How long you can keep a TCP connection alive?

2. What are the differences between TCP and UDP? And in which case we use which?
    https://www.geeksforgeeks.org/differences-between-tcp-and-udp/
    - Features of TCP
        + TCP keeps track of the segments being transmitted or received by assigning numbers to every single one of them.
        + Flow control limits the rate at which a sender transfers data. This is done to ensure reliable delivery.
        + TCP implements an error control mechanism for reliable data transfer.
        + TCP takes into account the level of congestion in the network.
    - Advantages of TCP
        + It is reliable for maintaining a connection between Sender and Receiver.
        + It is responsible for sending data in a particular sequence.
        + Its operations are not dependent on OS.
        + It allows and supports many routing protocols.
        + It can reduce the speed of data based on the speed of the receiver.
    - Disadvantages of TCP
        + It is slower than UDP and it takes more bandwidth.
        + Slower upon starting of transfer of a file.
        + Not suitable for LAN and PAN Networks.
        + It does not have a multicast or broadcast category.
        + It does not load the whole page if a single data of the page is missing.

    - Features of UDP
        + Used for simple request-response communication when the size of data is less and hence there is lesser concern about flow and error control.
        + It is a suitable protocol for multicasting as UDP supports packet switching.
        + UDP is used for some routing update protocols like RIP(Routing Information Protocol).
        + Normally used for real-time applications which can not tolerate uneven delays between sections of a received message.
    - Advantages of UDP
        + It does not require any connection for sending or receiving data.
        + Broadcast and Multicast are available in UDP.
        + UDP can operate on a large range of networks.
        + UDP has live and real-time data.
        + UDP can deliver data if all the components of the data are not complete.
    - Disadvantages of UDP
        + We can not have any way to acknowledge the successful transfer of data.
        + UDP cannot have the mechanism to track the sequence of data.
        + UDP is connectionless, and due to this, it is unreliable to transfer data.
        + In case of a Collision, UDP packets are dropped by Routers in comparison to TCP.
        + UDP can drop packets in case of detection of errors.

3. How Ping command works? What is TTL?? How does TTL will be changed??
    - Ping works by sending an Internet Control Message Protocol (ICMP) Echo Request to a specified interface on the network and waiting for a reply. When a ping command is issued, a ping signal is sent to a specified address. When the target host receives the echo request, it responds by sending an echo reply packet.

    - This approach serves two specific purposes: verifying that the target host is available and determining round-trip time (RTT) or latency.

4. How HTTP works?
    - How does HTTP work? As a request-response protocol, HTTP gives users a way to interact with web resources such as HTML files by transmitting hypertext messages between clients and servers. HTTP clients generally use Transmission Control Protocol (TCP) connections to communicate with servers.

    - Why did people say that HTTP is stateless? The reason they make it stateless?
    The HTTP protocol is a stateless one. This means that every HTTP request the server receives is independent and does not relate to requests that came prior to it. For example, imagine the following scenario: a request is made for the first ten user records, then another request is made for the next ten records.


    - Can we make a persistent HTTP connection? pros and cons of this way?
        If the client does not close the connection when all of the data it needs has been received, the resources needed to keep the connection open on the server will be unavailable for other clients. How much this affects the server's availability and how long the resources are unavailable depend on the server's architecture and configuration.


    - Why HTTP require cookie each time we send the request?
    - Can someone use your cookie and log in your Facebook account? How to migrate this?
    - What is HTTP session? How does authentication work in HTTP? What is JWT?
        HTTP sessions is an industry standard feature that allows Web servers to maintain user identity and to store user-specific data during multiple request/response interactions between a client application and a Web application.

    - Which type of "data" HTTP can help us to get or push? (binary file? image? text file? video file? music file?)
    - REST/RESTful?
    - AJAX technique?
    - How HTTPs work?
    - Learn about some useful headers.

5. When you type "google.com" into your browser, that will happen when you type enter till everything is displayed on your screen?
    - DNS lookup (in case you already access google.com before and also in case you do not know the IP of google.com)
        + Which protocol DNS use and why?
            DNS queries consist of a single UDP request from the client followed by a single UDP reply from the server
        + The other of place to look up DNS.
    - TCP or UDP will be used in this case? why?
    - How to know "google.com" require HTTP or https? how browser can know and redirect from HTTP to HTTps?
    - After you get the `HTML content` for "google.com" how to get the `*.js` and `image` files?
    - When getting `*.js` or `image` files do why use another `TCP connection` or use the same one as in the get `HTML content`? How DNS lookup work in this case?
    - After your browser display "google.com" fully, is there any connection open?
    - Caching can apply to which steps? How caching applied?

6. What is the connection pool? It's advantages and disadvantages? How to implement connection pool in your programing language?

7. What is socket?
    - Why do we need socket? Why socket is a "file" in linux?
    - What is `src port` when you create a connection to a "server"?
    - What one server can handle multiple connections to the same port? [Good answers here but read all answers](https://stackoverflow.com/questions/3329641/how-do-multiple-clients-connect-simultaneously-to-one-port-say-80-on-a-server)
    - What is the maximum number of connections a server can handle? (if it has unlimited resource) (in case of the same client and in case of multiple clients)
    - When you open multiple tabs on your chrome, how OS knows which packet (both sending and receiving) correspond to which tab? (how about in case you open many tabs to the same page "for eg: google.com")
    - What are the maximum numbers of connection your machine can connect to "google.com" (if you have unlimited resource)
    - Can two processes listen to the same port on your machine? Why? How?
        yes, with different protocol
    - What is `buffer`? why we always need buffer when working with "file"?
    - What is `unix socket`? When to use it?

8. What is `TCP proxy`? `reverse proxy`? and `VPN`?
    - How your router at your home works?
        + Inside LAN network, it uses IP or MAC address? Why?
        + How does it know which packet comes from (or arrive at) which machine?
        + What is the difference between Hub and Switch inside LAN?
        + How src IP/PORT and dst IP/PORT change on the way to the server?
    - How `load-balancer` works? (this one is a tough question) // hint: it opposite to how to router work. 
        + When we send a packet to a `load-balancer` how does it forward to the desired server? (Does it keep any data on its memory?)
        + When the server wants to send data back to the client, does the connection need to go through the `load-balancer`? 
        + What is different between `reverse proxy` and `load-balancer`?
        + Can `load-balancer` be a bottleneck? (Because it is the end-point of too many requests) (bottleneck about RAM or CPU or Network?)
        + Try to understand everything in [this page](https://softwareengineering.stackexchange.com/questions/312956/what-does-a-load-balancer-return) (all the answers)

## OPERATING SYSTEM

1. What is `process`, `thread`? What are the differents between them?
    - What data `process`, `thread` need to live? Why they said that `Thread is a lightweight process`?
        + A process has a virtual address space, executable code, open handles to system objects, a security context, a unique process identifier, environment variables, a priority class, minimum and maximum working set sizes, and at least one thread of execution. Each process is started with a single thread, often called the primary thread, but can create additional threads from any of its threads.

        + A thread is an entity within a process that can be scheduled for execution. All threads of a process share its virtual address space and system resources. In addition, each thread maintains exception handlers, a scheduling priority, thread local storage, a unique thread identifier, and a set of structures the system will use to save the thread context until it is scheduled. The thread context includes the thread's set of machine registers, the kernel stack, a thread environment block, and a user stack in the address space of the thread's process. Threads can also have their own security context, which can be used for impersonating clients.

        + Some people call threads lightweight processes because they have their own stack but can access shared data. Since threads share the same address space as the process and other threads within the process, it is easy to communicate between the threads.

    - How CPU switch (context switch) between `processes`/threads`? How data is to ensure safety? (in case single CPU core and multiple CPU cores)
        + Process-related information is stored in something called PCB(Process control block). Generally, process id, process number, process state, program counter, registers, and opened files are stored in PCB. This PCB is stored in a protected memory area to avoid normal user access as it contains critical information.

        + First, thes context switching needs to save the state of process P1 in the form of the program counter and the registers to the PCB (Program Counter Block), which is in the running state.
        + Now update PCB1 to process P1 and moves the process to the appropriate queue, such as the ready queue, I/O queue and waiting queue.
        + After that, another process gets into the running state, or we can select a new process from the ready state, which is to be executed, or the process has a high priority to execute its task.
        + Now, we have to update the PCB (Process Control Block) for the selected process P2. It includes switching the process state from ready to running state or from another state like blocked, exit, or suspend.
        + If the CPU already executes process P2, we need to get the status of process P2 to resume its execution at the same time point where the system interrupt occurs.

    - What is `multi-process` and `multi-thread`? When we should you which one?
        https://www.geeksforgeeks.org/difference-between-multiprocessing-and-multithreading/
        + Process has how many states? How does it change between each state?
        + Scheduling algorithm.
        + What will happen if a process is `waiting`? Or a thread is `sleeping`?
        + How CPU detects that a thread is `sleeping`? Or detect when it wants to run?
    - What is `thread-pool`? How to use it? Describe how to create a `thread-pool` in your programming language
        A thread pool is a group of pre-instantiated, idle threads which stand ready to be given work

    - Virtual memory ?

    - Can 2 different processes access or change data of each other `address space`? (this question may make you confuse with your knowledge about `virtual memory`)
        + Can 2 processes use the same library (for eg: libc is required to every process)? How?
        + How does `debugger` work? How it can attach to a running process and change data of that process? (so cool, right?)
    - How 2 processes can communicate with each other? (There are a lot of ways but focus on the OS's way)
        There are two modes through which processes can communicate with each other – shared memory and message passing. As the name suggests, the shared memory region shares a shared memory between the processes. On the other hand, the message passing lets processes exchange information through messages

    - What is `child-process`? How to create a `child-process`?
        + What data a `child-process` have when we create it?
        + Can it read/write data on it's `parent process`? No, each process has its own memory space
        + What is `copy on write (COW)`? **(this concept is important to understand OS)** // if you love computer security like me you can read more about `Dirty COW`, it's fabulous
        + What will happen when `child-process` changes a variable of `parent process`?
        + If `file descriptor` also be `inherited` by the `child process`. What if 2 processes can handle a same `file descriptor` or even a same `socket`? can refer [here](https://www.cs.ait.ac.th/~on/O/oreilly/perl/cookbook/ch17_10.htm)

2. `Concurrency` vs `Parallels`? (in case single CPU core and multiple CPU cores)
    - What is `critical zone`? 
    - What is `race condition` and how to handle this case?
    - What is locking mechanism? `mutex`? `semaphore`? `spinlock`? `read lock` vs `write lock`?
    - What is `deadlock` and how to avoid `deadlock`?

3. How does memory is managed in the OS?
    - What is `virtual memory`? Why do we need it? How does it work?
        + How large `virtual memory` is?
        + What is `paging`?
        + Can 2 processes map to the same `physical address`? How and in which case?
            Usually, each process gets its own page table, so any address it uses is mapped to a unique frame in physical memory. But what if the operating system points two page table-entries to the same frame? This means that this frame will be shared; and any changes that one process makes will be visible to the other.

            You can see now how threads are implemented. In Section 4.3.1, clone we said that the Linux clone() function could share as much or as little of a new process with the old process as it required. If a process calls clone() to create a new process, but requests that the two processes share the same page table, then you effectively have a thread as both processes see the same underlying physical memory.

            You can also see now how copy on write is done. If you set the permissions of a page to be read-only, when a process tries to write to the page the operating system will be notified. If it knows that this page is a copy-on-write page, then it needs to make a new copy of the page in system memory and point the page in the page table to this new page. This can then have its attributes updated to have write permissions and the process has its own unique copy of the page.
    
    - What is `heap space` and `stack space`?
    - What will happen with memory when you open an application?
    - What will happen you call another function (with parameters) or return from a function? 
        + What will happen with stack? (why we do not use heap here?)? 
        + What will happen with registors?
    
    - What causes stack-over-flow? Recursion and Large local variables
 
    - What is dynamic allocating? How does it work? 
        + How does deallocation work?
        + What happens when your computer is full of memory?
    - Why you do not need to "deallocate" local variable?
    - How does `Garbage Collection` work? When it will be triggered?
    - What is a pointer? What difference between `pass by value` and `pass by reference`?
    - Where `global variable` will be saved?

4. Why in Linux `everything is "file"`?
    - How does mouse/keyboard/monitor..... communicate with your computer?
    - What is `file descriptor`?
    - What is `buffer`? Why do we need `buffer`?
    - What will happen if 2 processes read/write to the same file?

5. What is `system call (syscal)`?
    - How to do a `syscal`?
    - What happens with CPU when we execute a `syscal`?
    - What is `user space` and `kernel space`?


6. Caching:
    - What is in-memory cache? (memcached/redis)
    - LRU? implement LRU in your program language! (How about multi-thread?)
    - How to migrate `Cache stampede`?
        https://viblo.asia/p/cache-stampede-cau-chuyen-dan-tho-AZoJjYwO4Y7


- Good resources:
    * [Overview of OS syntax, try do dive deeper to each concept](https://medium.com/cracking-the-data-science-interview/the-10-operating-system-concepts-software-developers-need-to-remember-480d0734d710)


## DATABASE

1. Compare `Relational DB (SQL)` vs `NoSQL`. It's also really nice to know about `newSQL` (a kind of auto sharding DB which support `SQL stuff` but scale like `NoSQL`) 
    - How these 2 things can scale up?
    - How Transaction is handled? 
    - `ACID` of `SQL` and `BASE` of `NoSQL`? Why `NoSQL` is `eventual consistency`?
    - `CAP` theorem in this case. [This is a so nice graph](http://blog.nahurst.com/visual-guide-to-nosql-systems)

2. What is `parameterized statement` (in Java it's `prepared statement`)? How does it work **internally**?
    - What is `SQL injection`? how to avoid it?
    - How many "requests" you have to send to `Database` in a single `prepared statement` query? // one for compile and one for execute
    - Can you reuse the `compiled` query multiple times? (does it help to speed up your application?)

3. How `indexing` works internally?
    - What algorithm and data structure `indexing` used? And why?
        b-tree, hash table, r-tree, bitmap
    - How `composite indexing` works?
    - How to know your query is using index?
     Write "explain " in front of your query. The result will tell you which indexes might be used

     How does a database know when to use an index? When a query like “SELECT * FROM Employee WHERE Employee_Name = ‘Abc’ ” is run, the database will check to see if there is an index on the column(s) being queried. Assuming the Employee_Name column does have an index created on it, the database will have to decide whether it actually makes sense to use the index to find the values being searched – because there are some scenarios where it is actually less efficient to use the database index, and more efficient just to scan the entire table.

    - How index work in this case: `WHERE age = 5` and `Where age > 5`? The complexity to go to the next record?
    - Indexing with char?

4. The complexity of SQL query? How to measure it? How SQL optimize a query?
    - Complexity of this query `SELECT * FROM abc ORDER BY name LIMIT 10 OFFSET 1000000` // SELECT 10 record from offset 10^6 after sort by name (which is a char)? How to optimize it?
        BigO(1000000)
        faster: select * from big_table WHERE id < 10 ORDER BY id DESC LIMIT 1;

    - What is the complexity of `COUNT(*)` query?
    - How to write query to avoid full table scan?
    - Complexity of `JOIN`, `INNER JOIN`, `OUTTER JOIN`?
        + A nested join is a join that compares every record in one table against every record in the other. The complexity is O(MN).
            This join is efficient when one or both of the tables are extremely small (e.g. < 10 records), which is a very common situation when evaluating queries because some subqueries are written to return only one row.
            Joins that are not equi-joins* frequently have to do a nested join to evaluate all possible pairs of records, and frequently have result sets of size O(MN) anyway, so then this complexity isn't even bad.
            Cross-joins are explicitly asking to take every pair of records, and therefore would use this algorithm.

        + A hash join has expected complexity O(M + N), but has unfavorable memory access patterns (random disk access is really bad). It can be really good when one or both the tables is small enough to fit into memory.

        + Merge joins are based on having both tables be sorted according to the keys being joined on, and then doing a O(M+N) merge-like step to determine the matching records.
            If both tables have an index on the joined columns, then the index already maintains those columns in order and there's no need to sort. The complexity will be O(M + N).
            If neither table has an index on the joined columns, a sort of both tables will need to happen first, so the complexity will look more like O(M log M + N log N). If the tables are large enough that they don't fit into memory, at least the data access patterns on the disk will be favorable to paging.
            If only one of the tables has an index on the joined columns, only the one table that doesn't have the index will need to be sorted before the merge step can happen, so the complexity will look like O(M + N log N).
            The term "index join" is confusing. Oracle uses this term to refer to a procedure of doing a hash join over indexes to optimize some queries that don't have joins in them at all! However, I think the more typical usage is another join algorithm that is often used by database engines. If one of the tables is fairly small, but the other is large and already has an index on the join columns, then each entry in the small table may be looked up (via an index seek) in the large table. This requires O(M * log N) time if N is the size of the large table. This join can be advantageous because N appears in the complexity only with a log factor in front of it.

5. What is Database Replicating? When we need it?
    - What is `bin log`? How `Master DB` sync with `Slave DB`?
    - Can a `Slave DB` be a slave of another `Slave DB` (we do not need to sync from `Master DB` directly)?

6. What is Database Sharding? When we need it?
    - Which rule we can apply to DB Sharding?
    - How to ensure `primary key` is globally unique when sharding?
    - How we can shard a table to multiple tables (same server) and multiple DB (multiple servers)?
    - How query can work when we sharding? for example query but the data is in different tables/dbs?

7. What is database transaction?
    - How `rollback` works internally?
    - `ACID`? What is `dirty read`?
    - How transaction work when there are many concurrent requests?
    - How to avoid `race condition` in DB? `Read/Write` lock?
    - `Distributed transaction`? How to make a transaction when a query needs to access multiple DB?


## SECURITY

1. Hash vs Encrypt vs Encode
    - Are there any way we can crack `Hash`
    - symmetric vs asymmetric encryption? AES vs RSA?
    - Fast Hash vs Slow Hash?
    - When we use Encode??
    - What is the perfect hash function?
    - What is the load factor of hashing?

2. SSL/TLS
    - How to verify a certificate? How many kinds of certificates are there?
    - What is CA? how to verify certificate of a CA?
    - What is `public`/`private` key? what is symmetric `key`
    - What is digital signature? What is `HMAC`?

3. How to store credential information efficiency? (user password, config key, database credential, user information, secret key,.... )

4. Describe a way to defense DDOS? (actually, there are many kinds of DDOS not just network or memory, so this question is pretty complicated)
