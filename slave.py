import subprocess
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = comm.bcast(None, root=0)  # Receive broadcasted data from the master

websites = ["www.example.com", "www.google.com"]

ping_results = []
for website in websites:
    # Ping the website and capture the result
    result = subprocess.run(["ping", "-c", "4", website], capture_output=True, text=True)
    ping_results.append(result.stdout)

# Send the ping results to the master
comm.send({'rank': rank, 'ping_results': ping_results}, dest=0)

print("Slave process with rank", rank, "finished the task and sent the ping results.")
