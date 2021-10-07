# csv2arr
Introduction: A simple javascript lib to import csv file and translate it to 2D array.It can automatic detect the file encoding,such as UTF8,GBK(GB2312),BIG-5 and so on.



Compatibility: IE10+,Chrome,Safari,firefox,and fast mode in Chinese browers.IE9 and less is not supported.



Dependence: To use this lib,you should import some other js lib,include jquery, papaparse.js and jschardet.js,which is include in the ./lib directory.If you customer use IE9 or less,you should import base64.js and it's in the ./lib too.



Download the packege and open the demo.html to see how to use,wish you like it.



###simple demo
```
$("input[name=csvfile]").change(function(){
	$(this).csv2arr(function( arr ){
		console.log( arr );
	}
});
```
