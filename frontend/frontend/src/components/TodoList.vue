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

  let nextTodoId = 1

  export default {
    components: {
      BaseInputText, TodoListItem
    },
    // props: {
    //   type: object,
    //   required: true
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
            this.$axios.post("http://localhost:5000/todo/"+nextTodoId, {
              params: {
                task: trimmedText
              }
            }).then(response => {
              console.log(response.data['id']);
              this.todos.push({
                id: response.data['id'],
                text: response.data['task']
              });
              // this.todos.push({id: nextTodoId, task: response.data});
            })
          this.newTodoText = ''
        }
      },
      removeTodo(idToRemove) {
        this.$axios.delete("http://localhost:5000/todo/"+idToRemove, {
          params: {id: idToRemove}
      }).then(
          response => {
            console.log(response.data);
            this.todos = response.data;
          }
        )
        this.todos = this.todos.filter(todo => {
          return todo.id !== idToRemove
        })
      },
      create() {
        console.log("succeed");
        this.$axios.get("http://localhost:5000/todo/").then(response => {
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
