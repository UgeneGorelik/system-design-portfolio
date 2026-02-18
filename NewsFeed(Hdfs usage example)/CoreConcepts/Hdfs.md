HDFS (Hadoop Distributed File System) Explained

HDFS is a distributed file system designed to store very large files reliably across many machines. It’s commonly used in big data systems for batch processing and analytics.

Key Features

Distributed Storage

Data is split into blocks (default 128 MB each).

Blocks are stored across multiple nodes in a cluster.

This allows parallel processing of huge files.

Replication for Fault Tolerance

Each block is replicated (default 3 copies) across different nodes.

If a node fails, data is still available on other nodes.

Ensures high reliability for critical data.

Write Once, Read Many

HDFS is optimized for append-heavy workloads.

You generally write a file once and then read it many times.

Ideal for logs, news posts, ETL batch processing, and analytics.

High Throughput

Optimized for large sequential reads/writes rather than small random access.

Perfect for processing huge datasets in batches, like news feeds.

Master/Slave Architecture

NameNode: Master node, keeps track of metadata (file names, block locations).

DataNodes: Worker nodes, store the actual data blocks.

How HDFS Fits in Your News Feed System

Storing Raw News Data

Posts (text + large bodies) are stored in HDFS.

This is your persistent, immutable storage layer.

ETL / Feed Preparation

ETL jobs read posts from HDFS, process them, and precompute feeds.

Ensures that the batch layer in Lambda architecture has access to all historical data.

Scalability

Can handle millions of posts per day because it stores data across many nodes.

Reliability

If a node storing some posts fails, replication ensures that no data is lost.

Integration

Works with distributed SQL and Redis cache:

HDFS stores raw posts

Metadata in distributed SQL

Precomputed feeds cached in Redis

Simple Analogy

Think of HDFS like a giant library:

Each book = a large file / post

Pages = blocks of the file

Multiple copies of each page are kept in different rooms (replication)

Librarian (NameNode) keeps index of all books and pages

Readers (ETL jobs) can read many books in parallel