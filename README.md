This Python project fetches 77 posts from a public API using multithreading to speed up the process.
The fetched data is written directly into a posts.json file in a valid JSON format.
Each post is written to the file in a thread-safe manner as soon as it's fetched, ensuring low memory usage.

Features
Retrieves 77 posts concurrently from https://jsonplaceholder.typicode.com.
Uses threading to improve performance and reduce latency.
Ensures valid JSON output.
Thread-safe file writing to prevent race conditions.
JSON data is saved to posts.json file in a valid JSON array format.
