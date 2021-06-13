<template>
        <section class="section">
      <div class="container is-fluid">
        <div class="mt-3">
          <div class="is-flex is-justify-content-space-between">
          <h1 class="title mb-6">Новости</h1>
          <router-link to="/add-news" class="button is-warning">Добавить новость</router-link>
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


  <div class="field is-grouped mb-6">
  <p class="control">
    <router-link :to="{name: 'EditNews', params: {id: n.id, title:n.title, body:n.body}}" class="button is-primary">Редактировать новость</router-link>
  </p>
  <p class="control">
    <button @click="del(n.id)" class="button is-danger">
      Удалить новость
    </button>
  </p>
</div>
            </div>
          </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import { toast } from "bulma-toast";

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
    del(id) {
      axios
      .delete(`api/v1/news/delete/${id}`)
      .then((response) => {
        this.getNews();
            toast({
              message: "Новость успешно удалена!",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });
          })
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