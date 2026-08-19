import { getSettings } from "../../config/settings";

export async function Client(
    endpoint: string,
    options: RequestInit = {}
) {
    const { apiUrl } = getSettings();

    const response = await fetch(`${apiUrl}${endpoint}`, {
        ...options,
    });

    if (!response.ok) {
        throw new Error(
            `API request failed: ${response.status}`
        );
    }

    return response;
}
