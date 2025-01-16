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

    const handleGenerate = async () => {
        if (inputText.trim() === "") {
            alert("Please enter some text!");
            return;
        }

        setLoading(true);

        try {
            const formData = new FormData();
            formData.append('text', inputText);
            formData.append('file', new Blob([inputText], { type: 'text/plain' }), 'file.txt');  // Передаємо текст як файл


            const response = await fetch('http://localhost:8000/generate/', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Failed to generate');
            }

            const data = await response.json();

            setGeneratedData({
                id: data.id || 'N/A',
                link: data.link || 'N/A',
                text: data.text || 'N/A',
                status: data.status || 'N/A',
            });


            const checkStatus = async (id) => {
                const interval = setInterval(async () => {
                    const resultResponse = await fetch(`http://localhost:8000/records/${id}`);
                    const result = await resultResponse.json();

                    if (result.status === 'done') {
                        setGeneratedData(result);
                        clearInterval(interval);
                    }
                }, 11000);
            };

            checkStatus(data.id);  // Перевіряємо статус

        } catch (error) {
            alert('Error: ' + error.message);
        } finally {
            setLoading(false);
        }
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