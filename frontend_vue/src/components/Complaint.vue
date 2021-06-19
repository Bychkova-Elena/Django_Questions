<template>
<div>
  <div class="card">
  <div class="card-content">
    <div class="content">
     <p>{{complaint.complaint}}</p>
     <p>Статус: {{complaint.status}}</p>
    </div>
    <div class="content"  v-if="show">
      <div v-for="question in questions" :key="question.id">
        <div v-if="complaint.question == question.id">
          <hr>
     <p><strong>Вопрос:</strong> {{question.question}}</p>
     <p><strong>Ответ:</strong> {{question.answer}}</p>
     <p><strong>Пояснение:</strong> {{question.clarification}}</p>
        </div>
      </div>
    </div>
  </div>
  </div>
  <div class="field is-grouped mt-3 mb-6">
    <p class="control" v-if="!show" @click="show=true">
      <button class="button is-warning">
      Показать вопрос
    </button>
    </p>
    <p class="control" v-else @click="show=false">
      <button class="button is-warning">
      Скрыть вопрос
    </button>
    </p>
    <p class="control">
    <button class="button is-primary">Изменить статус</button>
    </p>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
   props: ['complaint'],
   data() {
    return {
      show:false,
      questions:[]
    };
  },

    mounted() {
        this.getQuestions()
    },
    methods: {

      async getQuestions() {
        this.$store.commit('setIsLoading', true)
     await axios
        .get("/api/v1/questions/")
        .then(response => {
          this.questions = response.data;
        })
        .catch(error => {
          console.log(error);
        });
        this.$store.commit('setIsLoading', false)
    },
    },
}
</script>

<style lang="scss" scoped>

</style>
