import time
import requests
import threading
import json
import os


NUM_POSTS = 77
URL_TEMPLATE = "https://jsonplaceholder.typicode.com/posts/{}"
OUTPUT_FILE = "posts.json"
FILE_LOCK = threading.Lock()

start_time = time.time()
print(f"Start time {start_time}")


def fetch_and_save_post(post_id, is_first, is_last):
    url = URL_TEMPLATE.format(post_id)
    try:
        response = requests.get(url)
        response.raise_for_status()
        post_data = response.json()


        with FILE_LOCK:
            with open(OUTPUT_FILE, "a") as f:
                if is_first:
                    f.write("[\n")
                json.dump(post_data, f, indent=4)
                if not is_last:
                    f.write(",\n")
                else:
                    f.write("\n]")

    except requests.RequestException as e:
        print(f"Failed to retrieve post {post_id}: {e}")



def main():

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    threads = []


    for i in range(1, NUM_POSTS + 1):
        is_first = (i == 1)
        is_last = (i == NUM_POSTS)
        thread = threading.Thread(target=fetch_and_save_post, args=(i, is_first, is_last))
        thread.start()
        threads.append(thread)


    for thread in threads:
        thread.join()

    print(f"Successfully saved {NUM_POSTS} posts to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

print(f"End time {time.time() - start_time}")
