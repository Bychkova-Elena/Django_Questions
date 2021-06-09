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
      <button class="button is-warning mt-3 mb-6" v-if="!show" @click="show=true">
      Показать ответ
    </button>
      <button class="button is-warning mt-3 mb-6" v-else @click="show=false">
      Скрыть ответ
    </button>
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
