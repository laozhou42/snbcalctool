$(function(){
  var obj = $("#drop_zone");
  obj.on('dragenter', function (e){
    e.stopPropagation();
    e.preventDefault();
    $(this).css('border', '2px solid #bbb');
  });

  obj.on('dragover', function (e){
    e.stopPropagation();
    e.preventDefault();
  });

  obj.on('drop', function (e){
    $(this).css('border', '2px dashed #bbb');
    e.preventDefault();
    var files = e.originalEvent.dataTransfer.files;

    //We need to send dropped files to Server
    handleFileUpload(files,obj);
  });

  function handleFileUpload(files,obj){
    for (var i = 0; i < files.length; i++) {
      var fd = new FormData();
      fd.append('file', files[i]);
      sendFileToServer(fd,status);
    }
  }

  function sendFileToServer(formData){
    var extraData ={}; //Extra Data.
    var jqXHR=$.ajax({
      url: upload_url,
      type: "POST",
      contentType:false,
      processData: false,
      cache: false,
      data: formData,
      success: function(data){
        alert('file upload success');
        var respObj = JSON.parse(data);
        if (respObj.success){
          requestRecordsToXueqiu(respObj.filename);
        }else{
          alert(respObj.message);
        }
      },
      error: function(xhr, status, err) {
        alert('File upload failed, Server error');
      }
    });
  }

  function requestRecordsToXueqiu(filename) {
    var data = {
      'filename': filename
    };
    $.ajax({
      url: import_to_snb_url,
      dataType: 'json',
      type: 'POST',
      data: data,
      success: function(data) {
        if (data.success) {
          alert('import success');
        } else {
          alert('import failed');
        }
      },
      error: function(xhr, status, err) {
        alert('服务器错误');
      }
    });
  },
  }
})
