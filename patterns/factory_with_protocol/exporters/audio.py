import pathlib
from typing import Protocol


class AudioExporter(Protocol):
    def prepare_audio(self, audio_data):
        """Prepares audio data for exporting."""

    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""


class AACAudioExporter:
    def prepare_audio(self, audio_data):
        return "Preparing audio data for AAC export."

    def do_export(self, folder: pathlib.Path):
        return f"Exporting audio data in AAC format to {folder}"


class WAVAudioExporter:
    def prepare_audio(self, audio_data):
        return "Preparing audio data for WAV export."

    def do_export(self, folder: pathlib.Path):
        return f"Exporting audio data in WAV format to {folder}"
