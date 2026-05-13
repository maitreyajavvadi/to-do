import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      // Neo-Brutalism design system
      colors: {
        brand: {
          yellow: '#FFE500',
          blue: '#0047FF',
          pink: '#FF3CAC',
          green: '#00FF87',
          black: '#0A0A0A',
          white: '#FAFAFA',
        },
        priority: {
          low: '#00FF87',
          medium: '#FFE500',
          high: '#FF6B00',
          critical: '#FF0000',
        },
        status: {
          todo: '#E5E5E5',
          'in-progress': '#FFE500',
          blocked: '#FF3CAC',
          done: '#00FF87',
        },
      },
      fontFamily: {
        sans: ['var(--font-space-grotesk)', 'system-ui', 'sans-serif'],
        mono: ['var(--font-space-mono)', 'monospace'],
      },
      fontSize: {
        display: ['4rem', { lineHeight: '1', fontWeight: '900' }],
        heading: ['2rem', { lineHeight: '1.1', fontWeight: '800' }],
      },
      borderWidth: {
        '3': '3px',
        '4': '4px',
      },
      boxShadow: {
        brutal: '4px 4px 0px 0px #0A0A0A',
        'brutal-lg': '6px 6px 0px 0px #0A0A0A',
        'brutal-xl': '8px 8px 0px 0px #0A0A0A',
        'brutal-blue': '4px 4px 0px 0px #0047FF',
        'brutal-pink': '4px 4px 0px 0px #FF3CAC',
      },
      animation: {
        'slide-in': 'slideIn 0.2s ease-out',
        'fade-in': 'fadeIn 0.15s ease-out',
      },
      keyframes: {
        slideIn: {
          '0%': { transform: 'translateY(-8px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  plugins: [],
};

export default config;
