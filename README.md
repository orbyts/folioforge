# Folioforge

A shared asset library for icons, logos, banners, and brand artwork. Cloudinary is the planned delivery and transformation layer; Notion, websites, and other applications are consumers.

## Status

Version **0.0.0** is the initial foundation release. It provides version/help commands and an offline unsigned Cloudinary URL builder. Upload, download, inventory, cover generation, and consumer synchronization are planned, not implemented yet.

## Install

```sh
uv tool install folioforge
# or: pip install folioforge
folioforge --version
folioforge url brands/acme/logo.svg --cloud example
folioforge url brands/acme/logo.svg --cloud example --gray
```

The path includes the asset extension. The URL command neither uploads nor checks asset existence. It targets public image/upload assets. Gray delivery uses flat #808080 colorization and PNG output; it does not promise transformed SVG output. White overlays in a logo should be converted to genuine transparent cutouts before flattening colors.

## Direction

- One canonical color master per distinct symbol, wordmark, lockup, or artwork; genuine SVG preferred.
- Generate size, format, padding and monochrome derivatives rather than uploading duplicate masters.
- Inventory, upload, download, deduplicate, and generate delivery URLs across a portable asset registry.
- Compose full logos with reusable translucent background templates; use brand palettes and explicit or seeded random template selection.
- Separate the core library, storage adapters, renderers and consumer adapters so a future UI reuses the CLI's services.
- Plan and preview changes, preserve provenance and references, and verify migrations before retiring assets.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the initial roadmap.

## Development

Python 3.11+, uv, and Git. No runtime dependencies in this initial release.

```sh
uv sync
uv run python -m unittest discover -s tests
uv build --no-sources
```

Apache-2.0 licensed.
