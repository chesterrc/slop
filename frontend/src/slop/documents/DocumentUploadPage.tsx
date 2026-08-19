import type {FunctionComponent} from "react";
import {useState} from "react";

import { UploadDocument } from "./UploadDocument.tsx";


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
        <div>
            <h1>Please Upload Resume</h1>

            <form onSubmit={handleSubmit}>
                <label htmlFor="resume-upload"> Upload Your Resume </label>
                <input type="file" data-testid="resume-upload" accept=".pdf, .doc, .docx" onChange={handleFileSelected} />

                {file && (
                    <button type="submit" data-testid="submit-button">
                        Submit
                    </button>
                )}
            </form>
        </div>
    )
};