# Python Versions in Package Manager Benchmarks

## Overview

This document explains the Python versions used in our package manager benchmarks (pip vs uv) and the rationale behind excluding certain versions from our testing.

## Python Version Lifecycle

Python follows a well-defined release and support lifecycle that affects which versions are suitable for benchmarking:

### Current Support Status (as of 2025)

Based on the [Python Developer's Guide](https://devguide.python.org/versions/), Python versions have different support phases:

- **Active Development**: New features and bug fixes
- **Bugfix Only**: Security and bug fixes only
- **Security Only**: Security fixes only
- **End-of-Life**: No longer supported

## Versions Included in Our Benchmarks

Our benchmark suite tests the following Python versions:

- **Python 3.9** (Security support until October 2025)
- **Python 3.10** (Security support until October 2026)
- **Python 3.11** (Security support until October 2027)
- **Python 3.12** (Security support until October 2028)
- **Python 3.13** (Bugfix support until October 2029)

These versions represent the current range of actively supported Python releases that are:
- Stable and production-ready
- Receiving security updates
- Widely adopted in the Python ecosystem
- Compatible with modern package managers

## Excluded Versions and Rationale

### Python 3.8 and Older Versions

**Status**: End-of-Life (EOL)

**Why Excluded**:
- **Security Vulnerabilities**: Python 3.8 reached end-of-life in October 2024, meaning it no longer receives security patches
- **Package Compatibility**: Many modern packages have dropped support for Python 3.8
- **Performance**: Older Python versions lack performance optimizations present in newer releases
- **Ecosystem Relevance**: The Python ecosystem has largely moved beyond these versions

**Specific EOL Dates**:
- Python 3.8: October 2024
- Python 3.7: June 2023
- Python 3.6: December 2021
- Python 2.7: January 2020

### Python 3.14 and 3.15

**Status**: Pre-release/Development

**Why Excluded**:

#### Python 3.14
- **Beta Status**: As of 2025, Python 3.14 is in beta phase
- **Instability**: Beta releases are subject to API changes and potential bugs
- **Limited Package Support**: Many packages may not yet support pre-release Python versions
- **Unreliable Benchmarks**: Performance characteristics may change before final release

#### Python 3.15
- **Development Phase**: Still in active development with frequent changes
- **Feature Incomplete**: New features are still being added and may change
- **No Production Use**: Not suitable for production environments
- **Benchmark Validity**: Results would not be representative of stable releases

## Benchmark Design Principles

Our benchmark methodology follows these principles:

1. **Production Relevance**: Only test versions that are suitable for production use
2. **Security**: Exclude versions with known security vulnerabilities
3. **Stability**: Focus on stable releases with predictable behavior
4. **Ecosystem Support**: Ensure package compatibility across tested versions
5. **Performance Validity**: Use versions that provide meaningful performance comparisons

## Version Selection Impact

The selected Python versions (3.9-3.13) provide:

- **Comprehensive Coverage**: Span multiple major Python releases
- **Real-world Relevance**: Represent versions actually used in production
- **Performance Progression**: Show how package managers perform across Python's evolution
- **Security Compliance**: All versions receive security updates
- **Package Compatibility**: Full support from the Python package ecosystem

## Future Considerations

As Python continues to evolve:

- **Python 3.14**: Will be included once it reaches stable release (expected October 2025)
- **Python 3.15**: Will be considered for future benchmarks after stable release
- **EOL Versions**: Will continue to be excluded as they reach end-of-life
- **Security Updates**: Will monitor security support status for all tested versions

## Conclusion

Our benchmark suite focuses on Python versions that are:
- Currently supported with security updates
- Stable and production-ready
- Representative of real-world usage patterns
- Compatible with modern package management tools

This approach ensures that our benchmark results are meaningful, reliable, and relevant to the Python development community.

## References

- [Python Developer's Guide - Versions](https://devguide.python.org/versions/)
- [Python Release Schedule](https://www.python.org/dev/peps/pep-0602/)
- [Python Security Advisories](https://python.org/security/)
