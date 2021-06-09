<template>
        <section class="section">
      <div class="container is-fluid">
        <div class="mt-3">
          <div class="is-flex is-justify-content-space-between">
          <h1 class="title mb-6">Новости</h1>
          <router-link to="/admin-account/add-news" class="button is-warning">Добавить новость</router-link>
          </div>
          <div class="control">
          <input type="search" class="input is-warning mb-6" v-model="search" placeholder="Поиск по заголовку">
          </div>
            <div v-for="n in searchHandler" :key="n.id">
              <div class="card mb-3">
  <header class="card-header">
    <p class="card-header-title">
      {{n.title}}
    </p>
  </header>
  <div class="card-content">
    <div class="content">
     <p>{{n.body}}</p>
    </div>
  </div>
  </div>
            </div>
          </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
export default {
    name: 'News',
    data() {
    return {
      news: [],
      search:'',
    };
  },
    mounted() {
        document.title = 'Новости | DjangoQuestions',
        this.getNews()
    },
    methods: {
       getNews() {
      axios
        .get("api/v1/news/")
        .then(response => {
          this.news = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
        
    },

    computed:{
      searchHandler(){
        return this.news.filter(elem => {
          return elem.title.toLowerCase().includes(this.search.toLowerCase());
        })
      }
    }
}
</script>

<style lang="scss" scope>


</style>