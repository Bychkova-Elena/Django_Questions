<template>
        <section class="section">
      <div class="container is-fluid">
        <h1 class="title">Проект <span class="text-shadow">"DgangoQuestions"</span></h1>
        <h3 class="subtitle mt-3">Поможет тебе найти вопросы и ответы по конкретной области</h3>
        <div class="main-content">
          <h5 class="is-size-5 mb-3 mt-6 underline">Типы пользователей</h5>
          <div class="columns">
            <div class="column">
          <div class="card linear">
  <header class="card-header">
    <p class="card-header-title">
      Администратор
    </p>
  </header>
  <div class="card-content">
    <div class="content">
      Логин: admin
      <br>
      Пароль: admin
    </div>
  </div>
</div>
</div>

<div class="column">
          <div class="card linear">
  <header class="card-header">
    <p class="card-header-title">
      Менеджер
    </p>
  </header>
  <div class="card-content">
    <div class="content">
      Логин: manager
      <br>
      Пароль: manager
    </div>
  </div>
</div>
</div>

<div class="column">
          <div class="card linear">
  <header class="card-header">
    <p class="card-header-title">
      Незарегистрированный/зарегистрированный пользователь
    </p>
  </header>
  <div class="card-content">
    <div class="content">
      Пользователь может сам зарегистрироваться и войти
    </div>
  </div>
</div>
</div>
</div>


          <h5 class="is-size-5 mb-3 mt-6 underline">Функционал</h5>
                    <div class="columns mb-6">
            <div class="column">
          <strong>Любой пользователь может:</strong>
          <ul>
            <li class="li-style">просматривать вопросы по выбранной категории;</li>
            <li class="li-style">фильтровать вопросы по сложности;</li>
            <li class="li-style">распечатать страницу со списком вопросов;</li>
            <li class="li-style">использовать версию сайта для слабовидящих</li>
          </ul>
      </div>
          <div class="column">
            <strong>Менеджер может:</strong>
            <ul>
            <li class="li-style">просматривать/добавлять/редактировать/удалять новости;</li>
            <li class="li-style">искать новости по названию</li>
          </ul>
          </div>
          </div>
        </div>
        <img class="question-picture mt-6" src="../assets/logo.png" alt="question">
        </div>
    </section>
</template>

<script>
import axios from 'axios'


export default {
    name: 'Main',
    data() {
    return {

    };
  },
    mounted() {
        document.title = ' Главная | DjangoQuestions'
}
}
</script>

<style lang="scss" scope>
.linear {
  background-image: linear-gradient(#3298dc 5%, #ffdd57 90%, #fadb5e);
}
.li-style {
  position: relative;
  margin-left:1.5rem;
  margin-top:0.5rem;
  &:before {
  content: '';
  background-image: url('../assets/list-style.png');
  position: absolute;
  width: 16px;
  height: 16px;
  background-size: 16px 16px;
  left: -22px; 
  top: 1px;
}
}
//Контуры
.text-shadow {
  text-shadow:
    -1px -1px #FFF,
    -2px -2px #FFF,
    -1px 1px #FFF,
    -2px 2px #FFF,
    1px 1px #FFF,
    2px 2px #FFF,
    1px -1px #FFF,
    2px -2px #FFF,
    -3px -3px 2px #BBB,
    -3px 3px 2px #BBB,
    3px 3px 2px #BBB,
    3px -3px 2px #BBB;
  color: #3298dc;
  transition: all 1s;
  &:hover {
  color: #ffdd57;
}
}

//Живое подчеркивание
.underline {
  display: inline-block;
  text-shadow:
    1px 1px 1px white,
    1px -1px 1px white,
    -1px 1px 1px white,
    -1px -1px 1px white;
  transition: all 1s;
  &:after {
  content: "";
  display: block;
  position: relative;
  z-index: -1;
  width: 100%;
  margin: auto;
  border-bottom: 3px solid #3298dc;
  bottom: .15em;
  transition: all 1s;
}
  &:hover:after {
  width: 0%;
  border-bottom-width: 1px;
}
}
.main-content{
  margin-bottom:12rem;
}
.question-picture{
  width:3rem;
  margin-bottom:-10rem;
  position:absolute;
  animation: bounce 0.7s linear infinite, 
    moveLeft 17s linear infinite alternate;
}


@keyframes bounce {
  0% { bottom: 3rem; }
  25% { bottom:0;}
  30% { bottom:0;}
  35% { bottom:0;}
  70% { bottom:3rem;}
  100% { bottom:3rem; }
}

@keyframes moveLeft {
  from {left: 0;}
  to   {left: 100%;}
} 
</style>