from os import walk
from abc import ABC, abstractmethod
import pathlib


class VideoExporter(ABC):
    """Basic representation of video exporting codec."""

    @abstractmethod
    def prepare_exporter(self, video_data):
        """Prepare video data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Export the video data to a folder."""


class LossLessVideoExporter(VideoExporter):
    """LossLess Video Exporter codec."""

    def prepare_exporter(self, video_data):
        return "Preparing video data for lossless export."

    def do_export(self, folder: pathlib.Path):
        return f"Exporting video data in lossless format to {folder}"


class H264BPVideoExporter(VideoExporter):
    """H.264 Video Exporter codec."""

    def prepare_exporter(self, video_data):
        return "Preparing video data for H.264 export."

    def do_export(self, folder: pathlib.Path):
        return f"Exporting video data in H.264 format to {folder}"


class H264Hi422BPVideoExporter(VideoExporter):
    """H.264 Video Exporter codec with Hi422 profile"""

    def prepare_exporter(self, video_data):
        return "Preparing video data for H.264 with Hi422 profile export."

    def do_export(self, folder: pathlib.Path):
        return f"Exporting video data in H.264 with Hi422 profile format to {folder}"


class AudioExporter(ABC):
    """Basic representation of audio exporting codec."""

    @abstractmethod
    def prepare_audio(self, audio_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""


class AACAudioExporter(AudioExporter):
    def prepare_audio(self, audio_data):
        return "Preparing audio data for AAC export."

    def do_export(self, folder: pathlib.Path):
        return f"Exporting audio data in AAC format to {folder}"


class WAVAudioExporter(AudioExporter):
    def prepare_audio(self, audio_data):
        return "Preparing audio data for WAV export."

    def do_export(self, folder: pathlib.Path):
        return f"Exporting audio data in WAV format to {folder}"


class ExporterFactory(ABC):
    """The factory does not maintain any of the instances it creates."""

    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """returns a new video exporter instance."""

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        """returns a new audio exporter instance."""


class FastExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return LossLessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def read_exporter() -> ExporterFactory:
    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter(),
    }
    export_quality: str
    while True:
        export_quality = input("Enter output quality (low, high, master): ")
        if export_quality in {"low", "high", "master"}:
            return factories[export_quality]
        print(f"Unknow quality level: {export_quality}")


def main() -> None:
    fac = read_exporter()

    video_exporter: VideoExporter = fac.get_video_exporter()
    audio_exporter: AudioExporter = fac.get_audio_exporter()

    video_exporter.prepare_exporter("placeholder_for_video_data")
    audio_exporter.prepare_audio("placeholder_for_audio_data")

    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
