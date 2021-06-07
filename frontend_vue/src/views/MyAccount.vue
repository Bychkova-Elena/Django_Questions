<template>
        <section class="section">
            <div class="is-flex is-justify-content-space-between">
            <div class="">
                <h1 class="title">Мой аккаунт</h1>
            </div>

            <div class="">
                <button @click="logout()" class="button is-rounded is-danger">Выйти</button>
            </div>
            </div>

            <hr>

<nav class="navbar">

        <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-start">
          <router-link to="/personal-cart" class="navbar-item">Учетная запись</router-link>
          </div>
          </div>
      </nav>

          <router-view/>
    </section>
</template>

<script>
import axios from 'axios'
export default {
    name: 'MyAccount',
    mounted() {
        document.title = 'Мой аккаунт | DjangoQuestions'
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$store.commit('removeToken')
            this.$router.push('/')
        },
    }
}
</script>