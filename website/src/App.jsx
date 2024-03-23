import React, { useState } from "react";
import './index.css';
import pdfToText from "react-pdftotext";

function App() {
    const [text, setText] = useState("")

    function extractText(event) {
        const file = event.target.files[0]
        pdfToText(file)
            .then(text => setText(text))
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