<template>
    <div class="register-container">
      <h2>Register</h2>
      <input v-model="username" placeholder="Username">
      <input v-model="password" type="password" placeholder="Password">
      <select v-model="role">
        <option disabled value="">Please select one</option>
        <option>observer</option>
        <option>executioner</option>
      </select>
      <button @click="register">Register</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'RegisterPage',
    data() {
      return {
        username: '',
        password: '',
        role: '' 
      };
    },
    methods: {
  register() {
    fetch('http://localhost:5000/auth/register', {  
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: this.username,
        password: this.password,
        role: this.role
      })
    })
    .then(response => {
      if (!response.ok) {
        return response.json().then(err => { throw new Error(err.message || 'Network response was not ok') });
      }
      return response.json();
    })
    .then(data => {
      alert(data.message);  
      if (data.message === 'Registration successful!') {
        this.$router.push('/login');  
      }
    })
    .catch(error => {
      console.error('Registration error:', error);
      alert('Registration failed: ' + error.message);
    });
  }
}
  }
  </script>
  

  
  <style scoped>
.register-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 50px;
}

.register-container input, .register-container select, .register-container button {
  margin: 10px;
  padding: 10px;
  font-size: 16px;
}

.register-container button {
  background-color:  #4CAF50;
  border: none;
  color: white;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  transition-duration: 0.4s;
  cursor: pointer;
}

.register-container button:hover {
  background-color: #45a049;
}
</style>