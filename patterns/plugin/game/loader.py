"""Simple plugin loader"""

import importlib


class PluginInterface:
    @staticmethod
    def initialize() -> None:
        """Initialize plugin"""


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)  # type: ignore


def load_plugins(plugins: list[str]) -> None:
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initialize()
