import React from 'react'
import { Post } from '../models/models'

export interface PostsProps {
    posts:Post[] | undefined
}

const Posts = ({posts}:PostsProps) => {
  return (
    <div>
        {
            posts?.map((post) => {
                return (
                    <>
                     <p>{post.id}</p>
                     <p>{post.content}</p>                    
                    </>
                )
            })
        }
    </div>
  )
}

export default Posts