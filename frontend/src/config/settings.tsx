import type { Settings } from "./settings.types";

let settings: Settings;

export async function loadSettings() {
    const response = await fetch("/appsettings.json");

    if (!response.ok) {
        throw new Error("Failed to load application settings");
    }

    settings = await response.json();
}

export function getSettings(): Settings {
    if (!settings) {
        throw new Error("Settings have not been loaded");
    }

    return settings;
}
