## Benchmark Summary: uv vs pip

### Per Python version

| Python | pip | uv | winner |
|---|---:|---:|:--:|
| python3.9 | 60.338 | 10.028 | uv |
| python3.10 | 56.172 | 6.448 | uv |
| python3.11 | 54.516 | 6.958 | uv |
| python3.12 | 60.357 | 7.177 | uv |
| python3.13 | 55.709 | 6.457 | uv |

### Overall mean (seconds over successful runs)

| Manager | Mean seconds | Successful runs | Total runs |
|---|---:|---:|---:|
| pip | 57.418 | 15 | 15 |
| uv | 7.414 | 15 | 15 |

## System Information

- **OS**: Darwin 24.6.0
- **Architecture**: arm64
- **Python**: 3.9.6
- **macOS**: 15.6
