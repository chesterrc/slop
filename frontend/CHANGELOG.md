# Changelog

All notable changes to the frontend are documented here.

## [0.1.0] - 2026-08-18

### Added

- Initialized the frontend with Vite, React, and TypeScript.
- Added Vitest and JSDOM for frontend testing.
- Added Testing Library support for component and behavioral tests.
- Added `DocumentUploadPage`.
- Added resume/document file selection using a file input.
- Added an accessible label associated with the document upload input.
- Added conditional rendering of the Submit button when a document is selected.
- Added document upload handling through an abstracted API layer.
- Added a generic `Client` for communicating with backend endpoints.
- Added frontend configuration using `appsettings.json` generated from environment variables.
- Added application startup configuration loading before React renders.
- Added tests for `DocumentUploadPage`, including:
    - Rendering the upload page.
    - Rendering the resume upload prompt.
    - Rendering the document upload input.
    - Hiding the Submit button when no document is selected.
    - Submitting a selected document.
    - Verifying the upload behavior is invoked with the selected file.

Added warm dark color palette and global typography styling.
- Added Bookman/URW Bookman L typography for headings and LLM-generated responses.
- Added centered, responsive document upload layout for desktop and mobile.
- Added fade-in animations for the document upload header and input.
- Added reduced-motion support for accessibility.
- Added styled rounded document upload container.
- Added custom file upload control while retaining the native file input for accessibility.
- Added responsive spacing and styling for the document upload interface.

### Changed

- Organized frontend code around application behavior/features.
- Separated API communication from UI components.
- Separated application configuration from API implementation.
- Added defensive handling for missing files before attempting an upload.

### Testing

- Configured Vitest to use the `jsdom` environment.
- Added support for DOM assertions such as `toBeInTheDocument()` and `toBeVisible()`.
- Added behavioral testing for document upload interactions.