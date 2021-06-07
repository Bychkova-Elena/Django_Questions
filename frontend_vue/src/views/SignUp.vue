<template>
<section class="section">
  <div class="columns">
     <div class="column is-6 is-offset-3">
       <h1 class="title">Регистрация</h1>
                       <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Логин: <span class="has-text-danger">*</span></label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Пароль: <span class="has-text-danger">*</span></label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="field">
                        <label>Повторите пароль: <span class="has-text-danger">*</span></label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                      <p class="mb-3"><span class="has-text-danger">*</span> - Поля, обязательные для заполнения</p>
                        <div class="control">
                            <button class="button is-link">Зарегистрироваться</button>
                        </div>
                    </div>

                    <hr>

                    Или нажмите <router-link to="/log-in">сюда</router-link>, чтобы войти!
                </form>
     </div>

  </div>
</section>
</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

export default {
data() {
    return {
      username:'',
      password:'',
      password2:'',
      errors:[]
  }
},
mounted() {
        document.title = 'Регистрация | DjangoQuestions'
    },
 methods: {
        submitForm() {
            this.errors = []
            if (this.username === '') {
                this.errors.push('Введите логин')
            }
            if (this.password === '') {
                this.errors.push('Пароль слишком короткий')
            }
            if (this.password !== this.password2) {
                this.errors.push('Пароли не совпадают')
            }
            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }
                axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        toast({
                            message: 'Аккаунт создан, войдите!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Что-то пошло не так. Попробуйте ещё раз')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
}
</script>