import Vue from "vue";
import Vuetify from "vuetify/lib";

Vue.use(Vuetify);

const opts = {
  theme: {
    dark: true,
    themes: {
      dark: {
        primary: "#11151c",
        secondary: "#212d40",
        tertiary: "#364156",
        error: "#d66853",
        info: "#edebd7",
        success: "#e3b23c",
        warning: "#7d4e57"
      }
    }
  }
};

export default new Vuetify(opts);
