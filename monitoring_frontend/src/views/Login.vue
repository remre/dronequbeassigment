<template>
    <div class="login-container">
      <h2>Login</h2>
      <input v-model="username" placeholder="Username">
      <input v-model="password" type="password" placeholder="Password">
      <button @click="login">Login</button>
    </div>
  </template>
  
  <script>
export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      fetch('http://localhost:5000/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: this.username, password: this.password })
      })
      .then(response => response.json())
      .then(data => {
        if (data.status === 'success') {
          sessionStorage.setItem('jwt', data.access_token);
          sessionStorage.setItem('username', this.username); 
      
          this.$router.push('/dashboard'); 
        } else {
          alert('Login failed: ' + data.message);
        }
      })
      .catch(error => {
        console.error('Login error:', error);
        alert('Login failed: ' + error.message);
      });
    }
  }
}
  </script>
  <style scoped>
  .login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 50px;
  }
  
  .login-container input, .login-container button {
    margin: 10px;
    padding: 10px;
    font-size: 16px;
  }
  
  .login-container button {
    background-color: #6c757d; /* Green */
    border: none;
    color: white;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    transition-duration: 0.4s;
    cursor: pointer;
  }
  
  .login-container button:hover {
    background-color: #45a049;
  }
  </style>