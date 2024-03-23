import React, { useState } from "react";
import './index.css';
import pdfToText from "react-pdftotext";
import Logo from "./images/logo.png";
// import Background from "./images/back.png";

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
        <div className="backgroundImage">
            <div>
                <img src={Logo} className="logo"/>
            </div>

            <div className="header">
                <h1 className="h1"> Transforming Slides and PDFs into Summarized Notion Pages: </h1>
                <h1 className="h2"> SUSAN - Your Ultimate Productivity Companion </h1>           
                <input className="file" type="file" accept="application/pdf" style={{
                    border: '2px solid #2aff78',
                    borderRadius: '0.6rem',
                    padding: '10px',
                    fontSize: '17px' /* Optional: Adjust the font size as needed */
                }}/>
            </div>
            <svg className="header-lines" width="1331" height="409" viewBox="0 0 1731 409" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path className="line line--blue" d="M-210.326 -327C-210.326 -327 -38.3196 165.621 334.574 120.5C707.468 75.3784 868.584 134 1001.57 213.59C1134.56 293.179 1150.57 266.276 1217.45 222.385" stroke="#3B42B6" strokeLinecap="round" strokeDasharray="1685.669678" strokeDashoffset="0" style={{ opacity: 1, visibility: 'inherit' }}></path>
                    <path className="line line--green" d="M-482 107.169C-482 107.169 -30.4973 149.92 315.751 78.4576C662 6.99545 748.965 362.27 897.733 270.633C1046.5 178.995 1155.86 393.995 1235.93 310.245C1316 226.495 1320.5 216.996 1374.49 255.451C1426.83 292.732 1669 431.995 1726.38 307.721" stroke="#288453" strokeLinecap="round" strokeDasharray="2383.108154" strokeDashoffset="0" style={{ opacity: 1, visibility: 'inherit' }}></path>
                    <path className="line line--yellow" d="M-387.844 257.501C-387.844 257.501 -264.467 202.051 108.426 156.93C481.32 111.809 672.617 283.229 724.238 307.59C775.859 331.952 873.235 360.277 940.113 316.386C957.15 303.424 1026.41 247.5 1138.19 350.501C1201.41 408.762 1280.25 427.365 1312.58 369C1332.24 333.5 1347.76 211.001 1455.4 240.501" stroke="#857D15" strokeLinecap="round" strokeDasharray="2024.220581" strokeDashoffset="0" style={{ opacity: 1, visibility: 'inherit' }}></path>
            </svg>
            
            <div>
                <p>{text}</p>
            </div>
        </div>
      );
}

export default App;