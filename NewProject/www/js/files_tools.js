'use strict';

function openFile(fname) {
    cordova.plugins.fileOpener2.open(
        `${cordova.file.externalRootDirectory}/download/${fname}`,
        `application/${fname.split('.')[fname.split('.').length - 1]}`,
        {
            error : function(e) {
              if (e.status === 9) {
                alert('Ошибка при открытии: нет приложения для открытия данного формата файлов');
              } else {
                alert(`Ошибка при открытии: ${JSON.stringify(e)}`);
              }
              console.log(JSON.stringify(e));
            }
        }
      );
}

function downloadAndOpenFile(uri, fname) {
    let filePath = `${cordova.file.externalRootDirectory}/download/${fname}`,
        fileTransfer = new FileTransfer();

    fileTransfer.download(encodeURI(uri), filePath,
      function (entry) {
        openFile(fname);
      },
      function (error) {
        alert('Ошибка при скачивании файла');
      },
      true
    )
}

function handleFile(uri, fname){
  let path = `${cordova.file.externalRootDirectory}/download/${fname}`;
  window.resolveLocalFileSystemURL(
    path,
    function() {
      console.log('already downloaded');
      openFile(fname);
    },
    function() {
      console.log('not downloaded yet');
      downloadAndOpenFile(uri, fname);
    }
  )
}

function askForPermission(uri, fname) {
  let permissions = cordova.plugins.permissions;
  permissions.requestPermission(permissions.READ_EXTERNAL_STORAGE, function(status) {
    if (status.hasPermission) {
      handleFile(uri, fname);
    } else {
      console.log('Нет прав для чтения папки Download');
    }
  }, null)
}

function checkForPermission(uri, fname) {
  let permissions = cordova.plugins.permissions;
  permissions.checkPermission(permissions.READ_EXTERNAL_STORAGE, function (status) {
    if (status.hasPermission) {
      handleFile(uri, fname);
    } else {
      askForPermission(uri, fname);
    }
  }, null)
}

function openFileCallback(uri, fname) {
  checkForPermission(uri, fname);
}