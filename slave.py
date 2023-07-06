from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Get the hostname of the master process (rank 0)
master_hostname = MPI.Get_processor_name()
master_rank = 0

# Create a shared MPI communicator
master_comm = comm.Split(color=(rank == master_rank))

# Receive data from master process
data = master_comm.recv(source=master_rank, tag=1)

# Perform some task here
result = rank * 2  # Example task: Multiply rank by 2

# Send result to master process
master_comm.send(result, dest=master_rank, tag=2)
