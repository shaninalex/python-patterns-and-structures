import unittest
import pathlib

from exporters.video import H264BPVideoExporter, H264Hi422BPVideoExporter, LossLessVideoExporter
from exporters.audio import AACAudioExporter, WAVAudioExporter


class LossLessVideoExporter_TestCase(unittest.TestCase):
    def init_test(self):
        exp = LossLessVideoExporter()
        self.assertIsInstance(exp, LossLessVideoExporter)

    def test_prepare_exporter(self):
        exp = LossLessVideoExporter()
        self.assertEqual(
            exp.prepare_exporter("video data"),
            "Preparing video data for lossless export.",
        )

    def test_do_export(self):
        exp = LossLessVideoExporter()
        folder = pathlib.Path("/usr/test/video")
        self.assertEqual(
            exp.do_export(folder),
            f"Exporting video data in lossless format to {folder}",
        )


class H264BPVideoExporter_TestCase(unittest.TestCase):
    def init_test(self):
        exp = H264BPVideoExporter()
        self.assertIsInstance(exp, H264BPVideoExporter)

    def test_prepare_exporter(self):
        exp = H264BPVideoExporter()
        self.assertEqual(
            exp.prepare_exporter("video data"), "Preparing video data for H.264 export."
        )

    def test_do_export(self):
        exp = H264BPVideoExporter()
        folder = pathlib.Path("/usr/test/video")
        self.assertEqual(
            exp.do_export(folder), f"Exporting video data in H.264 format to {folder}"
        )


class H264Hi422BPVideoExporter_TestCase(unittest.TestCase):
    def init_test(self):
        exp = H264Hi422BPVideoExporter()
        self.assertIsInstance(exp, H264Hi422BPVideoExporter)

    def test_prepare_exporter(self):
        exp = H264Hi422BPVideoExporter()
        self.assertEqual(
            exp.prepare_exporter("video data"), "Preparing video data for H.264 with Hi422 profile export."
        )

    def test_do_export(self):
        exp = H264Hi422BPVideoExporter()
        folder = pathlib.Path("/usr/test/video")
        self.assertEqual(
            exp.do_export(folder), f"Exporting video data in H.264 with Hi422 profile format to {folder}"
        )


class AACAudioExporter_TestCase(unittest.TestCase):
    def init_test(self):
        exp = AACAudioExporter()
        self.assertIsInstance(exp, AACAudioExporter)

    def test_prepare_exporter(self):
        exp = AACAudioExporter()
        self.assertEqual(
            exp.prepare_audio("audio data"), "Preparing audio data for AAC export."
        )

    def test_do_export(self):
        exp = AACAudioExporter()
        folder = pathlib.Path("/usr/test/audio")
        self.assertEqual(
            exp.do_export(folder), f"Exporting audio data in AAC format to {folder}"
        )


class WAVAudioExporter_TestCase(unittest.TestCase):
    def init_test(self):
        exp = WAVAudioExporter()
        self.assertIsInstance(exp, WAVAudioExporter)

    def test_prepare_exporter(self):
        exp = WAVAudioExporter()
        self.assertEqual(
            exp.prepare_audio("video data"), "Preparing audio data for WAV export."
        )

    def test_do_export(self):
        exp = WAVAudioExporter()
        folder = pathlib.Path("/usr/test/audio")
        self.assertEqual(
            exp.do_export(folder), f"Exporting audio data in WAV format to {folder}"
        )
