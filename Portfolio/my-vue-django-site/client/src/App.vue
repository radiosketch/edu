<template>
  <v-app>
    <!-- Navigation -->
    <v-toolbar app color="secondary">
      <div class="row">
        <div class="column25">
          <router-link
            to="/"
            class="secondary--text"
          >
            <div class="px-4">
              <v-btn
                outlined
                width="100%"
                color="error"
                class="secondary--text"
              >
                <v-icon>mdi-home</v-icon>
              </v-btn>
            </div>
          </router-link>
        </div>
        <div class="column25">
          <router-link
            to="/"
            class="secondary--text"
          >
            <div class="px-4">
              <v-btn
                outlined
                width="100%"
                color="success"
                class="secondary--text"
              >
                About Me
              </v-btn>
            </div>
          </router-link>
        </div>
        <div class="column25">
          <router-link
            to="/posts"
            class="secondary--text"
          >
            <div class="px-4">
              <v-btn
                outlined
                width="100%"
                color="success"
                class="secondary--text"
              >
                Posts
              </v-btn>
            </div>
          </router-link>
        </div>
        <div class="column25">
          <div class="px-4">
            <v-btn
              outlined
              width="100%"
              color="success"
              class="secondary--text"
              href="https://github.com/patrick-yeadon"
            >
              Github
            </v-btn>
          </div>
        </div>
      </div>
    </v-toolbar>

    <v-main>
      <v-container fluid>
        <router-view/>
      </v-container>
    </v-main>

    <v-footer class="info--text" color="secondary">
      <div class="row pa-9">
        <div class="column33">
          <h2>About</h2>
          <p>Learn more about me</p>
        </div>
        <div class="column33">
          <h2>Contact Me</h2>
          <a
            href=""
            class="info--text"
          >
            patrickyeadon@hotmail.com
          </a>
        </div>
        <div class="column33">
          <h2>Github</h2>
          <a
            href="https://github.com/patrick-yeadon"
            class="info--text"
          >
            patrick-yeadon@github.com
          </a>
        </div>
      </div>
    </v-footer>

  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    //
  })
};
</script>

<style>
  .column25 {
    width: 25%;
  }

  .column33 {
    width: 33.33%;
  }
</style>
