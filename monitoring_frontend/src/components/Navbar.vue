<template>
    <nav>
      <div class="nav-container">
        <router-link class="nav-link" to="/">Home</router-link>
        <router-link class="nav-link" to="/drones">Drones</router-link>
        <router-link class="nav-link" to="/tasks/">Tasks</router-link>
        <div v-if="isLoggedIn">
          <button class="nav-link" @click="logout">Logout</button>
        </div>
        <div v-else>
          <router-link class="nav-link" to="/login">Login</router-link>
          <router-link class="nav-link" to="/register">Register</router-link>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'NavbarPage',
    computed: {
      isLoggedIn() {
        return !!sessionStorage.getItem('jwt');
      }
    },
    methods: {
      logout() {
        fetch('http://localhost:5000/auth/logout', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('jwt')}`
          }
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Logout failed');
          }
          return response.json();
        })
        .then(() => {
          sessionStorage.removeItem('jwt');
          this.$router.push('/login');
        })
        .catch(error => {
          console.error('Logout error:', error);
          alert('Logout failed: ' + error.message);
        });
      }
    }
  }
  </script>
  
  <style scoped>
  nav {
    background-color: #e0e0e0; /* Soft gray background */
    width: 100%;
    padding: 10px 0;
  }
  
  .nav-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
  }
  
  .nav-link {
    color: black;
    text-decoration: none;
    padding: 10px 20px;
    background-color: transparent; /* Clear background */
    transition: background-color 0.3s ease;
  }
  
  .nav-link:hover, .nav-link.router-link-active {
    background-color: #b0b0b0; /* Slightly darker gray for hover and active */
  }
  
  .nav-link.router-link-active {
    background-color: #909090; /* Even darker for active links */
  }
  </style>
  