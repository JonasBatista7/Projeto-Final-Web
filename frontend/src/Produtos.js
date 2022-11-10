import React from 'react'
import Produto from './Produto'


export default class  Produtos extends React.Component{
    state = {lists: [], loading:true}
    async componentDidMount(){
        const config = {
            headers : {
                'Content-Type': 'application/json',
                'Authorization': 'Token cf0517dd3818eb8a18e5e3abdd4db0d686de0c89'
            }
        }
        var url = 'http://127.0.0.1:8000/Produto/'
        const response = await fetch(url, config);
        const data = await response.json();
        console.log(data);
        this.setState({lists:data, loading:false});
    }
    render()
    {
        const listApi = this.state.lists;
        return (
            <div>
                <h2>Produtos</h2>
                 {listApi.map(list => <Produto key={list.id} NOME_PRODUTO={list.NOME_PRODUTO} CREATED_BY={list.CREATED_BY} VALOR={list.VALOR}/>)}

            </div>
        )
    }
}