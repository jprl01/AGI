import 'vuetify/dist/vuetify.min.css';
import { createVuetify } from 'vuetify';
import { aliases, fa } from 'vuetify/iconsets/fa';
import { mdi } from 'vuetify/iconsets/mdi';
import { VDataTable } from 'vuetify/labs/VDataTable';

// FIXME: import colors from 'vuetify/lib/util/colors';
// I think they forgot to export them in Vuetify 3...
// https://github.com/vuetifyjs/vuetify/blob/v3.0.2/packages/vuetify/src/util/colors.ts

const vuetify = createVuetify({
  components: { VDataTable },
  icons: {
    defaultSet: 'fa',
    aliases,
    sets: { fa, mdi },
  },
  theme: {
    defaultTheme: 'light',
    themes: {
      light: {
        dark: false,
        colors: {
          primary: '#757575', // colors.grey.darken1
          secondary: '#444444',
          accent: '#999999',
          error: '#b71c1c',
          darkOrange: '#c45d0e',
          edit: '#d4ad3c',
          light: '#f1f1f1',
          background: '#ffffff',
          info: '#0F9AD7',
          success: '#07844e',
          text: '#000000',
          chat: '#ebebeb',
        },
      },
      dark: {
        dark: true,
        colors: {
          primary: '#757575', // colors.grey.darken1
          secondary: '#444444',
          accent: '#999999',
          error: '#6f0000',
          darkOrange: '#92460c',
          edit: '#bd9931',
          background: '#171F24',
          info: '#0F9AD7',
          success: '#07844e',
          text: '#ffffff',
          chat: '#737373',
        },
      },
    },
  },
});

export default vuetify;
