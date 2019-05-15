var http = require('http'),
    fs = require('fs'),
    spawn = require('child_process').spawn,
    py    = spawn('python', ['compute_input.py', arg1, arg2, arg3, arg4]);

py.stdout.on('data');

fs.readFile('./index.html', function (err, html) {
    if (err) {
        throw err;
    }
    http.createServer(function(request, response) {
        response.writeHeader(200, {"Content-Type": "text/html"});
        response.write(html);
        response.write("hi");
        response.end();
    }).listen(8000);

    py.stdout.on('data', (data) => {
        // Do something with the data returned from python script
        console.log(data)
    });
});