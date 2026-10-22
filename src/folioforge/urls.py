"""Cloudinary delivery URL construction without credentials or network access."""
import re
from urllib.parse import quote


def delivery_url(cloud: str, public_id: str, *, gray: bool = False) -> str:
    """Build an unsigned public image/upload URL; public_id includes its extension.

    Gray delivery is explicitly PNG: SVG passthrough may ignore colorization.
    Private/authenticated assets and signed transformations are not supported.
    """
    if not re.fullmatch(r"[A-Za-z0-9_-]+", cloud):
        raise ValueError("cloud must be a Cloudinary cloud name")
    if not public_id or any(part in ("", ".", "..") for part in public_id.split("/")):
        raise ValueError("public_id must be a nonempty relative asset path")
    transform = "e_colorize:100,co_rgb:808080/f_png/" if gray else ""
    return f"https://res.cloudinary.com/{cloud}/image/upload/{transform}{quote(public_id, safe='/')}"
