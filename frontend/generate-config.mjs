import fs from "node:fs";
import path from "node:path";

const apiUrl = process.env.API_URL;

if (!apiUrl) {
    throw new Error("API_URL environment variable is required");
}

const config = {
    apiUrl,
};

const outputPath = path.resolve("public/appsettings.json");

fs.writeFileSync(
    outputPath,
    JSON.stringify(config, null, 2)
);

