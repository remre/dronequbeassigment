<template>
    <div class="task-form">
      <h2>Create New Task</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="taskName">Task Name:</label>
          <input type="text" id="taskName" v-model="task.name" required>
        </div>
        <div>
          <label for="taskDescription">Description:</label>
          <textarea id="taskDescription" v-model="task.description" required></textarea>
        </div>
        <div>
          <label for="droneSelect">Assign Drone:</label>
          <select id="droneSelect" v-model="task.drone_id" required>
            <option v-for="drone in drones" :key="drone.id" :value="drone.id">{{ drone.model }}</option>
          </select>
        </div>
        <button type="submit">Create Task</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        task: {
          name: '',
          description: '',
          drone_id: null
        },
        drones: []
      };
    },
    mounted() {
      this.fetchDrones();
    },
    methods: {
      fetchDrones() {
        fetch('http://localhost:5000/api/drones')
          .then(response => response.json())
          .then(data => {
            this.drones = data;
            if (data.length > 0) {
              this.task.drone_id = data[0].id; 
            }
          })
          .catch(error => console.error('Error fetching drones:', error));
      },
      submitForm() {
  fetch('http://localhost:5000/api/tasks', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(this.task)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok: ' + response.statusText);
    }
    return response.json();
  })
  .then(data => {
    console.log("Received data:", data);  
    if (data && data.id) {
      alert('Task created successfully!');
      this.$router.push('/tasks/' + data.id);
    } else {
      throw new Error('Task ID is undefined');
    }
  })
  .catch(error => {
    console.error('Error creating task:', error);
    alert(error.message);
  });
}

    }
  }
  </script>
  
  <style scoped>
  .task-form {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 50px;
  }
  .task-form input, .task-form select, .task-form button {
    margin: 10px;
    padding: 10px;
    font-size: 16px;
  }
  .task-form button {
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
  .task-form button:hover {
    background-color: #45a049;
  }
  </style>
  