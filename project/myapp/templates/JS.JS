fetch('http://127.0.0.1:8000/h/')
.then(result=>
{
	console.log(result);
	return result.jsone();
})
.then(data =>{
	console.log(data)
}
)
.catch(error => console.log(error))