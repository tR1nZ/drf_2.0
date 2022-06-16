import React from 'react'
import UserList from './components/User.js'
import {HashRouter, Route, Link, Switch, Redirect} from 'react-router-dom'


const NotFound404 = ({ location }) => {
  return (
    <div>
      <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
} 
  

class App extends React.Component {

  constructor(props) {
    super(props)
    const user1 = {username: 'grin', first_name: 'Грин', last_name: '', email: 'grinnn'}
    const user2 = {username: 'pushkin', first_name: 'Пушкин', last_name: '', email: 'pushkinnn'}
    const users = [user1, user2]
    this.state = {
      'users': users,
    }
  }
  render() {
    return (
      <div className="App">
        <BrowserRouter>
          <HashRouter>
          <nav>
            <ul>
              <li>
              <Link to='/'>Users</Link>
              </li>
            </ul>
          </nav>
            <Switch>
              <Route exact path='/' component={() => <UserList items={this.state.users} />} />
              <Route component={NotFound404} />          
              <Redirect from='/users' to='/' />
            </Switch>        
          </HashRouter>
        </BrowserRouter>
      </div>
    )
  }
}

export default App;

