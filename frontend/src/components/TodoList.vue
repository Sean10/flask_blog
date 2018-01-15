<template>
  <div id='TodoList'>
    <BaseInputText
            v-model="newTodoText"
            placeholder="New todo"
            @keydown.enter="addTodo"
        />
    <ul v-if="todos.length">
      <TodoListItem
        v-for="todo in todos"
        :key="todo.id"
        :todo="todo"
        @remove="removeTodo"
      />
    </ul>
    <p v-else>
      Nothing left in the list. Add a new todo in the input above.
    </p>
  </div>
</template>

<script>
  import BaseInputText from './BaseInputText.vue'
  import TodoListItem from './TodoListItem.vue'
  import qs from 'axios'

  let nextTodoId = 1

  export default {
    components: {
      BaseInputText, TodoListItem
    },
    // props: {
    //   // type: object,
    //   // required: true
    // },
    data() {
      var info = {
        newTodoText: '',

        todos: [
          {
            id: nextTodoId++,
            task: 'Learn Vue'
          },
          {
            id: nextTodoId++,
            task: 'Learn about single-file components'
          },
          {
            id: nextTodoId++,
            task: 'Fall in love'
          }
        ]
      }
      this.create();
      return info;
    },
    methods: {
      addTodo() {
        const trimmedText = this.newTodoText.trim()
        if (trimmedText) {
            // var parm = new URLSearchParams();
            // parm.append('task',trimmedText);
            // console.log(parm);
            var qs = require('qs');
            console.log(qs.stringify({'task':trimmedText}));
            this.$axios.post("/todo/api/todos/"+nextTodoId, qs.stringify({'task':trimmedText})).then(response => {
              console.log(response.data)
              console.log(response.data['id']);
              if(response.data) {
                this.todos.push({
                  id: response.data['id'],
                  task: response.data['task']
                });
              }
              // this.todos.push({id: nextTodoId, task: response.data});
            })
          this.newTodoText = ''
        }
      },
      removeTodo(idToRemove) {
        this.$axios.delete("/todo/api/todos/"+idToRemove).then(
          response => {
            console.log(response);
            console.log(response.data);
            this.todos = response.data;
          }
        )
      },
      create() {
        console.log("succeed");
        this.$axios.get("/todo/api/todos").then(response => {
          console.log(response.data);
          this.todos = response.data
        })
      }
    }
  }


</script>

<style>
  #TodoList {
    max-width: 400px;
    text-align: center;
    color: #2c3e50;
    margin: 0 auto;
    line-height: 1.4;

  }
</style>
