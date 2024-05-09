<template>
    <div class="task-list">
      <h2>Task List</h2>
      <div class="list-container">
        <div class="task-card" v-for="task in tasks" :key="task.id">
          <router-link :to="`/tasks/${task.id}`">{{ task.name }}</router-link>
        </div>
      </div>
      <router-link to="/tasks/new">Create New Task</router-link>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        tasks: []
      };
    },
    created() {
      this.fetchTasks();
    },
    methods: {
        fetchTasks() {
  fetch('http://localhost:5000/api/tasks')
    .then(response => response.json())
    .then(data => {
      this.tasks = data;
    })
    .catch(error => {
      console.error('Error fetching tasks:', error);
      alert('Error fetching tasks: ' + error.message);
    });
}
    }
  }
  </script>

<style scoped>
.task-list {
  padding: 20px;
  font-size: 20px;
}

.task-list h1 {
  margin-bottom: 20px;
}

.task-list a {
  color: black;
  text-decoration: none;
}

.task-list a:hover {
  text-decoration: underline;
}
.list-container {
  width: 50%;
  margin: 0 auto; 
}
.task-list a:hover {
  text-decoration: underline;
}

.list-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.task-card {
  width: 40%; 
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #333;
  border-radius: 5px;
}

.task-card:hover {
  background-color: #f0f0f0;
}
</style>