from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Get the master container name from the command line argument
master_container_name = sys.argv[1]

# Get the rank of the master process (which is 0)
master_rank = 0

# Perform some task here
result = rank * 2  # Example task: Multiply rank by 2

# Send result to the master process
comm.send(result, dest=master_rank)

# Receive data from the master process
data = comm.recv(source=master_rank)

# Perform some task using the received data
processed_data = data['message'] + ' Slave ' + str(rank)

# Send processed data back to the master process
comm.send(processed_data, dest=master_rank)
