<template>
    <div class="dashboard-container">
      <h1>Dashboard</h1>
      <div v-if="loggedIn">
        <h2>Username:</h2>
        <p>{{ username }}</p>
      
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DashboardPage',
    data() {
      return {
        username: '',
        accessToken: '',
        loggedIn: false,
      };
    },
    created() {
      this.username = sessionStorage.getItem('username');
      this.accessToken = sessionStorage.getItem('jwt');
      this.loggedIn = !!this.accessToken;
    },
  }
  </script>