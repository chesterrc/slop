import React from 'react'
import ReactDOM  from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { loadSettings } from "./config/settings.tsx";

async function main() {
    await loadSettings();

    ReactDOM.createRoot(
        document.getElementById("root")!
    ).render(
        <React.StrictMode>
            <App />
        </React.StrictMode>
    );
}

main()