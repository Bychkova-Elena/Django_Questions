<template>

<div>
  <Header/>
        <section class="section">
      <div class="container is-fluid">
        <div class="mt-3">
          <h1 class="title mb-6">Категории</h1>
            <div v-for="category in categories" :key="category.id">
            <table class="table is-fullwidth">
  <tbody>
    <tr>
      <td><router-link :to="{name: 'Subcategory', params: {id: category.id}}" class="">{{ category.nameCategory }}</router-link><hr></td>
    </tr>
  </tbody>
    </table>
            </div>
          </div>
        </div>
    </section>
  <Footer/>
</div>
</template>
<script>

import axios from 'axios'
import Footer from '@/components/Footer'
import Header from '@/components/Header'

export default {
    name: 'Category',
    data() {
    return {
      categories: [],
    };
  },

        components: {
        Footer,
        Header
    },
    mounted() {
        document.title = 'Категории | DjangoQuestions',
        this.getCategories()
    },
    methods: {
       getCategories() {
      axios
        .get("api/v1/categories/")
        .then(response => {
          this.categories = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
        
    }
}
</script>

<style lang="scss" scope>


</style>