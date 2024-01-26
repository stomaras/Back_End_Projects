exports.getPosts = (req, res, next) => {
    res.status(200).json({
        posts:[{title:'First Post', content:'This is the first stop'}]
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