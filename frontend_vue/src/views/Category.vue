<template>
        <section class="section">
      <div class="container is-fluid">
        <div class="mt-3">
          <h1 class="title mb-6">Категории</h1>
            <div v-for="category in categories" :key="category.id">
            <table class="table is-fullwidth">
  <tbody>
    <tr>
      <td><router-link to="/subcategory" class="">{{ category.nameCategory }}</router-link><hr></td>
    </tr>
  </tbody>
    </table>
            </div>
          </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Category',
    data() {
    return {
      categories: [],
    };
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