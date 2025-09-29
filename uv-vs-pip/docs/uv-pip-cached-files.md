# uv vs pip: Cached Files Management

## Where are the cached files?

### pip cache directory
```bash
pip cache dir
```
**Default locations:**
- **macOS**: `~/Library/Caches/pip/`
- **Linux**: `~/.cache/pip/`
- **Windows**: `%LOCALAPPDATA%\pip\Cache`

### uv cache directory
```bash
uv cache dir
```
**Default locations:**
- **macOS**: `~/.cache/uv/`
- **Linux**: `~/.cache/uv/`
- **Windows**: `%LOCALAPPDATA%\uv\Cache`

## Command to clear cached files

### Clear pip cache
```bash
pip cache purge
```

### Clear uv cache
```bash
uv cache clean
```

## Cached files on Mac

On Mac, by default:

- **pip**: `~/Library/Caches/pip/`
- **uv**: `~/.cache/uv/`

## Cache Management Details

### pip Cache Structure
```
~/Library/Caches/pip/
├── http/
│   └── [domain-hash]/
│       └── [package-files]
└── wheels/
    └── [package-files]
```

### uv Cache Structure
```
~/.cache/uv/
├── wheels/
│   └── [package-files]
├── registry/
│   └── [index-cache]
└── git/
    └── [git-repositories]
```

## Cache Size Management

### Check cache sizes
```bash
# pip cache info
pip cache info

# uv cache info (if available)
du -sh ~/.cache/uv/
```

### Manual cache cleanup
```bash
# Remove pip cache manually
rm -rf ~/Library/Caches/pip/

# Remove uv cache manually
rm -rf ~/.cache/uv/
```

## Environment Variables

### pip cache control
```bash
# Set custom cache directory
export PIP_CACHE_DIR="/custom/path"

# Disable cache
export PIP_NO_CACHE_DIR=1
```

### uv cache control
```bash
# Set custom cache directory
export UV_CACHE_DIR="/custom/path"

# Disable cache
uv pip install --no-cache-dir package
```

## Cache Benefits

| Feature | pip | uv |
|---------|-----|----|
| **Speed Improvement** | 2-5x faster | 10-100x faster |
| **Disk Usage** | 200MB-2GB | 50MB-500MB |
| **Cache Efficiency** | Basic | Advanced |
| **Network Reduction** | Good | Excellent |

## Best Practices

### For Development
- **Keep caches** for faster subsequent installs
- **Clean periodically** to free disk space
- **Monitor cache size** in CI/CD environments

### For CI/CD
- **Use cache** to speed up builds
- **Clean between builds** to avoid conflicts
- **Set cache limits** to prevent disk issues

### For Production
- **Disable cache** for security-sensitive deployments
- **Use lock files** instead of cache for reproducibility
- **Clean cache** before final deployment

## Troubleshooting

### Cache-related issues
```bash
# Clear all caches
pip cache purge
uv cache clean

# Reset to defaults
unset PIP_CACHE_DIR
unset UV_CACHE_DIR

# Check cache permissions
ls -la ~/Library/Caches/pip/
ls -la ~/.cache/uv/
```

### Cache corruption
```bash
# Remove corrupted cache
rm -rf ~/Library/Caches/pip/
rm -rf ~/.cache/uv/

# Reinstall packages to rebuild cache
pip install --no-cache-dir -r requirements.txt
uv pip install --no-cache-dir -r requirements.txt
```
