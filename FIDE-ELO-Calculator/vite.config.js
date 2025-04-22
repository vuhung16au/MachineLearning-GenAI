import { defineConfig } from 'vite';

export default defineConfig({
  root: './',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    rollupOptions: {
      input: {
        main: './index.html',
      },
    }
  },
  server: {
    port: 8080,
    open: true,
    watch: {
      usePolling: true
    }
  },
  css: {
    devSourcemap: true
  },
});