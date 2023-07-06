from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Master process
    print("I am the master process.")
    data = {'message': 'Hello, slaves!'}

    for i in range(1, size):
        received_data = comm.recv(source=i)  # Receive data from a finished slave
        print("Received data from slave", received_data['rank'], ":", received_data['result'])

else:
    # Slave processes
    print("I am a slave process with rank", rank)
    data = None

data = comm.bcast(data, root=0)  # Broadcast data from master to all slaves

# Simulating some computation or task
result = rank * 2

# Send result and rank to the master
comm.send({'rank': rank, 'result': result}, dest=0)

print("Process", rank, "finished the task and sent the result:", result)
