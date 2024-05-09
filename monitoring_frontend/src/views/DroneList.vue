<template>
  <div class="drone-list">
    <h2>Drones</h2>
    <div class="list-container">
      <div class="drone-card" v-for="drone in drones" :key="drone.id">
        {{ drone.model }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
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
        })
        .catch(error => {
          console.error('Error fetching drones:', error);
          alert('Error fetching drones: ' + error.message);
        });
    }
  }
};
</script>

<style scoped>
.drone-list {
  padding: 20px;
  font-size: 20px;
}

.drone-list h1 {
  margin-bottom: 20px;
}

.list-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.drone-card {
  width: 20%; 
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #333;
  border-radius: 5px;
}

.drone-card:hover {
  background-color: #f0f0f0;
}
</style>