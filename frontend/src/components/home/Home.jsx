import React, {Component} from 'react'
import Main from '@components/template/Main'

class Home extends Component {    

    render() {        
        
        return (
            <Main icon="home" title="Início"
                subtitle="Seu projeto React com uso de dados mock"
            >
                <h1>home</h1>                  
            </Main>
        )
    }
}
  export default Home
