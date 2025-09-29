# Documentation

This folder contains comprehensive documentation for the Python Package Manager Comparison project, comparing `pip` vs `uv` performance and features.

## 📚 Documentation Overview

### Core Documentation

| Document | Description | Purpose |
|----------|-------------|---------|
| [`intro-uv-vs-pip.md`](./intro-uv-vs-pip.md) | **Main comparison guide** | Comprehensive feature comparison, use cases, and recommendations |
| [`uv-pip-cached-files.md`](./uv-pip-cached-files.md) | **Cache management guide** | How to manage cached files for both package managers |

### Additional Resources

| Document | Description | Purpose |
|----------|-------------|---------|
| [`environment-variables.md`](./environment-variables.md) | **Environment configuration** | Key environment variables for both tools |

## 🚀 Quick Start

### For New Users
1. Start with [`intro-uv-vs-pip.md`](./intro-uv-vs-pip.md) for a complete overview
2. Check [`uv-pip-cached-files.md`](./uv-pip-cached-files.md) for cache management
3. Review [`environment-variables.md`](./environment-variables.md) for configuration

### For Developers
- **Performance Analysis**: See benchmark results in `../results/benchmark_results.md`
- **Cache Optimization**: Use cache management guide for CI/CD optimization
- **Migration Planning**: Follow recommendations in the main comparison guide

## 📊 Key Findings

### Performance Comparison
- **uv is 2.5x faster** on average (59.0s vs 23.2s)
- **Speed improvement increases** with newer Python versions
- **Memory usage is 2-4x lower** with uv

### When to Choose Each Tool

#### Choose **uv** for:
- ✅ New projects and modern workflows
- ✅ CI/CD environments where speed matters
- ✅ Large dependency trees
- ✅ Resource-constrained environments

#### Choose **pip** for:
- ✅ Legacy projects and established workflows
- ✅ Maximum compatibility requirements
- ✅ Simple use cases with few dependencies
- ✅ Educational and learning contexts

## 🛠️ Cache Management

### Quick Commands
```bash
# Check cache locations
pip cache dir
uv cache dir

# Clear caches
pip cache purge
uv cache clean
```

### Default Locations (macOS)
- **pip**: `~/Library/Caches/pip/`
- **uv**: `~/.cache/uv/`

## 📈 Benchmark Results

Our comprehensive benchmarks show:

| Python Version | pip (seconds) | uv (seconds) | Speedup |
|----------------|---------------|--------------|:-------:|
| Python 3.9 | 59.4 | 30.6 | 1.9x |
| Python 3.10 | 60.0 | 22.1 | 2.7x |
| Python 3.12 | 57.8 | 20.5 | 2.8x |
| Python 3.13 | 58.8 | 19.4 | 3.0x |

## 🔧 Environment Configuration

Key environment variables for both tools:

### pip
```bash
export PIP_CACHE_DIR="/custom/path"
export PIP_NO_CACHE_DIR=1
```

### uv
```bash
export UV_CACHE_DIR="/custom/path"
uv pip install --no-cache-dir package
```

## 📚 Additional Resources

- **Project Repository**: See `../README.md` for setup and usage
- **Benchmark Results**: Check `../results/` for detailed performance data
- **Scripts**: Review `../scripts/` for automation tools
- **Makefile**: Use `../Makefile` for easy benchmark execution

## 🤝 Contributing

To contribute to this documentation:

1. **Update benchmarks**: Run `make all` to generate fresh data
2. **Improve guides**: Add new use cases and scenarios
3. **Fix issues**: Report problems or suggest improvements
4. **Add examples**: Include practical code samples and workflows

## 📝 Documentation Standards

- **Markdown format** for all documentation
- **Clear headings** with consistent structure
- **Code blocks** with syntax highlighting
- **Tables** for comparison data
- **Practical examples** with real commands
- **Cross-references** between related documents

---

*This documentation is part of the Python Package Manager Comparison project. For the latest updates and benchmark results, see the main project repository.*
