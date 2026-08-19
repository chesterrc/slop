import type {FunctionComponent} from "react";
import {useState} from "react";

import { UploadDocument } from "./UploadDocument.tsx";

import "./DocumentUploadPage.css"

export const DocumentUploadPage: FunctionComponent = () => {
    const [file, setFile] = useState<File | null>(null);

    function handleFileSelected(event: React.ChangeEvent<HTMLInputElement>) {
        const selectedFile = event.target.files?.[0] ?? null;
        setFile(selectedFile)
    }

    async function handleSubmit(event: React.SubmitEvent) {
        event.preventDefault();

        if (!file) return;

        await UploadDocument(file);
    }

    return (
        <div className="document-upload-page">
            <h1 className="document-upload-header">Please Upload Your Resume</h1>

            <form onSubmit={handleSubmit} className="document-upload-input">
                <label htmlFor="resume-upload">
                    Choose a document
                </label>

                <input
                    type="file"
                    data-testid="resume-upload"
                    accept=".pdf, .doc, .docx"
                    id="resume-upload"
                    onChange={handleFileSelected}
                />

                {file && (
                    <button type="submit" data-testid="submit-button">
                        Submit
                    </button>
                )}
            </form>
        </div>
    )
};