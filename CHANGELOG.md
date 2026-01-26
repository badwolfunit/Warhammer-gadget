# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Added comprehensive .gitignore file for Python projects
- Added CONTRIBUTING.md with contribution guidelines
- Added docstrings to all functions
- Added error handling for dice rolling input validation
- Added error handling for datasheet loading (missing directory, invalid JSON)
- Added proper relative imports in main.py

### Changed
- Improved README.md with better structure, installation instructions, and usage examples
- Fixed typos throughout the codebase ("Bawolfunit" → "Badwolfunit")
- Fixed typos in README.md ("inlcuding" → "including", "copywrite" → "copyright", "conective" → "connective")
- Improved code formatting and consistency across all Python files
- Enhanced license header formatting in all source files
- Updated main() function to only run when script is executed directly

### Removed
- Removed self-deprecating comment from main.py
- Removed pyright ignore comments (fixed imports properly instead)
- Removed __pycache__ files from git tracking

## [0.0.1] - 2026-01-26

### Added
- Initial release
- Basic dice rolling functionality
- Datasheet viewing from JSON files
- TUI interface for PC
- Command-line entry point
