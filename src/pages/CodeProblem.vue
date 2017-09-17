<template>
  <div>
    <div class="section">
      <h5>{{problem.title}}&nbsp;&nbsp;&nbsp;
      <span class="chip">
        {{problem.difficulty}}
      </span></h5>

      <ul class="collapsible" data-collapsible="expandable">
        <li>
          <div class="collapsible-header active">Question</div>
          <div class="collapsible-body">
            <p>{{problem.input}}</p>
            <p>{{problem.output}}</p>
            <p v-if="problem.constraints">
              <span v-for="c in problem.constraints">{{c}}<br></span>
            </p>
          </div>
        </li>
        <li>
          <div class="collapsible-header">Code Editor</div>
          <div class="collapsible-body no-pad">
                  <codemirror v-model="content" :options="editorOptions"></codemirror>

            </div>
        </li>
        <li>
          <div class="collapsible-header">Test cases</div>
          <div class="collapsible-body no-pad">
                  <codemirror v-model="testCases" :options="testCaseOptions"></codemirror>
            </div>
        </li>
        <li>
          <div class="collapsible-header">Results</div>
          <div class="collapsible-body no-pad">
            <div id="console">
              <div id="inner-console">
                <span v-if="results == null">No results yet.</span>
                <pre v-else>{{results.results}}<br>Runtime: {{results.runtime}}s</pre>
              </div>
            </div>
          </div>
        </li>
      </ul>
    </div>
    <div>
    <a class="waves-effect waves-light btn" @click="submitCode">Submit</a>
    <span>&nbsp;&nbsp;&nbsp;</span>
    <a class="waves-effect waves-light btn btn-gray" @click="moveProblems(-1)">Previos</a>
    <a class="waves-effect waves-light btn btn-gray" @click="moveProblems(1)">Next</a>
    </div>
    <br><br>
  </div>
</template>

<script>
var firebase = require('firebase')
var axios = require('axios')

var config = {
  apiKey: "AIzaSyBO0-1WCTbu1xOLTy9qD1Fswf_w6ejNmeo",
  authDomain: "code-inter.firebaseapp.com",
  databaseURL: "https://code-inter.firebaseio.com",
  projectId: "code-inter",
  storageBucket: "code-inter.appspot.com",
  messagingSenderId: "176420991126"
};
firebase.initializeApp(config);

// require active-line.js
// require('codemirror/addon/selection/active-line.js')
// styleSelectedText
// require('codemirror/addon/selection/mark-selection.js')
// require('codemirror/addon/search/searchcursor.js')
// hint
// require('codemirror/addon/hint/show-hint.js')
// require('codemirror/addon/hint/show-hint.css')
// require('codemirror/addon/hint/javascript-hint.js')
// require('codemirror/addon/selection/active-line.js')
// highlightSelectionMatches
require('codemirror/addon/scroll/annotatescrollbar.js')
require('codemirror/addon/search/matchesonscrollbar.js')
require('codemirror/addon/search/searchcursor.js')
// require('codemirror/addon/search/match-highlighter.js')
// keyMap
require('codemirror/mode/clike/clike.js')
require('codemirror/addon/edit/matchbrackets.js')
require('codemirror/addon/comment/comment.js')
require('codemirror/addon/dialog/dialog.js')
require('codemirror/addon/dialog/dialog.css')
require('codemirror/addon/search/searchcursor.js')
require('codemirror/addon/search/search.js')
require('codemirror/keymap/sublime.js')
// foldGutter
// require('codemirror/addon/fold/foldgutter.css')
// require('codemirror/addon/fold/brace-fold.js')
// require('codemirror/addon/fold/comment-fold.js')
// require('codemirror/addon/fold/foldcode.js')
// require('codemirror/addon/fold/foldgutter.js')
// require('codemirror/addon/fold/indent-fold.js')
// require('codemirror/addon/fold/markdown-fold.js')
// require('codemirror/addon/fold/xml-fold.js')


export default {
  name: 'code-problem',
  data() {
    return {
      problem: {},
      content: '',
      testCases: '',
      results: null,
      editorOptions: {
        tabSize: 2,
        styleActiveLine: false,
        lineNumbers: true,
        line: true,
        foldGutter: true,
        styleSelectedText: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
        highlightSelectionMatches: { showToken: /\w/, annotateScrollbar: true },
        mode: 'text/x-python',
        hintOptions: {
          completeSingle: false
        },
        keyMap: "sublime",
        matchBrackets: true,
        showCursorWhenSelecting: true,
        theme: "monokai",
        extraKeys: { "Ctrl": "autocomplete" }
      },
      testCaseOptions: {
        tabSize: 2,
        styleActiveLine: false,
        lineNumbers: true,
        line: true,
        foldGutter: true,
        styleSelectedText: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
        highlightSelectionMatches: { showToken: /\w/, annotateScrollbar: true },
        mode: 'text/plain',
        hintOptions: {
          completeSingle: false
        },
        keyMap: "sublime",
        matchBrackets: true,
        showCursorWhenSelecting: true,
        theme: "monokai",
        extraKeys: { "Ctrl": "autocomplete" }
      }
    }
  },
  beforeRouteUpdate(to, from, next) {
    next()
    this.newQuestion(to.params.id)
    console.log('update' + to.params.id)
  },
  created() {
    this.newQuestion(this.$route.params.id)
    console.log('created ' + this.$route.params.id)
  },
  watch: {
    content: function(newContent) {
      firebase.database().ref('/solutions/' + this.$route.params.id).set({
        'content': newContent
      })
    }
  },
  methods: {
    newQuestion(id) {
      this.results = null
      this.problem = {}
      var vm = this
      firebase.database().ref('/solutions/' + id + '/content').once('value').then(function(snapshot) {
        if (snapshot.val()) {
          vm.content = snapshot.val()
        } else {
          vm.content = ''
        }
      })

      axios.get('//127.0.0.1:5000/problems/' + id).then(function(data) {
        console.log('here')
        vm.problem = data.data.problems
        console.log(data)
      }).catch(function(error){
        console.error(error)
        vm.$router.push('/')
      })
    },
    submitCode() {
      var vm = this
      var user_id = '12345678'
      var problem_id = this.$route.params.id
      axios.post('//127.0.0.1:5000/users/' + user_id + '/submissions/' + problem_id, {
        code: vm.content.replace(/"/g, "'").split("\n")
      }).then(function(data) {
        console.log(data)
        vm.results = data.data.submission[0]
      })
    },
    moveProblems(direction) {
      this.$router.push('/problem/'+(parseInt(this.$route.params.id)+direction))
    }
  }
}

</script>

<style>
.CodeMirror {
  /* border-style: solid;
  border-width: 1px; */
}

.CodeMirror,
.CodeMirror-linenumbers {
  background-color: #000!important;
  /* border-color: black; */
}

#console {
  background-color: black;
}
#inner-console {
  padding: 10px;
}

.collapsible-header{
  background-color: #3C3F46;
}
.no-pad {
  padding: 0;
}

.btn-gray {
  background-color: gray;
}
.btn-gray:hover {
  background-color: lightgray;
}

#app > div > div.col.s9.m10 > div > div.section > ul > li > div.collapsible-body {
  display: block;
}

#app > div > div.col.s9.m10 > div > div.section > ul > li > div.collapsible-header {
  cursor: auto;
}

#app > div > div.col.s9.m10 > div > div.section > ul > li:nth-child(3) > div.collapsible-body.no-pad > div {
  height: 200px;
}
</style>
