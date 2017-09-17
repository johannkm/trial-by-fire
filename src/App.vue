<template>
  <div id="app">
    <!-- <Navbar></Navbar> -->
    <div class="row main">

      <div class="col s3 m2 fake-sidebar"></div>
      <div class="col s3 m2 sidebar">
        <div style="text-align:center" class="section">
          <h5 id="title"><span style="color:red">//</span>trialbyfire</h5>
          <br>
          <div id="bar" class="divider"></div>
          <br>
          <a class="waves-effect waves-light btn" style="text-transform:lowercase" href="/#/">Dashboard</a>
          <a class="waves-effect waves-light btn" style="text-transform:lowercase" href="/#/problem/0">Problems</a>
        </div>
      </div>

      <div class="col s9 m10">
        <router-view></router-view>
      </div>
    </div>
    <notifications group="submit" position="bottom right" />
    </div>
</template>

<script>
import Navbar from '@/components/Navbar'

export default {
  name: 'app',
  components: {
    Navbar
  }
}
</script>

<style>
html {
  background-color: #17181D;
  color: white;
}

html, body, #app, .row, .sidebar {
  height: 100%;
}

nav {
  background-color: #747C92;
  color: white;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.main {
  margin-bottom: 0;
}

.sidebar {
  background: #000000;
  height: 100%;
  position: fixed;
  top: 0;
}
#app > div > div.col.m2.sidebar > div > a {
  margin-top: 10px;
  width: 100%;
  background-color: #191919;
}

.my-style {
  background: #4183D7;
}

div ul {
  border-color: #76787D!important;
}

#bar {
  background-color: #76787D;
}
</style>
