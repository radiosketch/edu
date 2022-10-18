<template>
  <v-app>
    <v-main>
      <div class="image">
        <img
          src="../assets/frontpage_blobs.png"
          width="100%"
          id="blobs"
        />
        <img
          src="../assets/logo_palette_2.png"
          width="20%"
          id="icon"
        />
      </div>
      <v-divider class="mx-4"></v-divider>
    </v-main>
  </v-app>
</template>

<script></script>

<style>
	#icon {
		position: absolute;
		right: 40%;
		top: 15%;
	}

	#blobs {
		position: absolute;
		left: -0%;
		top: -12px;
	}

  .image {
    position: relative;
  }

</style>
