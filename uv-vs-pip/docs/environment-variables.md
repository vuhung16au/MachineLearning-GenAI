Here are some of the most important environment variables for both package managers:

### Environment Variables for `pip`

`pip` relies on environment variables, often prefixed with `PIP_`, to override default settings and behavior, which is useful in continuous integration (CI) or constrained network environments.

| Environment Variable | Description |
| :--- | :--- |
| **`PIP_INDEX_URL`** | Specifies the base URL of the Python package index to use (e.g., a private repository). |
| **`PIP_EXTRA_INDEX_URL`** | Specifies secondary index URLs to search for packages, in addition to the main index. |
| **`PIP_CACHE_DIR`** | Overrides the default location where `pip` stores downloaded `.whl` files and package metadata. |
| **`PIP_DEFAULT_TIMEOUT`** | Sets the network timeout (in seconds) for connecting to package repositories. |
| **`PIP_REQUIRE_VIRTUALENV`** | If set to `true`, `pip` will refuse to install packages globally (outside of an active virtual environment). |
| **`HTTP_PROXY` / `HTTPS_PROXY`** | Standard network variables used by `pip` to connect through a proxy server. |

---

### Environment Variables for `uv`

`uv` is designed to be highly configurable, inheriting many conventions from the Rust and Python packaging ecosystems.

| Environment Variable | Description |
| :--- | :--- |
| **`UV_NO_CACHE`** | If set to `true` (or `1`), prevents `uv` from using the local cache for installation, forcing it to download packages every time. |
| **`UV_INDEX_URL`** | Specifies the base index URL, similar to `PIP_INDEX_URL`. |
| **`UV_EXTRA_INDEX_URL`** | Specifies secondary index URLs to search for packages. |
| **`UV_CACHE_DIR`** | Overrides the default location where `uv` stores its package cache (`~/.cache/uv` on Linux). |
| **`UV_HTTP_TIMEOUT`** | Sets the maximum time (in seconds) for network requests, similar to `PIP_DEFAULT_TIMEOUT`. |
| **`UV_AS_PIP`** | When set, allows the `uv` executable to be invoked using the command `pip` instead of `uv`, ensuring compatibility with existing scripts. |