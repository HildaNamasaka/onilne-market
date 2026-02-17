import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    token : '',
    isLoading: false
  },
  getters: {
  },
  mutations: {
  initializeStore(state){
    if(localStorage.getItem('cart')){
      try {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } catch(e) {
        // If parsing fails, reset to default
        state.cart = { items: [] }
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    } else {
      localStorage.setItem('cart', JSON.stringify(state.cart))
    }
    
    // Extra safety: ensure cart.items exists
    if (!state.cart || !state.cart.items) {
      state.cart = { items: [] }
      localStorage.setItem('cart', JSON.stringify(state.cart))
    }
  },
  
  addToCart(state, item) {
    // Safety check
    if (!state.cart || !state.cart.items) {
      state.cart = { items: [] }
    }
    
    const exists = state.cart.items.filter(i => i.product.id === item.product.id)
    
    if (exists.length){
      exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
    } else {
      state.cart.items.push(item)
    }
    
    localStorage.setItem('cart', JSON.stringify(state.cart))
  },
  setIsLoading(state, status) {
    state.isLoading = status
  }
    },
  actions: {
  },
  modules: {
  }
})
