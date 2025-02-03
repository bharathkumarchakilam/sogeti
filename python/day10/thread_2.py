import threading

def sum_chunk(chunk, results, index):
    results[index] = sum(chunk)

def split_data(data, num_chunks):
    chunk_size = len(data) // num_chunks
    return [data[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)] + [data[num_chunks * chunk_size:]] if len(data) % num_chunks else []

def main():
    data = list(range(1, 25000)) 
    num_threads = 5  
    chunks = split_data(data, num_threads)

    threads = []
    results = [0] * len(chunks)  

    for i, chunk in enumerate(chunks):
        if chunk: 
            thread = threading.Thread(target=sum_chunk, args=(chunk, results, i))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    total_sum = sum(results)
    print(f"Total Sum: {total_sum}")

main()
