<template>
  <div class="home">
    <section class="hero is-mediun mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to the cloth market
        </p>
        <p class="subtitle">
          An affordable cloth store
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>
      <div class="column is-3" v-for="product in products" v-bind:key="product.id">
        <div class="box">
          <figure class="image mb-4">
            <img v-bind:src="product.get_thumbnail">
          </figure>
          <h3 class="is-size-4 has-text-centered">{{ product.name }}</h3>
          <p class="is-size-6 has-text-centered">ksh{{ product.price }}</p>
          view details
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from'axios'

export default {
  name: 'HomeView',
  data() {
    return{
      products: []
    }

  },

  components: {
  },
  mounted() {
    this.getProducts()
  },
  methods:{
    getProducts(){
      axios.get('/api/v1/products/').then(response => {
        this.products = response.data
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
<style scoped>
  .image{
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>
