# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-11-13

### Added

- Filter notes by tag
- Export a notebook to a JSON string
- Search across all notes by their text

### Fixed

- Duplicate tags on a note are no longer stored
- A missing notes file now produces a clear error message

## [0.1.0] - 2026-01-15

### Added

- Initial release of the `notes` library
- In-memory notebook with add / get / list / remove / find
- JSON persistence via `storage.save` and `storage.load`
