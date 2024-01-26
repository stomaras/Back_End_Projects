exports.getPosts = (req, res, next) => {
    res.status(200).json({
        posts:[
            {
                _id:'1',
                title:'First Post', 
                content:'This is the first stop', 
                imageUrl: 'images/image.jpg',
                creator: {
                    name:'Tom'
                },
                createdAt: new Date(),
            }
        ]
    });
};

exports.createPost = (req, res, next) => {
    const title = req.body.title;
    const content = req.body.content;
    console.log(title,content);
    // create post in db
    // 201 indicates that we created a resource
    res.status(201).json({
        message:'Post created successfully',
        post: {id: new Date().toISOString(), title: title, content:content}
    });
}