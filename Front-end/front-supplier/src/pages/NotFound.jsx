import React from 'react'
import { Link } from 'react-router-dom'

const NotFound = () => {
    return (
        <div style={{ textAlign: 'center' }}>
            <h1>Página não encontrada!</h1>
            <p>Volte para página Base <Link to='/'>Home</Link></p>
        </div>
    )
}

export default NotFound