import argparse
import os

from ffprobe import FFProbe



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
    metadata = FFProbe(self.filepath)
    for stream in metadata.streams:
      if stream.is_video():
        return stream.duration_seconds()
    return 0

if __name__ == "__main__":
    my_args = parser.parse_args()
    metadata_processor = MetadataProcessor(my_args.filepath)
    metadata_processor.process()
