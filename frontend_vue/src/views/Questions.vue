<template>
        <section class="section">
      <div class="container is-fluid">
        <div class="mt-3">

          <nav class="breadcrumb" aria-label="breadcrumbs">
  <ul>
    <li><router-link to="/category" class="">Категории</router-link></li>
    <li><router-link :to="{name: 'Subcategory', params: {id: this.id}}" class="">Категория "{{ name }}"</router-link></li>
    <li class="is-active"><router-link :to="{name: 'Questions', params: {id2: this.id2}}" class="">Подкатегория "{{ name2 }}"</router-link></li>
  </ul>
</nav>


          <h1 class="title mb-6">Список вопросов</h1>
          <div class="filter">
          <p class="label">Выберите сложность:</p>
          <div class="select is-warning mb-6">
          <select v-model="filter"> 
          <option value="every" selected>Все</option>
          <option value="simple">Простые</option>
          <option value="complicated">Сложные</option>
          </select>
          </div>
          </div>
                        <Question 
                v-for="question in questionsFilter" :key="question.id"
                :question="question" />
          <p v-if="!questionsFilter.length">Вопросов не найдено</p>
          </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import Question from '@/components/Question'

export default {
    name: 'Questions',

    components: {
        Question
    },
    data() {
    return {
      id:this.$route.params.id,
      id2:this.$route.params.id2,
      name:"",
      name2:"",
      subcategories: [],
      categories: [],
      questions:[],
      filter:'every',
    };
  },
    mounted() {
        document.title = 'Список вопросов | DjangoQuestions',
        this.getSubcategories(),
        this.getCategories(),
        this.getQuestions()
    },
    methods: {
   async getCategories() {
     this.$store.commit('setIsLoading', true)
     await axios
        .get("api/v1/categories/")
        .then(response => {
          this.categories = response.data;
          this.name = this.categories[this.id-1].nameCategory;
        })
        .catch(error => {
          console.log(error);
        });

        this.$store.commit('setIsLoading', false)
    },


      async getSubcategories() {
        this.$store.commit('setIsLoading', true)
     await axios
        .get(`/api/v1/categories/${this.id}`)
        .then(response => {
          this.subcategories = response.data;
          this.name2 = this.subcategories[this.id2-1].nameSubcategory;
        })
        .catch(error => {
          console.log(error);
        });
        this.$store.commit('setIsLoading', false)
    },

      async getQuestions() {
        this.$store.commit('setIsLoading', true)
     await axios
        .get(`/api/v1/subcategories/${this.id2}`)
        .then(response => {
          this.questions = response.data;
        })
        .catch(error => {
          console.log(error);
        });
        this.$store.commit('setIsLoading', false)
    },
    },

    computed:{
      questionsFilter(){
        if (this.filter == 'simple') {
          return this.questions.filter(elem => {
          return elem.complexity == "SIMPLE";
        })
        }
        else if (this.filter == 'complicated') {
          return this.questions.filter(elem => {
          return elem.complexity == "COMPLICATED";
        })
        }
        else return this.questions;
      }
    }
}
</script>

<style lang="scss" scope>
select{
  width:25rem;
}

@media print {

  .filter {
    display:none;
  }

}

</style>