import { IconsetRegistration } from 'https://cdn.jsdelivr.net/gh/custom-cards/ha-svg-iconset@1.3.0/ha-svg-iconset.js';

IconsetRegistration.registerIconset('bf', {
  size: 24,
  icons: {
    // Philips Hue old-style dimmer
    'hue-dimmer-old': `
      <g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
        <rect x="6" y="2.5" width="12" height="19" rx="2.2"/>
        <circle cx="12" cy="6.5" r="1.4"/>
        <path d="M9 10.5h6M12 9v3"/>
        <path d="M9 13.5h6"/>
        <circle cx="12" cy="17.5" r="1.4"/>
      </g>
    `,
    // Flic logo
    'flic-mark': `
      <g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="7.5"/>
        <path d="M10.2 9.2c.2-1.1 1-1.7 2.1-1.7h.9M12.2 7.5v9M10.1 13.2c1.1 1 2.3 1.2 3.6.2"/>
      </g>
    `,
    // Work tomorrow: hammer + clock + arrow
    'work-tomorrow': `
      <g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
        <path d="M5 9.5h7v2H5z"/>
        <path d="M9 11.5l5 6.5"/>
        <circle cx="17" cy="7" r="2.4"/>
        <path d="M17 7v-1 M17 7l1.2.8"/>
        <path d="M14 12h6"/>
        <path d="M18 10l2 2-2 2"/>
      </g>
    `,
  },
});