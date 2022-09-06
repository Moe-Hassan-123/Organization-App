import React, { useState, useEffect } from 'react'


// main page where all projects are shown
function Main() {
  // Fetches the projects from the Backend
  const [data, setData] = useState([{}])
  useEffect(() => {
    fetch("/projects").then(
       res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])
  
  return (
    <div>
    {(
      (typeof data.projects == 'undefined')
      ? (<p> Loading... </p>)
      : (data.projects.length === 0)
        ?(<p> empty </p>)
        : <p>NOT EMPTY!</p>
    )}
    </div>
  )
}

export default Main