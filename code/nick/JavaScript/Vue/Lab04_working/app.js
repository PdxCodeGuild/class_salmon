Vue.component('task-item', {
  template: '\
    <li>\
      {{ title }}\
      <button v-on:click="$emit(\'remove\')">Remove</button>\
    </li>\
  ',
  props: ['title']
})

new Vue({
  el: '#app',
  data: {
    newTaskText: '',
    tasks: [
    ],
    nextTaskId: 1
  },
  methods: {
    addNewTask: function () {
      this.tasks.push({
        id: this.nextTaskId++,
        title: this.newTaskText
      })
      this.newTaskText = ''
    }
  }
})