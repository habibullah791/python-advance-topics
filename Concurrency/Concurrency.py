import multiprocessing

# Define a CPU-bound function to be parallelized
def count_iterations(number):
    result = 0
    for _ in range(number):
        result += 1
    return result

if __name__ == "__main__":
    
    # number of the process we want to create
    num_processes = 4
    
    results = []
    
    # Create a multiprocessing pool, for num_process in this case 4
    pool = multiprocessing.Pool(processes=num_processes)
    
    # Define the number of iterations for each process
    iterations_per_process = 1000000
    
    # Run the tasks in parallel
    for _ in range(num_processes):
        result = pool.apply_async(count_iterations, args=(iterations_per_process,))
        results.append(result)
    
    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()
    
    # Retrieve the results from each process
    final_results = [result.get() for result in results]
    
    # Print the final results
    print("Final Results:", final_results)
