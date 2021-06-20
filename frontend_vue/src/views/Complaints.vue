<template>
      <section class="section">
      <div class="container is-fluid">
        <div class="mt-3">
          <h1 class="title mb-6">Жалобы</h1>
            <Complaint 
                v-for="complaint in complaints" :key="complaint.id"
                :complaint="complaint" />
            <p v-if="!complaints.length">Жалоб не найдено</p>
          </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import Complaint from '@/components/Complaint'

export default {
    name: 'Complaints',
    data() {
    return {
      complaints:[]

    };
  },
      components: {
        Complaint
    },
    mounted() {
        document.title = 'Список жалоб | DjangoQuestions',
        this.getComplaints()
    },
    methods: {
          async getComplaints() {
        this.$store.commit('setIsLoading', true)
     await axios
        .get("/api/v1/complaints/")
        .then(response => {
          this.complaints = response.data;
        })
        .catch(error => {
          console.log(error);
        });
        this.$store.commit('setIsLoading', false)
    },
    },
}
</script>

<style lang="scss" scope>

</style>