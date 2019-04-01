const fs = require('fs'); 
const csv = require('csv-parser');

fs.createReadStream('description.csv')
.pipe(csv())
.on('data', function(data){
    try {
     if(data.disease)
     	if(data.disease=='HIV')
     		console.log(data.treatment)
    }
    catch(err) {
        //error handler
        if(err)
        	console.log('general disease is ')
    }
})
  