import './Cards.css'
import React from 'react'
import { Link } from 'react-router-dom'

const Card = (props) => {    
    return (        
        <div className="column is-one-third">
            <div className="card">
                <div className="card-image ">
                    <figure className="image is-4by3">                        
                        <Link to={`/template/${props.name}`}><img src={props.image} alt="" /></Link>                        
                    </figure>
                </div>
                <div className="card-content">
                    <div className="media">                                    
                        <div className="media-content">
                            <p className="title is-4 no-padding">{props.title}</p>                                        
                        </div>
                    </div>
                    <div className="content">
                        {props.description}                                               
                    </div>                    
                    <div className="columns">
                        <div className="column">
                            <a className="button is-outlined is-cart"><span><i className="fa fa-shopping-cart" aria-hidden="true"></i></span></a>
                            <a href={props.demo} className="button is-outlined is-orange"><span> Demo</span></a>
                        </div>                        
                    </div>                                  
                </div>
            </div>
        </div>            
    )    
}

export default Card