<template>
<div>
  <div id="javascript-editor"></div>
</div>
</template>

<script>


export default {
  name: 'code-editor',
  props: [
    'content'
  ],
  data() {
    return {
      language: 'ruby',
      editor: {}
    }
  },
  mounted () {
    console.log('mounted')
    var ace = require('brace');
    require('brace/mode/' + this.language);
    require('brace/theme/monokai');

    this.editor = ace.edit('javascript-editor');
    this.editor.getSession().setMode('ace/mode/' + this.language);
    this.editor.setTheme('ace/theme/monokai');
  },
}
</script>

<style>

#javascript-editor {
  height: 500px;
}

</style>