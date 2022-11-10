import React from 'react'

export default function Produto(props) {
    return <li> 
        <p>{ props.NOME_PRODUTO }</p>
        <p>{ props.CREATED_BY }</p>
        <p>{ props.VALOR }</p>
        <p>{ props.QUANTIDADE_ESTOQUE }</p>
        <p>{ props.DESCRICAO}</p>
</li>
}
