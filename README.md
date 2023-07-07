# MPI Master-Slave Application

This repository contains an example application that demonstrates the use of MPI (Message Passing Interface) with a master-slave architecture. The application uses Docker and Docker Compose to set up multiple containers for running the MPI processes.

## Introduction to MPI

MPI (Message Passing Interface) is a standard communication protocol used for parallel computing. It allows multiple processes running on different machines to communicate and coordinate their tasks. MPI is widely used in scientific and high-performance computing applications.

MPI provides a rich set of communication primitives, such as point-to-point communication, collective operations, and data distribution. It allows for efficient data exchange and synchronization between processes, making it suitable for parallel computing tasks.

## Application Overview

The MPI Master-Slave Application in this repository demonstrates a simple master-slave architecture using MPI. The master process distributes a task to multiple slave processes, which perform the task in parallel. Once a slave process finishes its task, it sends the result back to the master.

The application includes two Python scripts:
- `master.py`: The script for the master process.
- `slave.py`: The script for the slave process.

The master process broadcasts the task data to all slave processes using MPI's `comm.bcast()` function. Each slave process performs the task, and when finished, it sends the result to the master process using `comm.send()`. The master process collects the results from all slaves using `comm.recv()`.

## Getting Started

To run the MPI Master-Slave Application, follow these steps:

1. Install Docker and Docker Compose on your system.
2. Clone this repository to your local machine.
3. Navigate to the repository directory.

4. Build the Docker image:
5. Start the application:

```
docker-compose exec --user mpirun --privileged mpi_head mpirun -n 2 python /home/mpirun/mpi4py_benchmarks/all_tests.py

```
This command starts the MPI application with one master process and two slave processes. Adjust the scaling factor (`2` in this case) to control the number of slave processes.

6. Observe the output in the terminal. You will see the execution of the master and slave processes, as well as the results returned by the slave processes to the master.

## Difference Between MPI and Multithreading

- **Communication Model:** MPI follows a message-passing model, where processes explicitly send and receive messages. On the other hand, multithreading uses shared memory for communication, and threads can access shared data structures directly.

- **Concurrent Execution:** In MPI, each process has its own address space and executes independently. Processes can be distributed across multiple machines. In multithreading, multiple threads share the same address space within a process and run concurrently on a single machine.

- **Scalability:** MPI is well-suited for distributed memory systems and can scale to a large number of processes running on different machines. Multithreading is typically used on shared memory systems and can efficiently utilize multiple cores within a single machine.

- **Complexity:** MPI requires explicit management of communication and synchronization between processes, which can be more complex. Multithreading can be simpler to implement, especially for shared memory systems, as it relies on implicit communication and synchronization through shared data.

It's important to choose the appropriate parallel programming model based on the characteristics of the problem, the available hardware, and the desired performance.

## License

This project is licensed under the [MBM License](LICENSE).
