<template>
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
          <router-link to="/main" class="navbar-item">Главная</router-link>
          <router-link to="/category" class="navbar-item">Категории</router-link>
          <router-link to="/news" class="navbar-item">Новости</router-link>
          </div>
          <div class="navbar-item navbar-end">
            <div class="buttons">
              <a href="#" class="bvi-open button is-rounded" title="Версия сайта для слабовидящих">Для слабовидящих</a>
              <template>
                <router-link to="/manager-account" class="button is-rounded is-warning">Мой аккаунт</router-link>
              </template>
            </div>
          </div>
          </div>
      </nav>
  </header>
</template>