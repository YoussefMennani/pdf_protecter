const HummusRecipe = require('hummus-recipe');
var http = require('http');

//create a server object:
http.createServer(function (req, res) {

    if(req.url != '/favicon.ico'){

        console.log("--------------- *** START PROCESS PROTECTING PDF *** ---------------")

            cryptePdf("saample.pdf","1234","neewPdf.pdf").then((value) =>{
                res.write('Hello World!'); //write a response to the client
                res.end(); //end the response
            }) 

        console.log("----------------------- *** END PROCESS *** -----------------------")
    }

}).listen(8080); //the server object listens on port 8080

console.log("Server nodejs running on port 8080..")



async function cryptePdf(path,password,newPath){

    try {
        const pdfDoc = new HummusRecipe(path, newPath);
        
            pdfDoc.encrypt({
                userPassword: password,
                ownerPassword: password,
                userProtectionFlag: 4
            }).endPDF();

            console.log(" -->  PDF  '"+path+"'  CRYPTED with success  ");
            pdfDoc = new HummusRecipe(inputPath, outputPath);
    } catch (error) {
        
        console.log("--> ERROR WARNING : "+error.message );
        /*if (error.message === 'TypeError: Unable to start parsing PDF file') {
            console.log("########### Unable to start parsing PDF file" );
    }*/
    }

}