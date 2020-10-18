function openPdf(fileName, mimeType)
{
    console.log("Copying: "+fileName);
    var filePath = cordova.file.applicationDirectory+"www/files/"+fileName;
    console.log("FilePath: "+filePath);
    window.resolveLocalFileSystemURL(filePath,function (fileEntry)
    {
        console.log("cordova.file.applicationDirectory enter success");
        window.resolveLocalFileSystemURL(cordova.file.dataDirectory,function (directory)
        {
            console.log("cordova.file.dataDirectory: "+cordova.file.dataDirectory);
            fileEntry.copyTo(directory, fileName,function()
            {
                console.log("Successful Copy!");
                cordova.plugins.fileOpener2.open(
                cordova.file.dataDirectory+"/"+fileName,
                'application/pdf',
                {
                    error : function(e){
                        console.log('Error status: ' + e.status + ' - Error message: ' + e.message);
                    },
                    success : function () {
                        console.log('file opened successfully');
                    }
                 });
            },
            function()
            {
                console.log("Copying Unsuccessful");
                alert('Copying Unsuccessful ');
            });
        },null);
    }, null);
}