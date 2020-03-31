import AppApi from '~apijs'

class Auth {
    constructor() {
      this.authenticated = false
    }
    
    authentication() {
        return (        
            AppApi.whomi().then(response => {                
                this.authenticated = response.data.authenticated
            })
        )         
    }
  
    isAuthenticated() {
        return this.authenticated
    }
  }
  
  export default new Auth();
  