import React from 'react'

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.email}
            </td>
            <td>
                <button onClick={()=>deleteUser(item.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <div>
        <table>
            <th>
                Username
            </th>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Email
            </th>
            {users.map((user) => <UserItem user={user} />)}
            {items.map((item) => <UserItem item={item} deleteUser={deleteUser}/>)}
        </table>
        <Link to='/users/create'>Create</Link>
        </div>
    )
}

export default UserList
