
from watchdog.observers.polling import PollingObserver as Observer
from watchdog.events import FileSystemEventHandler
import time

from main import run_pipeline


class DataHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        file_path = event.src_path

        print(f"New dataset detected: {file_path}")

        if file_path.endswith((".csv", ".xlsx", ".json")):
            run_pipeline(file_path)

if __name__ == "__main__":

    path = "/app/data"

    event_handler = DataHandler()
    observer = Observer()

    observer.schedule(event_handler, path, recursive=False)

    observer.start()

    print("Watching for new datasets in /data folder...", flush=True)

    try:
        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()