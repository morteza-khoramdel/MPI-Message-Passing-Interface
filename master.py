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
