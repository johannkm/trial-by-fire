<template>
  <div id="app">
    <!-- <Navbar></Navbar> -->
    <div class="row main">

      <div class="col s3 m2 fake-sidebar"></div>
      <div class="col s3 m2 sidebar">
        <div class="section">
          <h4>Code Platform</h4>
          <div class="divider"></div>
          <br>
          <a class="waves-effect waves-light btn" href="/#/">Dashboard</a>
          <a class="waves-effect waves-light btn" href="/#/problem/0">Problems</a>
        </div>
      </div>

      <div class="col s9 m10">
        <router-view></router-view>
      </div>
    </div>
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
  background-color: #292C34;
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
</style>
