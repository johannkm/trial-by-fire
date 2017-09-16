<template>
    <div>
        <h3 class="is-size-3">Problem #{{$route.params.id}}</h3>
        <CodeEditor></CodeEditor>
        <br>
        <a class="button is-primary" @click="content='no'">Submit</a>
    </div>
</template>

<script>
import CodeEditor from '@/components/CodeEditor'

var firebase = require('firebase')
var config = {
  apiKey: "AIzaSyBO0-1WCTbu1xOLTy9qD1Fswf_w6ejNmeo",
  authDomain: "code-inter.firebaseapp.com",
  databaseURL: "https://code-inter.firebaseio.com"
};
firebase.initializeApp(config);
var database = firebase.database().ref();

export default {
  name: 'code-problem',
  components: {
      CodeEditor
  },
  data(){
      return{
        content: 'hello world'
      }
  },
  events: {
    codeChanged(newContent){
      this.content = newContent
    }
  },
  moounted: {
    
  }
}
</script>
