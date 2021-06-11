<template>
        <section class="section">
      <div class="container is-fluid">
        <div class="mt-3">
          <h1 class="title mb-6">Новости</h1>
            <div v-for="n in news" :key="n.id">
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
  <div class="is-flex is-justify-content-flex-end">
  <button class="button mb-6 is-warning">Оставить комментарий</button>
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
        
    }
}
</script>

<style lang="scss" scope>


</style>