<template>
        <section class="section">
            <div class="is-flex is-justify-content-space-between">
            <div class="">
                <h1 class="title">Привет админ!</h1>
            </div>

            <div class="">
                <button @click="logout()" class="button is-rounded is-danger">Выйти</button>
            </div>
            </div>

            <hr>

<nav class="navbar">

        <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-start">
          <router-link to="/admin-account/admin-news" class="navbar-item">Новости</router-link>
          </div>
          </div>
      </nav>
      <router-view/>
            
    </section>
</template>

<script>
import axios from 'axios'
export default {
    name: 'AdminAccount',
    mounted() {
        document.title = 'Админ | DjangoQuestions'
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