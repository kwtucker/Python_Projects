var DevBlog = require('../models/devblog');

module.exports.create = function(req,res) {
    var devblog = new DevBlog(req.body);
    res.setHeader('Content-Type', 'text/json')
    res.write('you posted:\n');
    res.end(JSON.stringify(req.body, null, 2))
    devblog.save(function(err, result){
    res.json(result);
    });
    console.log(req.body);
};


module.exports.list = function(req,res) {
    DevBlog.find({}, function(err, results){
        res.json(results);
    })
}
