import React from 'react'
import {Link} from 'react-router-dom'

const UserItem = ({item}) => {
    return (
        <tr>
            <td><Link to={`user/${item.username}`}>{item.username}</Link></td>
            <td>{item.first_name}</td>
            <td>{item.last_name}</td>
            <td>{item.email}</td>
        </tr>
    )
}

const UserList = ({items}) => {
    return (
        <table>
            <tr>
                <th>USERNAME</th>
                <th>FIRST_NAME</th>
                <th>LAST_NAME</th>
                <th>EMAIL</th>
            </tr>
            {items.map((item) => <UserItem item={item} />)}
        </table>
    )
}
    export default UserList