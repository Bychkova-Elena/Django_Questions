<template>
        <section class="section">
            <div class="is-flex is-justify-content-space-between">
            <div class="">
                <h1 class="title">Привет менеджер!</h1>
            </div>

            <div class="">
                <button @click="logout()" class="button is-rounded is-danger">Выйти</button>
            </div>
            </div>

            <hr>

<nav class="navbar">

        <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-start">
          <router-link to="/manager-account/manager-news" class="navbar-item">Новости</router-link>
          <router-link to="#" class="navbar-item">Жалобы</router-link>
          </div>
          </div>
      </nav>
      <router-view/>
            
    </section>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ManagerAccount',
    mounted() {
        document.title = 'Менеджер | DjangoQuestions'
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$store.commit('removeToken')
            this.$router.push('/main')
        },
    }
}
</script>