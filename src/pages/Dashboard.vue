<template>
  <div>
    <h5>Welcome back, Kevin.</h5>
    <h6><br>Solved problems:</h6>

        <span v-if="solved.length > 0"><div v-for="i in solved" class="card darken-1">
          <div class="card-content white-text">
            <span class="card-title">{{i.title.substring(0,80)}}</span>
          </div>
          <div class="card-action">
            Status: Complete
            <a class="btn" style="float: right" :href="'/#/problem/'+i.id">Open</a>
          </div>
        </div>
        </span>
        <p v-else>None yet, start on <a href="/#/problem/0">Problem 1</a></p>

        <br>
        <a href="/#/problem/0" style="background-color: #BF4141;" class="waves-effect waves-light btn">Try Problems</a>

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
    var user_id = '1'
    axios.get('//127.0.0.1:5000/users/'+user_id+'/solved/').then(function(data){
      console.log(data)
      var solved = [...new Set(data.data.solved)]
      solved.forEach(function(id){
        axios.get('//127.0.0.1:5000/problems/' + id).then(function(data) {
          console.log(data)
          vm.solved.unshift(data.data.problems)
        })
      })
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

.card {
    background-color: #292C34;
    width: 300px;
}
.card-action {
  min-height: 70px;
}

</style>