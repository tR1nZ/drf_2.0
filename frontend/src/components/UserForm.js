import React from 'react'

class UserForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {username: '', email: ''}
    }
    handleChange(event)
    {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }
    handleSubmit(event) {
        console.log(this.state.username)
        console.log(this.state.email)
        event.preventDefault()
    }
    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                    <div className="form-group">
                        <label for="login">username</label>
                            <input type="text" className="form-control" name="username" value={this.state.username} onChange={(event)=>this.handleChange(event)} />
                    </div>
                <div className="form-group">
                    <label for="email">author</label>
                    <input type="number" className="form-control" name="email" value={this.state.email} onChange={(event)=>this.handleChange(event)} />
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}
export default UserForm
