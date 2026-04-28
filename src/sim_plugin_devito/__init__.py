"""Devito driver plugin for sim-cli.

Distributed as an out-of-tree plugin; discovered by sim-cli via the
``sim.drivers`` entry-point group. Bundled skill files (under
``_skills/``) are exposed via the ``sim.skills`` entry-point group, and
lightweight metadata via ``sim.plugins``.
"""
from importlib.resources import files

from .driver import DevitoDriver

skills_dir = files(__name__) / "_skills"

plugin_info = {
    "name": "devito",
    "summary": "Devito driver for sim.",
    "homepage": "https://github.com/svd-ai-lab/sim-plugin-devito",
    "license_class": "oss",
    "solver_name": "Devito",
}

__all__ = ["DevitoDriver", "skills_dir", "plugin_info"]
