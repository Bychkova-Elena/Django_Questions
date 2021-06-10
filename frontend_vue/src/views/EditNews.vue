<template>
    <section class="section">
        <div class="columns">
            <div class="column is-6 is-offset-3">
                <h1 class="title">Редактирование новости</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Заголовок: <span class="has-text-danger">*</span></label>
                        <div class="control">
                            <input type="text" class="input" v-model="title">
                        </div>
                    </div>

        <div class="field">
            <label>Текст новости: <span class="has-text-danger">*</span></label>
            <div class="control">
              <textarea
                class="textarea"
                placeholder="Текст"
                v-model="body"
              ></textarea>
            </div>
          </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                      <p class="mb-3"><span class="has-text-danger">*</span> - Поля, обязательные для заполнения</p>
                        <div class="control">
                            <button class="button is-warning">Сохранить</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import { toast } from "bulma-toast";

export default {
    name: 'EditNews',
    data() {
        return {
            title:this.$route.params.title,
            body:this.$route.params.body,
            errors: [],
            news:[],
            id:this.$route.params.id,
        }
    },
    mounted() {
        document.title = ' Редактирование новости | DjangoQuestions'
    },
    methods: {
  async submitForm() {
      this.errors = [];
      if (this.title === "") {
        this.errors.push("Не указан заголовок новости!");
      }
      if (this.body === "") {
        this.errors.push("Не указан текст новости!");
      }
      if (!this.errors.length) {
        const data = {
          title: this.title,
          body: this.body
        };

        await axios
          .put(`/api/v1/news/update/${this.id}`, data)
          .then((response) => {
            this.$router.go(-1);
            toast({
              message: "Новость изменена!",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });
          })
          .catch((error) => {
            this.errors.push("Что-то пошло не так. Попробуйте ещё раз.");
            console.log(error.response)
          });
      }
    },
  },
};
</script>