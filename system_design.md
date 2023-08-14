# payment system
    - https://newsletter.pragmaticengineer.com/p/designing-a-payment-system
    - noticable points:
        + 

# Digital wallet
    - Distributed transaction
        - BASE:
            Basic Availability
            Soft state
            Eventual consistency
        - Partially follow ACID:
            - Atomicity: strict compliance
            - Consistency: Consistency after the transaction is completed is strictly followed; consistency in the transaction can be relaxed appropriately
            - Isolation: no influence between parallel transactions; visibility of intermediate results of transactions is allowed to be relaxed in a safe manner
            - Persistence: Strictly followed
        - 2PC
        - TC/C
            - better lantency than Saga, because it can exeture in any order
        - Saga: linear order
            - Choreography
            - Orchestration
        - Event sourcing:
            - mmap
        
# hotel management system
    - concurrency
        - one user re-submit
            - use itempotent id
        - double booking: https://medium.com/@abhishekranjandev/concurrency-conundrum-in-booking-systems-2e53dc717e8c
            - locking mananism: 
                - pessimistics: lock record and perform
                - optimistics: use versioning, will check again when at booking step
                - db constraint


# Distributed search system
    - 1 st: id-> document -> traverse all docs
    - inverted-index: term -> ([doc], [freq], [[loc])
        - come with costs of storage, maintainance
    - Document partition vs Term partition
    - The cluster manager splits the input document set into N number of partitions

# Search autocomplete system
    - Gather đata: run as background and update the Trie
        - Trie DB:
            - key: prefix - value: word and its freq
    - Scale:
        - split by first/two character, but imbalance happens
            - can split by place some char at same node
# Chat system
    - http: client initiated request
    - what about server initiated:
        - pooling: inefficient
        - long pooling:
            - sender and reciver may not connect to same server
            - user not chat frequently -> waste of resource
            - server has no good way to tell if a client is disconnected
        - web socket: most common way to send msg from server to client
            - it is also initiated by client
            - bi-directional
            - stateful: because clients have to maintain a persistent connection to chat server
            - scale:
                - multi server: -> need service discovery -> zookeeper
    - data model:
        - message in group: how to order ?
    - sync between devices:
        - each device has curr_max_msg_id
    - on/offline management:
        - if the group has many member, each status changes need to be broacasted to all member -> expensive -> lazy load

# New feed system
    - Post svc, Fanout svc, Notification svc
    - Two main flows: feed publishing and news feed building
    - Fanout svc: get friends ids -> friends 's info -> send friend list and new post id to queue -> consumer
        - on-write: feeds are delivered to friends immediately -> but it is slow and can have problem if hot idol, waste resource for idle user 
        - on-read: can be slower than on-write
    - New feeds retrieval: newfeed svc -> cache -> list of post id -> fetch info

# Notification system

# Web crawler
    - seed Url -> url frontier -> html downloader -> parser -> link -> db
    - url frontier: to be downloaded vs dowloaded
        - select url and push them to queue, all link in same domains must to the same queue.
        - storage: 100 miliions of url
    - content parser: malformed web pages
    - content seen ?
    - Robot Exclusion Protocol: standard used by websites to communicate with crawlers. it specifies what pages crawlers are allowed to download


# Youtube
    - upload and stream flow
        - upload:
            - metadata:
            - video content
            - transcode
            - CDN
        - streaming protocol: different protocol support different format and playback player
        - codec: reduce size video size but preserve the video quality (i.e H264)
        - DAG scheduler for different video tasks
        - Optimization:
            - parallelize uploading: split by Group of picture
            - presigned url


# Key value
    - CAP
    - Distributed partition:
        - evenly
        - minimize data movement
    - Virtual node
    - Write/Read quorum: W/R
        - R = 1, W = N: optimize for read
        - R = N, W = 1: optimize for write
        - R + W > : strong consistency
    - Inconsistency resolution: versioning
    - Gossip protocol: to detect failure
        - each node has membership list (id and heartbeat counters)
    - Failure:
        - Temporary:
            - sloppy quorum: first W healthy server for write, first R heathy servers for read 
            - hinted handoff: stand by
        - Permanent:
            - anti-entropy protocol to keep replica in sync
    - Write path (cassandra): commit log(disk) -> memory cache -> SStables(disk)
    - Read path: read from memory cache -> if miss, read from SSTables:
        - efficient way to find out which SSTables contain the key : bloom filter

# Consistent Hashing
    - when hash table is re-sized: only k/n keys need to be remapped (k : all keys, n: n number of slots)
    - number of virtual node belongs to single physical nodes


# caching
    read intensive application
        Cache-aside: miss cache -> db -> save cache
        Cache-through: cache read DB to prefetch data -> return to app
        Refresh-ahead
    write intensive application
        Write-Through: cache as main db
        Write-behind: same as write -though but asynchonously write to db
    Write-around: write to db -> cache    

# connection
https://blog.bytebytego.com/p/network-protocols-behind-server-push?utm_source=post-email-title&publication_id=817132&post_id=135305890&isFreemail=true&utm_medium=email


# java garbage collection
https://www.freecodecamp.org/news/garbage-collection-in-java-what-is-gc-and-how-it-works-in-the-jvm/

# db transaction isolation
- Symptoms:
    - dirty read: read uncommited data from other txn
    - non repeatable read: 2 read returns different value, data is commited by other txn
    - phantom read: same as non-repeatable but happen for range of data
    - write skew: contrainst : a + b =200- >both txn a and b read then txn write a, txn write b 
- Isolation level:
    - read uncommited
    - read commited : either read or write lock
    - repeatable Read : read locks on all rows it references and writes locks on all rows it inserts, updates, or deletes. 
    - serializable: lock the whole table
    - Snapshot Isolation: multi versions

