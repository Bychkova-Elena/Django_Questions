<template>
  <div id="wrapper">
    <header>
    <nav class="navbar p-4 is-info">
      <div class="navbar-brand">
        <router-link to="/" class=" hov navbar-item is-size-4"><strong>DjangoQuestions</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu=!showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          </a>
        </div>

        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-start">
          <router-link to="/" class="navbar-item">Главная</router-link>
          <router-link to="/category" class="navbar-item">Категории</router-link>
          <router-link to="/news" class="navbar-item">Новости</router-link>
          </div>
          <div class="navbar-item navbar-end">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-rounded is-warning">Мой аккаунт</router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-rounded is-warning">Вход/Регистрация</router-link>
              </template>
            </div>
          </div>
          </div>
      </nav>
  </header>

  <router-view/>

  <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data(){
    return{
      showMobileMenu: false,
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
}
</script>
