import React, { useState } from "react";
import './index.css';
import pdfToText from "react-pdftotext";

function App() {
    const [text, setText] = useState("")

    function extractText(event) {
        const file = event.target.files[0]
        pdfToText(file)
            .then(text => {
              // setText(text)
              console.log(typeof(text))
              fetch('http://127.0.0.1:8000/pdf_insert/', {
                method: 'POST',
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                  text: text,
                })
              }).then((res) => {
                console.log(res)
              })
              console.log("I AM HERE")
            })
            .catch(error => console.error("Failed to extract text from pdf"))
    }
    
    return (
        <div>
          <h1>PDF Text Extractor</h1>
          <input type="file" accept="application/pdf" onChange={extractText} />
          <div>
            <h2>Extracted Text:</h2>
            <p>{text}</p>
          </div>
        </div>
      );
}

export default App;