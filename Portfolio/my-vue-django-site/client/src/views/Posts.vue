<template>
  <v-app>
  	<v-main>
      <h1 class="info--text">Posts</h1>
      <div v-for="posts in APIData.slice().reverse()" :key="posts.id">
      	<v-card class="mb-4 box-shadow info--text" color="secondary">
      		<div class="pa-2">
      			<h2>{{posts.title}}</h2>
	      		<p>{{posts.author}} @ {{posts.date}}</p>
	      		<p>{{posts.text}}</p>
      		</div>
      	</v-card>
      </div>
  	</v-main>
  </v-app>
</template>

<script>
	import { getAPI } from "../axios-api"

	export default {
		name: "Posts",
		data () {
			return {
				APIData: []
			}
		},
		created () {
			getAPI.get("/posts/")
			.then(response => {
				console.log("Post API has recieved data")
				this.APIData = response.data
			})
			.catch(err => {
				console.log(err)
			})
		},
	};
</script>
