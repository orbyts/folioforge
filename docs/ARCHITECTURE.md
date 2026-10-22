# Architecture and next steps

Python was selected for API integration, SVG/image tooling and a reusable application core. Rendering backends can use native libraries or a Rust implementation later if measured performance warrants it.

## Boundaries

- Core: entities, canonical representations, provenance, asset references, delivery profiles and migration plans.
- Providers: Cloudinary inventory/upload/download and URL generation. Credentials stay outside the registry.
- Rendering: SVG logo placement, alpha-safe palette extraction, reusable neutral background templates, deterministic seeds, focal bounds and crop previews.
- Consumers: Notion page icons/covers, website manifests and future applications.
- Interfaces: CLI first; a UI calls the same core services later.

Asset identity must remain independent of consumer and folder layout. Canonical color SVGs are preferred, but raster-in-SVG is not vector. A distinct symbol and full lockup can both be legitimate masters. Do not store redundant gray or raster masters when delivery transforms suffice. Gray SVG recoloring is not assumed to work through Cloudinary passthrough.

## Milestones

0.0.0: packaging, CLI entry point, offline public Cloudinary URL builder.

Next: typed configuration and portable registry; read-only inventory/import with hashes and duplicate candidates; Cloudinary upload/download with dry-run plans; tested delivery profiles; deterministic SVG cover templates; Notion adapter; optional UI.

Mutation tools must save before states, avoid overwrite by default, preserve working public IDs, and verify outcomes. Deletion requires explicit targets and reference checks. Secrets belong in environment variables or a credential provider, never source control or synced config.
