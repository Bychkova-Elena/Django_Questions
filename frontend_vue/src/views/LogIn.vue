<template>
    <section class="section">
        <div class="columns">
            <div class="column is-6 is-offset-3">
                <h1 class="title">Войти</h1>

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

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                      <p class="mb-3"><span class="has-text-danger">*</span> - Поля, обязательные для заполнения</p>
                        <div class="control">
                            <button class="button is-link">Войти</button>
                        </div>
                    </div>

                    <hr>

                    Или нажмите <router-link to="/sign-up">сюда</router-link>, чтобы зарегистрироваться!
                </form>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = ' Вход | DjangoQuestions'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            const formData = {
                username: this.username,
                password: this.password
            }
            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem("token", token)
                    if (this.username == 'admin') {
                        const toPath = this.$route.query.to || '/admin-account'
                        this.$router.push(toPath)
                    }
                    else if (this.username == 'manager') {
                        const toPath = this.$route.query.to || '/manager-account/manager-news'
                        this.$router.push(toPath)
                    }
                    else {
                        const toPath = this.$route.query.to || '/my-account'
                        this.$router.push(toPath)
                    }
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Что-то пошло не так. Пожалуйста, попробуйте ещё раз!')
                        
                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>