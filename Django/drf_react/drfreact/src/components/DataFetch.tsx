import React from 'react'
import { useEffect, useState } from 'react'
import { Post } from '../models/models';
import Posts from './Posts';


const DataFetch = () => {

    const [posts,setPosts] = useState<Post[]>();

    useEffect(() => {
        const apiUrl = 'http://127.0.0.1:8000/api/';
        const fetchData = async() => {
            try {
                const response = await fetch(apiUrl);
                if(!response.ok) {
                    throw new Error('Network ')
                }

                const data = await response.json();
                console.log(data);
                setPosts(data)
                
            }catch(error){

            }
        }
        fetchData();
    },[]);

  return (
    <div>
        <Posts posts={posts}/>
        
    </div>
  )
}

export default DataFetch