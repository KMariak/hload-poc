import React, { useState } from 'react';
import './App.css';

const App = () => {
    const [inputText, setInputText] = useState('');
    const [generatedData, setGeneratedData] = useState({
        id: 'N/A',
        link: 'N/A',
        text: 'N/A',
        status: 'N/A'
    });
    const [loading, setLoading] = useState(false);

    const handleGenerate = () => {
        if (inputText.trim() === "") {
            alert("Please enter some text!");
            return;
        }

        setLoading(true);

        // Simulate an API call or backend process
        setTimeout(() => {
            const data = {
                id: '12345',
                link: 'https://s3.example.com/file12345',
                text: inputText,
                status: 'done'
            };

            setGeneratedData(data);
            setLoading(false);
        }, 2000); // Simulate delay of 2 seconds
    };

    return (
        <div className="container">
            <header>
                <h1>Text Generator</h1>
            </header>
            <main>
                <section className="input-section">
                    <textarea
                        id="inputText"
                        placeholder="Enter your text here..."
                        value={inputText}
                        onChange={(e) => setInputText(e.target.value)}
                    />
                    <button onClick={handleGenerate} disabled={loading}>
                        {loading ? 'Generating...' : 'Generate'}
                    </button>
                </section>
                <section className="output-section">
                    <h2>Output:</h2>
                    <div id="output">
                        <p><strong>id:</strong> <span>{generatedData.id}</span></p>
                        <p><strong>link:</strong> <span>{generatedData.link}</span></p>
                        <p><strong>Text:</strong> <span>{generatedData.text}</span></p>
                        <p><strong>Status:</strong> <span>{generatedData.status}</span></p>
                    </div>
                </section>
            </main>
        </div>
    );
};

export default App;