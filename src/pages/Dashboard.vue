<template>
  <div>
    <h4>Kevin's Dashboard</h4>
    <h5><br>Solved problems:</h5>

        <span v-if="solved.length > 0"><div v-for="i in solved" class="card darken-1">
          <div class="card-content white-text">
            <span class="card-title">Card Title</span>
            <p>I am a very simple card. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.</p>
          </div>
          <div class="card-action">
            Progress
          </div>
        </div>
        </span>
        <p v-else>None yet, start on <a href="/#/problem/0">Problem 1</a></p>

        <br>
        <a href="/#/problems/0" class="waves-effect waves-light btn">Try Problems</a>

  </div>
</template>

<script>
var axios = require('axios')
export default {
  name: 'dashboard',
  data(){
    return{
      solved: []
    }
  },
  mounted(){
    var vm = this
    var user_id = '12345678'
    axios.get('//127.0.0.1:5000/users/'+user_id+'/solved/').then(function(data){
      console.log(data)
    })
  }
}
</script>

<style scoped>
#app > div > div.col.s9.m10 > div > div {
  background-color: #3C3F46!important;
  width: 300px;
  display: inline-block;
  margin-right: 10px;
}

</style>