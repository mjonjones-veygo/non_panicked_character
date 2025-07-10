# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

This is a Python project using Poetry for dependency management.

### Setup and Installation
```bash
poetry install
```

### Testing
```bash
poetry run pytest
```

### Building
```bash
poetry build
```

## Project Architecture

This is a simple NPC (Non-Playable Character) generator utility library for tabletop RPGs.

### Core Structure
- `non_panicked_character/npc.py`: Main module containing utility functions for generating NPC attributes
- `non_panicked_character/__init__.py`: Package initialization with version info
- `tests/test_npc.py`: Test suite covering all generator functions

### Key Components
- **Generator Functions**: Simple random choice functions with customizable default arrays
  - `generate_race()`: Returns random race from configurable options
  - `generate_class()`: Returns random class from configurable options  
  - `generate_background()`: Returns random background from configurable options
  - `generate_name()`: Uses `names` library to generate full names with gender option
  - `generate_alignment()`: Returns random D&D-style alignment

### Dependencies
- `names`: External library for name generation
- `pytest`: Testing framework

## Release Management

This project uses semantic-release for automated versioning and releases.

### Commit Convention
Follow conventional commits with these categories:
- `fix`: Bug fixes (patch version bump)
- `feat`: New features (minor version bump)
- `BREAKING CHANGE`: Include in footer for major version bumps

### Version Management
- Version is tracked in both `pyproject.toml` and `non_panicked_character/__init__.py`
- Releases are published to GitHub releases (not PyPI)
- Build command: `pip install poetry && poetry build`