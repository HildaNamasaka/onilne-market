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
      
      <ProductBox
        v-for="product in products"
        v-bind:key="product.id"
        v-bind:product="product"
      />

    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from'axios'
import ProductBox from '@/components/ProductBox.vue';


export default {
  name: 'HomeView',
  data() {
    return{
      products: []
    }

  },

  components: {
    ProductBox
  },
  mounted() {
    this.getProducts()
    document.title = 'Home | market'
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
