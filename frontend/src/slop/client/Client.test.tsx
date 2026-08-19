const API_URL = "place this in a .env";

export async function apiClient(
    endpoint: string,
    options: RequestInit = {}
) {
    const response = await fetch(`${API_URL}${endpoint}`, {
        ...options,
    });

    if (!response.ok) {
        throw new Error(`API request failed: ${response.status}`);
    }

    return response;
}
