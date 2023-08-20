from typing import Type
from dataclasses import dataclass
import pathlib

from exporters.video import VideoExporter, H264BPVideoExporter, H264Hi422BPVideoExporter, LossLessVideoExporter
from exporters.audio import AudioExporter, AACAudioExporter, WAVAudioExporter



@dataclass
class MediaExporter:
    video: VideoExporter
    audio: AudioExporter


@dataclass
class MediaExporterFactory:
    video_class: Type[VideoExporter]
    audio_class: Type[AudioExporter]

    def __call__(self) -> MediaExporter:
        return MediaExporter(video=self.video_class(), audio=self.audio_class())


FACTORIES = {
    "low": MediaExporterFactory(H264BPVideoExporter, AACAudioExporter),
    "high": MediaExporterFactory(H264Hi422BPVideoExporter, AACAudioExporter),
    "master": MediaExporterFactory(LossLessVideoExporter, WAVAudioExporter),
}


def read_factory() -> MediaExporterFactory:
    while True:
        export_quality = input(f"Enter output quality ({', '.join(FACTORIES)}): ")
        try:
            return FACTORIES[export_quality]
        except KeyError:
            print(f"Unknow quality level: {export_quality}")


def do_export(exporter: MediaExporter) -> None:

    exporter.video.prepare_exporter("placeholder_for_video_data")
    exporter.audio.prepare_audio("placeholder_for_audio_data")

    folder = pathlib.Path("/usr/tmp/video")
    print(exporter.video.do_export(folder))
    print(exporter.audio.do_export(folder))


def main():
    factory = read_factory()
    media_exporter = factory()
    do_export(media_exporter)


if __name__ == "__main__":
    main()
