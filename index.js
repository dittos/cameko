var spawn = require('child_process').spawn;
var readTorrent = require('read-torrent');
var torrentStream = require('torrent-stream');

readTorrent(process.argv[2], function(err, torrent) {
    if (err) {
        console.error(err);
        return;
    }

    var engine = torrentStream(torrent);

    engine.on('ready', function() {
        engine.files.forEach(function(file) {
            console.log('filename:', file.name);
            var avconv = spawn('avconv', [
                '-i', 'pipe:',
                '-vsync', '0',
                '-vf', "select='eq(pict_type\,I)'",
                '-f', 'image2',
                '%d.png'
            ], {
                stdio: ['pipe', process.stdout, process.stderr]
            });
            avconv.on('close', function(code) {
                console.log('avconv exit code: ' + code);
                // Clear up things
                engine.remove(function() {
                    engine.destroy();
                });
            });
            file.createReadStream().pipe(avconv.stdin);
        });

        engine.on('idle', function() {
            console.log('download finished');
        });

        engine.on('download', function(i) {
            console.log('piece downloaded: ' + i);
        });
    });
});
