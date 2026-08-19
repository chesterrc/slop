import { Client } from "../client/Client.tsx";

export async function UploadDocument(file: File) {
    const formData = new FormData();

    formData.append("file", file);

    const response = await Client("/api/documents", {
        method: "POST",
        body: formData,
    });

    return response.json();
}
