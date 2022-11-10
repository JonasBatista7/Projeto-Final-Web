import React from 'react'
import Produto from './Produto'

export default function Produtos() {
    return (
        <div>
            <h2>Produtos</h2>
            <ul>
            <Produto name={"Meu Produto"}/>
            <Produto name={"Meu Produto 2"}/>

            </ul>
        </div>
    )
}
