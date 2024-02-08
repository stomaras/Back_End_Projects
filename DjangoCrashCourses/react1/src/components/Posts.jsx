import React from 'react'

const Posts = ({posts}) => {
  return (
    posts.map((post) => {
      return (  
      <article key={post.id}>
        <ul className='ul-post'>
          <li className='li-post'>{post.id}</li>
          <li className='li-post'>{post.title}</li>
        </ul>
      </article>
      )
    })
  )
}

export default Posts