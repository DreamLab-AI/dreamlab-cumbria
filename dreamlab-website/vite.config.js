import { defineConfig } from 'vite';

export default defineConfig({
  root: '.',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: true,
    minify: 'terser',
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['alpinejs', 'aos']
        }
      }
    }
  },
  server: {
    port: 3000,
    open: true,
    host: true
  },
  css: {
    devSourcemap: true
  },
  optimizeDeps: {
    include: ['alpinejs', 'aos']
  }
});