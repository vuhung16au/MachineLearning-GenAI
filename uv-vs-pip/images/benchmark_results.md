## Benchmark Summary: uv vs pip

### Per Python version

| Python | pip | uv | winner |
|---|---:|---:|:--:|
| python3.9 | 62.354 | 12.943 | uv |
| python3.10 | 61.727 | 8.212 | uv |
| python3.11 | 58.105 | 6.985 | uv |
| python3.12 | 62.433 | 7.728 | uv |
| python3.13 | 60.338 | 8.173 | uv |

### Overall mean (seconds over successful runs)

| Manager | Mean seconds | Successful runs | Total runs |
|---|---:|---:|---:|
| pip | 60.991 | 15 | 15 |
| uv | 8.808 | 15 | 15 |

## System Information

- **OS**: Darwin 24.6.0
- **Architecture**: arm64
- **Python**: 3.9.6
- **macOS**: 15.6
