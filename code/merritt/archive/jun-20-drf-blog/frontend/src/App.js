import React from 'react';
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { todos: [] };
  }

  componentDidMount () {
    this.getTodos();
  }

  getTodos() {
    axios({
      method: 'get',
      url: 'http://localhost:8000/api/v1/posts/'
    }).then(res => {
      this.setState({todos: res.data});
    })
  }

  render() {
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <h3>{item.author_detail.username}</h3>
            <h3>{item.created}</h3>
            <p>{item.body}</p>
          </div>
        ))}
      </div>
    )
  }
}

export default App;