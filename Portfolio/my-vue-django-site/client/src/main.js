// Polyfills
import "core-js/stable";
import "regenerator-runtime/runtime";

// Imports
import vuetify from "./plugins/vuetify";
import Vue from "vue";
import App from "./App.vue";
import router from "./router";

Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount("#app");
