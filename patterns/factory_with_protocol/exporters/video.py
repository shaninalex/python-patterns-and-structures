import pathlib
from typing import Protocol


class VideoExporter(Protocol):
    def prepare_exporter(self, video_data):
        """Prepare video data for exporting."""

    def do_export(self, folder: pathlib.Path):
        """Export the video data to a folder."""


class LossLessVideoExporter:
    def prepare_exporter(self, video_data):
        return "Preparing video data for lossless export."

    def do_export(self, folder: pathlib.Path):
        return f"Exporting video data in lossless format to {folder}"


class H264BPVideoExporter:
    def prepare_exporter(self, video_data):
        return "Preparing video data for H.264 export."

    def do_export(self, folder: pathlib.Path):
        return f"Exporting video data in H.264 format to {folder}"


class H264Hi422BPVideoExporter:
    def prepare_exporter(self, video_data):
        return "Preparing video data for H.264 with Hi422 profile export."

    def do_export(self, folder: pathlib.Path):
        return f"Exporting video data in H.264 with Hi422 profile format to {folder}"

