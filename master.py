from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Master process
    print("I am the master process.")
    data = {'message': 'Hello, slaves!'}

    # Send data to slave processes
    for i in range(1, size):
        comm.send(data, dest=i)

    # Receive results from slave processes
    results = []
    for i in range(1, size):
        result = comm.recv(source=i)
        results.append(result)

    print("Results:", results)
else:
    # Slave processes
    print("I am a slave process with rank", rank)

    # Receive data from master process
    data = comm.recv(source=0)

    # Perform some task here
    result = rank * 2  # Example task: Multiply rank by 2

    # Send result to master process
    comm.send(result, dest=0)
