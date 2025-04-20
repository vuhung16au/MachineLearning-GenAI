/** @type {import('next').NextConfig} */
const nextConfig = {
  // Enable strict mode for React
  reactStrictMode: true,
  // Ensure trailing slashes are not added to URLs
  trailingSlash: false,
  // Add custom headers for security
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff',
          },
          {
            key: 'X-Frame-Options',
            value: 'DENY',
          },
          {
            key: 'X-XSS-Protection',
            value: '1; mode=block',
          },
        ],
      },
    ];
  },
};

module.exports = nextConfig;