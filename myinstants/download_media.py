import requests
from tqdm import tqdm
def downloadMedia(link, destination):
     # Send a GET request to the URL
    response = requests.get(link, stream=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the total file size from the headers
        total_size = int(response.headers.get('content-length', 0))
        
        # Create a progress bar
        with open(destination, 'wb') as file, tqdm(
            desc=destination,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            leave=True
        ) as bar:
            # Iterate over the response data in chunks
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                bar.update(len(data))  # Update the progress bar
    else:
        print("Failed to download the file.")