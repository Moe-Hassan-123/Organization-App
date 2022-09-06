import React from 'react'

class card extends React.Component {
    render() {
        <div>
            {/* TODO CSS */}
            <img src={ require('../images/'+this.props.name) } />
            <h3>this.props.name</h3>
        </div>  
    }
  }

function GetUser() {

}

export default GetUser