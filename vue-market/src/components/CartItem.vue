<template>
<tr v-if="item && item.product">  <!-- ✅ Only show if product exists -->
    <td><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
    <td>ksh{{ item.product.price }}</td>
    <td>
        {{ item.quantity }}

        <a @click="decreamentQuantity(item)"> - </a>
        <a @click="increamentQuantity(item)"> + </a>

    </td>
    <td>ksh{{ getItemTotal(item).toFixed(2) }}</td>
    <td><button class="delete" @click="removeFromCart(item)"></button></td>
</tr>
</template>

<script>
export default{
    name:'CartItem',
    props: {
        initialItem: Object
    },
    data(){
        return {
            item: this.initialItem
        }
    },
    mounted() {
        console.log('Cart item:', this.item)  // Check what's in the item
    },
    methods: {
        getItemTotal(item) {
            if (!item.product) return 0  // ✅ Safety check
            return item.quantity * item.product.price
        },
        decreamentQuantity(item){
            item.quantity -=1
            this.updateCart()

            if(item.quantity === 0){
                this.$emit('removeFromCart', item)
            }
        }, 
        increamentQuantity(item){
            item.quantity += 1
            this.updateCart()
        }, 
        updateCart(){
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item){
            this.$emit('removeFromCart', item)
            this.updateCart()
        }
    }
}
</script>