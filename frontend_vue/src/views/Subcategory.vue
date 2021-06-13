<template>
<div>
  <Header/>
        <section class="section">
      <div class="container is-fluid">
        <div class="mt-3">

          <nav class="breadcrumb" aria-label="breadcrumbs">
  <ul>
    <li><router-link to="/category" class="">Категории</router-link></li>
    <li class="is-active"><router-link :to="{name: 'Subcategory', params: {id: this.id}}" class="">Категория "{{ name }}"</router-link></li>
  </ul>
</nav>


          <h1 class="title mb-6">Подкатегории</h1>
            <div v-for="subcategory in subcategories" :key="subcategory.id">
            <table class="table is-fullwidth">
  <tbody>
    <tr>
      <td><router-link :to="{name: 'Questions', params: {id2: subcategory.id}}" class="">{{ subcategory.nameSubcategory }}</router-link><hr></td>
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
    name: 'Subcategory',
    data() {
    return {
      id:this.$route.params.id,
      name:"",
      subcategories: [],
      categories: [],
    };
  },
      components: {
        Footer,
        Header
    },
    mounted() {
        document.title = 'Подкатегории | DjangoQuestions',
        this.getSubcategories(),
        this.getCategories()
    },
    methods: {
      getCategories() {
      axios
        .get("api/v1/categories/")
        .then(response => {
          this.categories = response.data;
          this.name = this.categories[this.id-1].nameCategory;
        })
        .catch(error => {
          console.log(error);
        });
    },


       getSubcategories() {
      axios
        .get(`/api/v1/categories/${this.id}`)
        .then(response => {
          this.subcategories = response.data;
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