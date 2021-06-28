<template>
<div>
  <Header/>
    <section class="section">
        <div class="columns">
            <div class="column is-6 is-offset-3">
                <h1 class="title">Создание жалобы</h1>

                <form @submit.prevent="submitForm">

        <div class="field">
            <label>Введите важу жалобу: <span class="has-text-danger">*</span></label>
            <div class="control">
              <textarea
                class="textarea"
                placeholder="Текст"
                v-model="complaint"
              ></textarea>
            </div>
          </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                      <p class="mb-3"><span class="has-text-danger">*</span> - Поля, обязательные для заполнения</p>
                        <div class="control">
                            <button class="button is-danger">Пожаловаться</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </section>
      <Footer/>
</div>
</template>

<script>
import axios from 'axios'
import { toast } from "bulma-toast";
import Footer from '@/components/Footer'
import Header from '@/components/Header'

export default {
    name: 'AddNews',
    data() {
        return {
            question: this.$route.params.id,
            complaint: '',
            errors: []
        }
    },
            components: {
        Footer,
        Header
    },
    mounted() {
        document.title = ' Создание жалобы | DjangoQuestions'
    },
    methods: {
  async submitForm() {
      this.errors = [];
      if (this.complaint === "") {
        this.errors.push("Введите вашу жалобу!");
      }
      if (!this.errors.length) {
        const data = {
          complaint: this.complaint,
          question: this.question
        };

        await axios
          .post("/api/v1/complaints/create/", data)
          .then((response) => {
            this.$router.push('/');
            toast({
              message: "Ваша жалоба успешно отправлена!",
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