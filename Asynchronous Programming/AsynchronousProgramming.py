import httpx
import asyncio
from typing import List

async def fetch_data(url: str) -> str:
    '''
        @desc:      Fetch data from a given URL using an asynchronous HTTP client.
        @param url: The URL to fetch data from.
        @returns:   The content of the URL as a string.
    '''
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text

async def fetch_multiple_urls(urls: List[str]) -> List[str]:
    '''
        @param:      A list of URLs to fetch data from.
        @desc:       Fetch data from multiple URLs concurrently.
        @returns:    A list of content fetched from each URL in the same order as input.
    '''
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

# Example usage
async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/users',
        'https://jsonplaceholder.typicode.com/users',
        'https://jsonplaceholder.typicode.com/users'
    ]
    data = await fetch_multiple_urls(urls)
    for idx, content in enumerate(data):
        print(f'Data from URL {urls[idx]}:\n{content}\n{'=' * 50}')

# Run the asynchronous function
if __name__ == '__main__':
    asyncio.run(main())
