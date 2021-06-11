<template>
<div>
  <div class="card">
  <header class="card-header">
    <p class="card-header-title">
      {{question.question}}
    </p>
  </header>
  <div class="card-content" v-if="show">
    <div class="content">
     <strong>{{question.answer}}</strong><br>
     <small>{{question.clarification}}</small>
    </div>
  </div>
  </div>
  <div class="field is-grouped mt-3 mb-6">
    <p class="control" v-if="!show" @click="show=true">
      <button class="button is-warning">
      Показать ответ
    </button>
    </p>
    <p class="control" v-else @click="show=false">
      <button class="button is-warning">
      Скрыть ответ
    </button>
    </p>
    <p class="control">
    <button class="button is-danger">Пожаловаться</button>
    </p>
  </div>
  </div>
</template>

<script>

export default {
   props: ['question'],
   data() {
    return {
      show:false,
    };
  },

}
</script>

<style lang="scss" scoped>
@media print {

  .button {
    display:none;
  }

}
</style>
