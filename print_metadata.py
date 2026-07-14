import argparse
import json
import os
import subprocess

parser = argparse.ArgumentParser(description='Get Podcast Metadata')
parser.add_argument('filepath',
                    help='Path to the file')

class MetadataProcessor():

  def __init__(self, filepath):
    self.filepath = filepath

  def process(self):
    file_size = self.get_file_size()
    podcast_duration = self.get_audio_length()
    print(f"podcast_bytes: {file_size}")
    print(f"podcast_duration: {podcast_duration}")

  def get_file_size(self):
      file_stats = os.stat(self.filepath)
      return file_stats.st_size

  def get_audio_length(self):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "json", self.filepath],
        capture_output=True, text=True, check=True)
    metadata = json.loads(result.stdout)
    return float(metadata["format"]["duration"])

if __name__ == "__main__":
    my_args = parser.parse_args()
    metadata_processor = MetadataProcessor(my_args.filepath)
    metadata_processor.process()
