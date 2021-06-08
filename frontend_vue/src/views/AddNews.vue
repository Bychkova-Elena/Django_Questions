<template>
    <section class="section">
        <div class="columns">
            <div class="column is-6 is-offset-3">
                <h1 class="title">Добавление новости</h1>

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
                            <button class="button is-warning">Добавить</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
export default {
    name: 'AddNews',
    data() {
        return {
            title: '',
            body: '',
            errors: []
        }
    },
    mounted() {
        document.title = ' Добавление новости | DjangoQuestions'
    },
    methods: {


    }
}
</script>