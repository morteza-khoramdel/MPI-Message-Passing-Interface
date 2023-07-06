from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Perform some task here
result = rank * 2  # Example task: Multiply rank by 2

# Send result to master process
comm.send(result, dest=0)

# Receive data from master process
data = comm.recv(source=0)

# Perform some task using the received data
processed_data = data['message'] + ' Slave ' + str(rank)

# Send processed data back to master process
comm.send(processed_data, dest=0)
