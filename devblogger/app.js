var express       = require('express'),
    handlebars    = require('express-handlebars'),
    devController = require('./server/controllers/blog_list_controller.js'),
    app           = express(),
    mongoose      = require('mongoose'),
    bodyParser    = require('body-parser');

mongoose.connect('mongodb://localhost:27017/devblogger');

app.use(bodyParser.json());

app.get('/', function(req, res) {
	res.sendFile(__dirname + '/client/views/index.html');
});

app.use('/js', express.static(__dirname + '/client/js'));

app.get('/api/posts',devController.list);
app.post('/api/posts',devController.create);

app.listen(3000, function() {
	console.log("Yep I\'m Here");
});

