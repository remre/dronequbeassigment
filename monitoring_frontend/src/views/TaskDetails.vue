<template>
  <div class="task-details">
    <h2>Task Details</h2>
    <div v-if="task">
      <p><strong>Name:</strong> {{ task.name }}</p>
      <p><strong>Description:</strong> {{ task.description }}</p>
      <p><strong>Drone ID:</strong> {{ task.drone_id }}</p>
      <div>
        <p v-if="images.length > 0" class="executed-message">Task is executed already.</p>
        <h3>Images:</h3>
        <img v-for="image in images" :src="'http://localhost:5000/' + image.image_data" :alt="'Image ' + image.id" :key="image.id">
      </div>
    </div>
    <!-- Execute Task button is only active if the user is an executioner and the task is executable -->
    <button v-if="userRole === 'executioner' && isExecutable" @click="executeTask">Execute Task</button>
    <button v-else disabled>Execute Task</button>
  </div>
</template>

<script>
export default {

  data() {
    return {
      task: null,
      images: [],
      userRole: null, 
    };
  },
  computed: {
    isExecutable() {
      return this.images.length === 0;
    },
  },
  methods: {
    
    fetchTaskDetails() {
      const taskId = this.$route.params.id;
    fetch(`http://localhost:5000/api/tasks/${taskId}`)
      .then(response => response.json())
      .then(data => {
        this.task = data;
        this.fetchImages();
      })
      .catch(error => {
        console.error('Error fetching task details:', error);
        alert('Error fetching task details: ' + error.message);
      });
  },
    fetchImages() {
      const taskId = this.$route.params.id;
      fetch(`http://localhost:5000/api/tasks/${taskId}/images`)
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch images');
            return response.json();
        })
        .then(data => {
            this.images = data;
        })
        .catch(error => {
            console.error('Error fetching images:', error);
            alert('Error fetching images: ' + error.message);
        });
    },
    executeTask() {
  const taskId = this.$route.params.id;
  if (!this.isExecutable) {
    alert('Task has already been executed.');
    return;
  }
  fetch(`http://localhost:5000/api/tasks/${taskId}/execute`, { method: 'POST' })
    .then(response => {
      if (!response.ok) throw new Error('Task execution failed');
      return response.json();
    })
    .then(() => {
      alert('Task executed successfully');
      this.fetchImages(); 
    })
    .catch(error => {
      console.error('Error executing task:', error);
      alert('Error executing task: ' + error.message);
    });
},
    fetchUserRole() {
      fetch('http://localhost:5000/auth/role', {
        headers: {
          'Authorization': `Bearer ${sessionStorage.getItem('jwt')}`
        }
      })
      .then(response => response.json())
      .then(data => {
        this.userRole = data.role;
      })
      .catch(error => {
        console.error('Error fetching user role:', error);
      });
    }
  },
  created() {
 
  this.fetchUserRole();
  this.fetchTaskDetails();
}
}
</script>

<style scoped>
.task-details {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 50px;
}

.task-details p, .task-details h3, .task-details button {
  margin: 10px;
  padding: 10px;
  font-size: 16px;
}

.task-details button {
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



.executed-message {
  color: red;
}
</style>